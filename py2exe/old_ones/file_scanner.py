# -*- coding: utf-8 -*-
import glob

#bootloader to boot

def scanner(model,curdir):
    try:
        smd_label=model+':SMD filelist:'
        home_label=model+':Home filelist:'
        smd_filelist=[]
        sh_name=''
        sftp_filelist=[]
        text_smd_file=''
        fls=[]
        
        #open ini.txt file
        try:
            f=open('ini.txt')
        except:
            text_smd_file+="--Can't open ini.txt--"
            pass
        #scanning ini smd files list creation and home file list creation
        for line in f.readlines():
            if model in line:
                if smd_label in line:
                    smd_filelist.append(line.rstrip())
                    fls=smd_filelist[0].split(',')# count number of files(AP,CP..)
                    fls[0]=fls[0].replace(smd_label,'')
                    text_smd_file+=smd_label+str(fls)+"\n"
                    
                if home_label in line:
                    
                    home_tar_filelist=line.rstrip()
                    home_tar_filelist=home_tar_filelist.replace(home_label,'')
                    text_smd_file+='HOME files:'+home_tar_filelist+"\n\n"
    except:
        pass
    #scan current folder and creation list for sftp transfer
    source_file=glob.glob(curdir+'\\*')

    try:
        i=0
        for fl in source_file:
            for sl in fls:
                if sl in fl:
                    if 'GANG' in fl:
                        if fl in sftp_filelist:
                            continue
                            sftp_filelist.append(fl.split('\\')[-1])
                            print(sl,'<----',fl)
                            text_smd_file+=sl+'<----'+fl.split('\\')[-1]+'\n'
                            i+=1 

                    if 'EFS' in fl:
                        if fl in sftp_filelist:
                            continue
                        else:
                            sftp_filelist.append(fl.split('\\')[-1])
                            print(sl,'<----',fl)
                            text_smd_file+=sl+'<----'+fl.split('\\')[-1]+'\n'
                            i+=1
                    if model in fl:
                        if 'user' in fl:
                            sftp_filelist.append(fl.split('\\')[-1])
                            print(sl,'<----',fl)
                            text_smd_file+=sl+'<----'+fl.split('\\')[-1]+'\n'
                            i+=1

                        if 'CP' in fl:
                            if fl in sftp_filelist:
                                continue
                            sftp_filelist.append(fl.split('\\')[-1])
                            print(sl,'<----',fl)
                            text_smd_file+=sl+'<----'+fl.split('\\')[-1]+'\n'
                            i+=1                        
                        if 'MODEM' in fl:
                            if fl in sftp_filelist:
                                continue 
                            sftp_filelist.append(fl.split('\\')[-1])
                            print(sl,'<----',fl)
                            text_smd_file+=sl+'<----'+fl.split('\\')[-1]+'\n'
                            i+=1
                        
                    if '.pit' in fl:
                        if fl in sftp_filelist:
                            continue
                        else:
                            sftp_filelist.append(fl.split('\\')[-1])
                            print(sl,'<----',fl)
                            text_smd_file+=sl+'<----'+fl.split('\\')[-1]+'\n'
                            i+=1
                        
            if '.sh' in fl:
                sh_name+=fl
                text_smd_file+='SH file: <---- '+fl.split('\\')[-1]
        ctn=len(fls)+1
        print(len(fls),ctn,i)
        if ctn!=i:
            print(len(fls),ctn,i)
            text_smd_file+='\n\nCHECK FILES QUANTITY!!!'

    except ValueError:
        text_smd_file+='Check SMD files!Can not find files!\n'+ValueError
        pass
    print(text_smd_file)
    return sftp_filelist,home_tar_filelist,sh_name,text_smd_file



def ver_name(model,curdir):
    try:
        files=scanner(model,curdir)
        ver_m=''
        for f in files[0]:
            print f
            if model in f:
                #for pda
                for x in f.split('_'):
                    if 'AP' in f:
                        if model in x:
                            ver_p=x
                            if 'T210' in x:
                                ver_m=x
                            print ver_p
                    if 'CODE' in f:
                        if model in x:
                            ver_p=x
                            print ver_p
                    if 'PLATFORM' in f:
                        if model in x:
                            ver_p=x
                            print ver_p
                #for csc
                    if 'CSC' in f:
                        if model in x:
                            ver_c=x
                            print ver_c
                    if 'csc' in f:
                        if model in x:
                            ver_c=x
                            print ver_c
                #for Modem
                    if 'CP' in f:
                        if model in x:
                            ver_m=x
                            print ver_m
                    if 'MODEM' in f:
                        if model in x:
                            ver_m=x
                            print ver_m
        if len(ver_m)<2:
            ver_n=ver_p+'_'+ver_c
        else:
            ver_n=ver_p+'_'+ver_c+'_'+ver_m
        return ver_n
    except:
        print 'Version name error'
        pass
      
