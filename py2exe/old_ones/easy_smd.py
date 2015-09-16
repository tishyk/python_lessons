# -*- coding: cp1251 -*-
import os,paramiko
from Tkinter import*
from file_scanner import*
from tkFileDialog import *

root=Tk()
win=Toplevel(root)
win.title('-|-')

root.title('Easy SMD creation')
root.iconify()
root.minsize(width=440,height=320)
fr1=Frame(root)
fr2=Frame(root)

#variables

login_l,passwd_l,Model_l=[],[],[]
host='106.125.32.180'
port=22


f=open('ini.txt')

for line in f.readlines():
    if 'curdir:' in line:
        curdir=line.split('curdir:')[1].rstrip()
    if 'login' in line:
        login_l.append(line.split('login:')[1].rstrip())

print (curdir,type(curdir))

#curdir=os.path.abspath(os.curdir)# 1 st version
smd_remote='SMD_auto'


#def for smd

def ssh_command(command):
    try:
        if __name__=='__main__':
#            paramiko.util.log_to_file(curdir+'\\connection.log')
            s=paramiko.SSHClient()
            s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            s.load_system_host_keys()
            s.connect(host,port,login_l[0],passwd_l[0])#connection
            stdin,stdout,stderr=s.exec_command(command)
            text = stdout.read() + stderr.read()
            return text,host
            
    except ValueError:
        print ('Connection failed', ValueError)
        pass
    
#smd file transfer to
    
def transport_to(user,passwd,sftp_files):
    try:
        text=''
        transfer = paramiko.Transport((host, port))
        transfer.connect(username=user, password=passwd)
        sftp = paramiko.SFTPClient.from_transport(transfer)
        for sftp_file in sftp_files:
            if 'HOME_' in sftp_file:
                continue
            sftp.put(curdir+'/'+sftp_file, 'SMD_auto/output/'+sftp_file)
            text+='\n-- '+sftp_file+' -- Succesfully copied!!!\n'

        sftp.close()
        transfer.close()
        
    except:
        t_log.insert(END,'Failed in copy files to server!!!')
        pass
    return text,sftp_file


#smd file transfer from local for smd

def transport_from(user,passwd,sftp_files):
    try:
        text=''
        transfer = paramiko.Transport((host, port))
        transfer.connect(username=user, password=passwd)
        sftp = paramiko.SFTPClient.from_transport(transfer)
        
        for sftp_file in sftp_files:
            try:
                sftp.get(sftp_file, curdir+'/'+ver_name(Model_l[0])+'/'+sftp_file.split('/')[-1])
                text+='\n-- '+sftp_file+' -- Succesfully copied!!!\n'

            except:
                pass
        sftp.close()
        transfer.close()
        
    except:
        t_log.insert(END,'Failed in copy files from server!!!')
        pass
    return text,sftp_file


#smd file transfer for HOME
def transport_to_home(user,passwd,sftp_files):
    try:
        text=''
        transfer = paramiko.Transport((host, port))
        transfer.connect(username=user, password=passwd)
        sftp = paramiko.SFTPClient.from_transport(transfer)
        for sftp_file in sftp_files:
            if 'HOME_' in sftp_file:
                sftp.put(curdir+'/'+sftp_file, 'SMD_auto/output/'+sftp_file)
                text+='\n-- '+sftp_file+' -- Succesfully copied!!!\n'
        sftp.close()
        transfer.close()
        
    except:
        t_log.insert(END,'Failed in copy files to server!!!')
        pass
    return text,sftp_file


    
#def event for Top level

def login(event):
    try:
        t_log.delete(1.0,END)
        login_l.append(ent_l.get())
        passwd_l.append(ent_p.get())
        Model_l.append(ent_m.get())
        ent.insert(0,Model_l[0])
        if len(login_l[0])>0:
            t_log.insert(END,'Logged as: '+login_l[0]+'\n\n')
            text=scanner(Model_l[0])
            t_log.insert(END,text[-1])
        else:
            t_log.insert(END,'Restart for Log in !!! '+'\n\n\n')
           
        #create connection to host & cleand server folder

        temp=' cleaned!\n\nPress "Copy to host" and wait untill copyng to linux server will be finished!'
        t_log.insert(END,'\n\nConnection established to '+host+'\nFolder '+smd_remote+temp)
        t_ver.insert(END,ver_name(Model_l[0]))
        # check SMD folder
        if not os.path.exists(ver_name(Model_l[0])):
            os.makedirs(ver_name(Model_l[0]))
    except:
        print('Data Failed!!!  Please restart!')
        t_log.delete(1.0,END)
        t_log.insert(END,'Data Failed!!!  Please restart!')
    root.deiconify()
    btn1.focus()
    btn3.config(state=NORMAL)
    win.destroy()
