#!/usr/bin/python
# -*- coding: utf-8 -*-

import poplib, email,re,time
import MySQLdb
from email.header import decode_header

server='POP3.W1.SAMSUNG.COM'
port='995'
login='s.tischenko'
password2='tishyk1986'
password1='adelaida01'


try:
    con=MySQLdb.connect(host='106.125.52.31', user='rs', passwd='Metallica21', db='rs')
    cur = con.cursor()
    #cur.execute('SET NAMES `utf8`')
    #INSERT INTO `rs`.`stat` (`id`, `date`, `user_id`, `approver_id`, `binary_type_id`, `project`, `version`) VALUES (NULL, '2014-02-18 02:08:10', '1', '0', '1', '9100', '9sg9sdeg9es4des9hb');
except:
    print 'Connection failed! Rollback MySQLdb!!!'

day=time.strftime("%a", time.localtime())

def get_stat():
    
    box = poplib.POP3_SSL(server)
    box.user(login)
    try:
        box = poplib.POP3_SSL(server)
        box.user(login)
        box.pass_(password1)
        lst = box.list()[1]
    except:
        box = poplib.POP3_SSL(server)
        box.user(login)
        box.pass_(password2)
        lst = box.list()[1]
    print ("Debug: Total messages to %s : %s" % (login, len(lst)))

    cur.execute('SELECT `id`,`user` FROM `release_user`')
    members={row[0]:row[1] for row in cur}  #dict with db id:user from user table
    print members
    
    for msnum in [i.split()[0] for i in lst[::-1] ]:
        lines=box.retr(msnum)[1]
        msgtext='\n'.join(lines)+'\n\n'
        message=email.message_from_string(msgtext)
        time_str = message["Date"] # Mon, 10 Feb 2014 06:17:35 +0000
        
        if message["Date"]: #add day in for 1 day
            #Get and decode Subject from object Message
            h = decode_header(message['Subject'])
            if h[0][1] == 'utf-8' or 'None':
                subject = h[0][0].decode(h[0][1]) if h[0][1] else h[0][0]
            elif h[0][1] == 'iso-8859-5':
                subject = h[0][0].decode('iso-8859-5')
            else:
                subject=''
            # filter creation for messages 'if required result not  in subject - next'
            try:
                if '[결재 통보][myProject]'.decode('utf-8') not in subject:
                    continue
                else:
                    subject=subject.replace('[결재 통보][myProject]'.decode('utf-8'),'')
                    sender = message['From']
                    #there were members :)     
                    if [subject for member in members.values() if member in sender]:
                        subj=re.findall('\w\d\w+_\w+',subject.replace(' / ','_'))
                        version=subj[1]
                        user_id=[user_id for user_id, member in members.items() if member in sender][0]
                        user=members[user_id]
                        print user
                        
                        if "_SW" in subj[0]:
                            bin_type_id=0
                            bin_type="S/W"
                            project=subj[0].replace("_SW","")
                        else:
                            bin_type_id=1
                            bin_type="SMD"
                            project=subj[0].replace("_SMD","")
                        print bin_type_id, bin_type
                        
                        time_obj=time.strptime(time_str.replace('+0000 ',''),"%a, %d %b %Y %H:%M:%S (%Z)")
                        #print time_obj , time.localtime((time.mktime(time_obj)+7200)),'\n'*2   Debug
                        time_obj=time.localtime((time.mktime(time_obj)+7200))
                        now_time=time.strftime("%Y-%m-%d %H:%M:%S", time_obj)
                    
                        # Get approver from message body
                        text = unicode(message.get_payload(decode=True), message.get_content_charset(), 'ignore').encode('utf8', 'replace')
                        text_temp=re.findall('>승인<.{400}',text.replace('\n',' '))
                        app_vacantion=[re.findall('.+</a>',approver)[0].replace('</a>','') for approver in text_temp[0].split('#cccccc solid;" namo_lock>') if '</a></td>\r' in approver][0]
                        approver=app_vacantion.replace(' Engineer','')
                        approver=approver.replace(' Lead','')
                        
                        #Get approver,id from db if no - add to db and get id
                        cur.execute('SELECT `id`,`approver` FROM `rs`.`release_approver`')
                        a_member={row[0]:row[1] for row in cur}  #dict with db id:approver from approver table
                        print approver
                        
                        if approver not in a_member.values():
                            cur.execute('INSERT INTO `rs`.`release_approver` (`approver`) VALUES (%s)', (approver))
                            cur.execute('SELECT `id`,`approver` FROM `rs`.`release_approver`')
                            a_member={row[0]:row[1] for row in cur}
                            print 'approver was added'
                        
                        cur.execute('SELECT `binary_type`,`version` FROM `rs`.`release_stat` WHERE `binary_type`=%s AND `version`=%s ',(bin_type, version))
                        in_db=[row for row in cur]  #dict with db id:approver from approver table
                        #print in_db

                        if len(in_db)>=1:
                            print now_time, user, approver, bin_type, project, version
                            print 'Binary present in db! Script exit!'
                            break
                            #continue
                        
                        else:
                            print now_time, user, approver, bin_type, project, version
                            try:
                                cur.execute("""INSERT INTO `release_stat` (`date`, `user`, `approver`, `binary_type`, `project`, `version`)  VALUES (%s,%s,%s,%s,%s,%s) """,
                                            (now_time, user, approver, bin_type, project, version))
                                print 'Binary was added to db!' 
                            except :
                                print(con.error())
                        con.commit()
                        print "pass"
            except:
                print "\nPass non encode string\n"

        else:
            print "Scan Done for "+day
            open("Done!.txt","w").write("Mail successfully scaned!")
            break


get_stat()






         
