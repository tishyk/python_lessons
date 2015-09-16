# -*- coding: cp1251 -*-
from Tkinter import*
#from scanner import*
from tkFileDialog import *

fpath=[]#add path to file here, clean by every call
num,err,tochka=[],[],[]#for scanner
possition=0
def path():
    try:
        path=askopenfilename()
        lb.delete(0, END)
        path=path.encode('cp1251')
        lb.insert(0,path.decode('cp1251').split('/')[-1])
        global fsave
        fsave=path.replace(path.decode('cp1251').split('/')[-1],'')
        print(fsave)
        if len(lb.get())>0:
            try:
                fpath.pop(0)
            except:
                pass
            bgen.config(state=NORMAL)
        else:
            bgen.config(state=DISABLED)
        return path
    except:
        lb.delete(0, END)
        lb.insert(0,'File for analizing not found!')
    
def scanner(path):
    try:
        try:
            f=open(path[0]).readlines()
        except:
            f='0'
        duplicated=0;lines_count=0
        global num,err,tochka,nums
        num,err,tochka=[],[],[] #clean data from previous scanning
        for line in f:
            lines_count+=1
            if len(line)>2:
                try:
                    num1=re.findall('\d{3}',line)[0]
                    num2=re.findall('\d{5}',line)[0]
                    num3=re.findall('\d{6}',line)[0]

                    if len(num2)==5 and num2 not in tochka:
                        tochka.append(num2)
                    elif len(num2)!=5:
                        print('Tochka len error in line: '+str(f.index(line))+' ---('+line.rstrip()+')--- not added!')
                        err.append(line)
                    if len(num1)==3 and len(num2)==5 and len(num3)==6:
                        x=str(num1+'-'+num2+'-'+num3)
                        mass=int(x[-4:-2])*10000+int(x[-6:-4])*100+int(x[-12:-7])*0.0001+int(x[:3])*0.000001
                        if [mass,x] not in num:
                            if (int(x[-2:]) not in range(13,15) or
                                int(x[-4:-2]) not in range(1,13) or
                                int(x[-6:-4]) not in range(1,32)):
                                err.append(line)
                                print('Date error in line: '+str(f.index(line))+' ---('+line.rstrip()+')--- not added!')
                            else:
                                num.append([mass,x])
                        else:
                            duplicated+=1
                    else:
                        err.append(line)
                        print('Date len error in line: '+str(f.index(line))+' ---('+line.rstrip()+')--- not added!')
                except:
                    err.append(line)
                    print('Error in line: '+str(f.index(line))+' ---('+line.rstrip()+')--- not added!')
            else:
    #            err.append(line)
                print('Empty line: '+str(f.index(line))+' ---('+line.rstrip()+')---  not added!')
        enterr.delete(0, END)
        if len(err)>0:
            enterr.insert(0,err[0])
            bn.config(state=NORMAL);br.config(state=NORMAL);bp.config(state=DISABLED)
        print(len(num),len(err),len(tochka))
        ls.config(text=' Lines recognised :  '+str(len(num))+'\tHave errors :  '+str(len(err))+'\tTotal :  '+str(len(num)+len(err))+' lines')
        for x in err:
            print x
        return num,err,tochka
    except:
        ls.config(text='scanner(path) module error!!!')
                  
def nex(event):
    try:
        global possition
        pos=err.index(enterr.get())
        if 0<=pos<(len(err)-1):
            bp.config(state=NORMAL)
            enterr.delete(0, END)
            enterr.insert(0,str(err[pos+1]))
            possition+=1
            if 0<=pos<=(len(err)-3):
                bn.config(state=NORMAL)      
            else:
               bn.config(state=DISABLED)
        elif pos<1:
            bp.config(state=DISABLED)
        print('current pos inserted:'+str(pos+1))
    except:
        ls.config(text=' next module error!!!')
        
def prev(event):
    try:
        global possition
        pos=err.index(enterr.get())
        if 0<pos<=(len(err)):
            bp.config(state=NORMAL)
            enterr.delete(0, END)
            enterr.insert(0,str(err[pos-1]))
            possition-=1
            if 0<=pos<=(len(err)-3):
                bn.config(state=NORMAL)      
            else:
               bn.config(state=NORMAL)
        elif pos<=0:
            bp.config(state=DISABLED)
        elif pos<=0:
            bp.config(state=DISABLED)
        print('err pos inserted:'+str(pos+1)) 
    except:
        ls.config(text=' prev module error!!!')
        