#SMD creation def
    
def generate(event):
    
    print t_log.get(1.0,END)
    if 'Folder SMD_auto cleaned!' in t_log.get(1.0,END):
        t_log.delete(2.0,END)
        try:
            ssh_command('rm -rf SMD_auto')
            ssh_command('mkdir SMD_auto')
            ssh_command('cd SMD_auto;cp -a //home/s.tischenko/'+Model_l[0]+'/* .')
            command='rm -rf SMD_auto/output;mkdir SMD_auto/output'
            ssh_command(command)
            scan=scanner(Model_l[0])
            print scan[0],type(scan[0])
            transfer_to=transport_to(login_l[0],passwd_l[0],scan[0])
            print transfer_to[0]
            t_log.insert(END,'\n'+transfer_to[0])
            t_log.insert(END,"\nPress Next for SMD generation and downloading from server! (About 5 min!!!)\n")
            btn3.focus()
            btn3.config(state=NORMAL)
            btn1.config(state=DISABLED)
        except:
            pass
def gen_smd(event):
    #SMD step
    if c1.get()==1:
        try:
            if 'Press Next for SMD generation and downloading from server!' in t_log.get(1.0,END):
                t_log.delete(2.0,END)
                ssh_com=ssh_command('cd SMD_auto;ls')
                for x in ssh_com[0].split('\n'):
                    if '.sh' in x:
                        sh_com=x
                        continue
                t_log.insert(END,'\nUsed file - '+sh_com+'\n')
                command='cd SMD_auto;chmod 777 -R *;./'+sh_com
                ssh_con=ssh_command(command)
                ssh_com=ssh_command('chmod 777 -R *;find SMD_auto/ user '+login_l[0])
                smd_file=[]
                for f in ssh_com[0].split('\n'):
                    if 'md5.img' in f:
                        smd_file.append(f)
                        print f,type(f)
                    if 'md5_' in f:
                        smd_file.append(f)
                        print f,type(f)
                    if 'smd.pit' in f:
                        smd_file.append(f)
                        print f,type(f)
                    if '.bin' in f:
                        smd_file.append(f)
                        print f,type(f)
                    if 'emmc' in f:
                        smd_file.append(f)
                        print f,type(f)
    #            t_log.insert(END,ssh_con[0])        
                t=transport_from(login_l[0],passwd_l[0],smd_file)    
                t_log.insert(END,t[0])
                t_log.insert(END,'\n SMD DONE!!!\n')
                c1.set(0)
        except:
            t_log.insert(END,'\nNo sh file! SMD creation failed!\n')
            pass
    #HOME step
    if c2.get()==1:
        if c1.get()==0:
            print 'Ready for HOME'
#            t_log.delete(2.0,END)
            ssh_con=ssh_command('cd SMD_auto/output/;rm -f CSC*')
            scan=scanner(Model_l[0])
            transfer=transport_to_home(login_l[0],passwd_l[0],scan[0])
            t=scanner(Model_l[0])
            for f in t[0]:
                ssh_con=ssh_command('cd SMD_auto/output/;cp //home/s.tischenko/addmd5sum.sh .;chmod 777 -R *;tar -xvf '+f+';chmod 777 -R *')
#                t_log.insert(END,'\n\n'+ssh_con[0])
            ssh_con=ssh_command('cd SMD_auto/output/;tar -cvf '+ver_name(Model_l[0])+'_HOME.tar '+scan[1]+';rm -f *tar.md5;./addmd5sum.sh -d ./')
