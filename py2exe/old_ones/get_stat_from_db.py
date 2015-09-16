# -*- coding: utf-8 -*-
import MySQLdb
import time

release_member={'o.polishchuk':['Olena Polishchuk'],'s.tischenko':['Sergiy Tischenko'],
                'y.fam':['Yaroslav Fam'],'s.tolokevych':['Svetlana Tolokevych']}

day_start=time.strftime("%Y-%m-%d",time.gmtime(time.time()-604800)) #(2014-08-27)

try:
    con=MySQLdb.connect(host='106.125.52.31', user='rs', passwd='Metallica21', db='rs')
    cur = con.cursor()
    #cur.execute('SET NAMES `utf8`')
    #INSERT INTO `rs`.`stat` (`id`, `date`, `user_id`, `approver_id`, `binary_type_id`, `project`, `version`) VALUES (NULL, '2014-02-18 02:08:10', '1', '0', '1', '9100', '9sg9sdeg9es4des9hb');
except:
    print 'Connection failed! Rollback MySQLdb!!!'

cur.execute("SELECT * FROM  `release_stat` WHERE  `date` >=  '"+day_start+" 12:00:00'")
members={row:row[2] for row in cur}  #dict with db id:user from user table

release_data=members.keys()
#print members.keys()[0:10]

for member in sorted(release_member.keys()):
    i=0
    all_release=0
    all_smd=0
    release=0
    smd=0
    for data in release_data:
        #print data
        i+=data[1:].count(member)
        all_release+=data[1:].count("S/W")
        all_smd+=data[1:].count("SMD")
    release_member[member].append(i)
    #print member,i
f=open("release_report.txt","w")
f.write( "From "+day_start+" 12:00:00\n")
f.write("Release - "+str(all_release) +"\nSMD -"+str(all_smd)+"\n")
for member_id,member in zip(sorted(release_member.values()),sorted(release_member.keys())):
    f.write( member_id[0]+'('+member+') - '+str(member_id[1])+' request\n')
f.close()    
print "Done!"