def repl(event):
    try:
        print(len(num))
        x=enterr.get().rstrip()
        x=x.replace(' ','')
        try:
            mass=int(x[-4:-2])*10000+int(x[-6:-4])*100+int(x[-12:-7])*0.0001+int(x[:3])*0.000001
            if [mass,enterr.get()] not in num:
                num.append([mass,enterr.get()])
        except:
            pass
        enterr.delete(0, END)
        enterr.insert(0,err[possition])
        print(len(num),possition)
        nex(event)
    except:
        ls.config(text=' repl module error!!!')
    
def defaults(event):
    try:
        entki.delete(0, END)
        entadm.delete(0, END)
        entki.insert(0,('Якимчук Н.М.').decode('cp1251'))
        entadm.insert(0,('Пшеннікова О.В.').decode('cp1251'))
    except:
        pass
def gen(event):
    num.sort()
    client=entki.get().encode('cp1251')
    manager=entadm.get().encode('cp1251')

    tochki=''
    for t in tochka:
        tochki+=t+', '
    print(tochki)
    
    try:
        file_s=(fsave+'Звіт_'.decode('cp1251')+client.decode('cp1251')+num[0][1].split('-')[2]+'-'+num[-1][1].split('-')[2]+'_'+str(len(num))+'.xls')
        print(file_s)
    except:
        file_s='0.txt'
        print ('gen some error')
    print(file_s)
    open(file_s,'a').write('Акт прийому-передачі договорів з ТП: '+tochki[:-2]+'\n\n№ п/п \t№ договору\tПІБ КІ\tПІБ ТМ\n')
    
    for n in num:
        if len(n[1])>6:
            open(file_s,'a').write(str(num.index(n)+1)+'\t  '+n[1].rstrip()+'\t  '+client+'\t  '+manager+'\n')

    open(file_s,'a').write('''
        \n\nПередав: \nПосада: КІ\t\t\t'''+client+'''\n
        <<____>>______________ 20__ року\n\n
        Прийняв: \nПосада: Адміністратор\t\t\t'''+manager+'''\n
        <<____>>______________ 20__ року\n\n''')
    ls.config(text='Report successfully created!!!')
    print('Report successfully created!!!')

def ev(event):
    if  len(fpath)>1:
        fpath.pop(0)
    else:
        fpath.append(path())
    scanner(fpath)

root=Tk()
root.title('Deltabank Report (by Tischenko S. ver.1.0)')

fr1=Frame(root,bd=2,height=5)
fr2=Frame(root,bd=2)
#frame1
lki=Label(fr1,text='C.I.:',height=2)
entki=Entry(fr1,width=25)
ladm=Label(fr1,text='Administrator:',)
entadm=Entry(fr1,width=25)
bf=Button(fr1,text='Choose file for analizing ',width=25)
lb=Entry(fr1,width=41)
bgen=Button(fr1,text='Generate\nreport',width=12,height=3,bd=3,state=DISABLED)

lki.grid(row=1,column=1,padx=5,pady=2,sticky=W)
entki.grid(row=1,column=2,pady=2,sticky=W)
ladm.grid(row=1,column=3,ipady=2,padx=5,pady=2,sticky=E)
entadm.grid(row=1,column=4,pady=2,sticky=W)
bgen.grid(row=1,column=5,rowspan=2,padx=5,sticky=E)
bf.grid(row=2,column=1,columnspan=2,padx=5)
lb.grid(row=2,column=3,columnspan=2,padx=5,sticky=W)
#frame 2
enterr=Entry(fr2,width=60,fg='darkblue')
bp=Button(fr2,text='<< Previous ',state=DISABLED)
br=Button(fr2,text='Replace ',state=DISABLED)
bn=Button(fr2,text='Next >>',state=DISABLED)

ls=Label(fr2,text='-'*34+'Error in lines (press "Replace" when fix it)'+'-'*34)
ls.grid(columnspan=5,padx=5,pady=2,sticky=S)
enterr.grid(row=1,column=1,padx=5,sticky=W)
bp.grid(row=1,column=2,padx=2,sticky=E)
br.grid(row=1,column=3,padx=2,sticky=E)
bn.grid(row=1,column=4,padx=2,sticky=E)

fr1.pack(side='top',padx=5,pady=5,expand=0,fill='both',anchor=N)
fr2.pack(side='bottom',expand=1,fill='both',anchor=W)


bf.bind("<Button-1>",ev)
bgen.bind("<Button-1>",gen)
root.bind("<Button-2>",defaults)
bp.bind("<Button-1>",prev)
br.bind("<Button-1>",repl)
bn.bind("<Button-1>",nex)

root.mainloop()