#            t_log.insert(END,'\n\n'+ssh_con[0])
            #get smd home from server
            ssh_com=ssh_command('chmod 777 -R *;find SMD_auto/ user '+login_l[0])
            smd_file=[]
            for f in ssh_com[0].split('\n'):
                if 'HOME.tar.md5' in f:
                    smd_file.append(f)
                    print f,type(f)
            t=transport_from(login_l[0],passwd_l[0],smd_file)    
            t_log.insert(END,t[0]+'\n SMD HOME DONE!!!\n')
            print smd_file,type(smd_file)
            c2.set(0)
            btn3.config(state=DISABLED)
            btn1.config(state=NORMAL)


#Toplevel w

l_login=Label(win,text='Login',fg='darkblue')
l_pass=Label(win,text='Password',fg='darkblue')
l_model=Label(win,text='Model',fg='darkblue')

ent_l=Entry(win,width=17,relief='sunken',bd=3,fg='darkblue')
ent_p=Entry(win,width=17,relief='sunken',bd=3,fg='darkblue',show="*")
ent_m=Entry(win,width=17,relief='sunken',bd=3,fg='darkblue')
btn2=Button(win,text='Log in',width=14,fg='darkblue')

#Toplevel w grid
ent_l.focus()
l_login.grid(row=1,column=1,sticky=N,pady=2,padx=20)
ent_l.grid(row=2,column=1,sticky=N,pady=2,padx=20)
l_pass.grid(row=3,column=1,sticky=N,pady=2,padx=20)
ent_p.grid(row=4,column=1,sticky=N,pady=2,padx=20)
l_model.grid(row=5,column=1,sticky=N,pady=2,padx=20)
ent_m.grid(row=6,column=1,sticky=N,pady=2,padx=20)
btn2.grid(row=7,column=1,sticky=N,pady=10,padx=20)
btn3=Button(fr1,text='Next  >>>',width=14,fg='darkblue')

if len(login_l)>=1:
    ent_l.insert(0,login_l[0])

#Toplevel event

btn2.bind("<Button-1>",login)
ent_l.bind("<Return>",login)
ent_p.bind("<Return>",login)
ent_m.bind("<Return>",login)


#frame1 w
lmodel=Label(fr1,text='Model name:',fg='darkblue')
ent=Entry(fr1,fg='darkblue',width=17,relief='sunken')
btn1=Button(fr1,text='Copy to host',width=14,fg='darkblue')
btn3=Button(fr1,text='Next  >>>',width=14,fg='darkblue',state=DISABLED)

c1 = IntVar()
c2 = IntVar()
c1.set(1)
c2.set(1)
che1 = Checkbutton(fr1,text="SMD",
          variable=c1,onvalue=1,offvalue=0)
che2 = Checkbutton(fr1,text="SMD HOME",
          variable=c2,onvalue=1,offvalue=0,)

#frame2 

lver=Label(fr2,text='  SMD version name:  ',fg='darkblue')
t_ver=Text(fr2,width=50,height=1,font="Verdana 10",relief='groove')
t_log=Text(fr2,width=100,font="Verdana 8",wrap=WORD,fg='darkblue',relief='groove')

#root binding
btn1.bind("<Button-1>",generate)
btn3.bind("<Button-1>",gen_smd)
root.bind("<Return>",generate)
btn3.bind("<Return>",gen_smd)
    
#frame1 grid

lmodel.grid(row=1,column=1,sticky=W,pady=2,padx=3)
ent.grid(row=2,column=1,sticky=W,pady=10,padx=3)
btn1.grid(row=3,column=1,sticky=W,pady=10,padx=3)
che1.grid(row=4,column=1,sticky=W,pady=2,padx=3)
che2.grid(row=5,column=1,sticky=W,pady=2,padx=3)
btn3.grid(row=6,rowspan=5,column=1,sticky=S,pady=20,padx=3)

#frame2 grid

lver.grid(row=1,column=1,sticky=E,pady=3,padx=3)
t_ver.grid(row=1,column=2,sticky=E,pady=3,padx=15)
t_log.grid(row=2,column=1,columnspan=2,sticky=W,pady=2,padx=3)

fr1.grid(row=1,column=1,sticky=N)
fr2.grid(row=1,column=2,sticky=E)



root.mainloop()
