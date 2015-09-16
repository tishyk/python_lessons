# -*- coding: utf-8 -*-
from Tkinter import*
from tkFileDialog import*
from tkMessageBox import*
from PIL import Image, ImageTk
import ttk,os,io
import get_info,gms_search,availability_search
encodings=('utf-16-le','utf-8','utf-16','utf-16-be','cp1251','cp1252','cp1255')

root=Tk()
root.minsize(610,195)
root.title('GMS Application checker 2.0')
#root.maxsize(635,465)
win=Toplevel(root)
win.state('withdrawn')

fgtext='darkblue'
bgcolor='#f8faf3'
bgcolor='white'

CSC_verification_boot='adb shell am start -a android.intent.action.BOOT_COMPLETED -n com.samsung.sec.android.application.csc/.CscVerifierActivity'
CSC_verification_main='adb shell am start -a android.intent.action.MAIN -n  com.samsung.sec.android.application.csc/.CscVerifierActivity'
result_com=[] ; result_packages = [] ; result_df = [] ; result_app_phone = []
Configurations={} ; Configuration_text='' ; Configurations['df_addittion']='1'
Checkbox_values={} #collect checkbox values()

mask = [("Text files","*.txt")]
#,         ("HTML files","*.htm"),        ("All files","*.*")
#--- menu defs ---

def open_w():
    path=askopenfilename(filetypes=[("Text files","*.txt")])

def rdc():
    info_text()
    if linfo["text"]=='Connected !!!':
        resbtn["width"]=24
    print('rdc done !', info[0])
    
def file_save():
    global fout
    try:
        """get a filename and save the text in the editor widget"""
        # default extension is optional, here will add .txt if missing
        fout = asksaveasfile(mode='w', defaultextension=".html")
        
        fout.write('<pre><h3>Adb Commands result:</h3>\n')
        html_save(result_com)
        fout.write('<h3>Adb DF result:</h3>\n')
        html_save(result_df)
        fout.write('<h3>Adb Packages compare:</h3>\n')
        html_save(result_packages)
        fout.write('<h3>All Device Packages:</h3>\n')
        html_save(result_app_phone)
        fout.close()
    except:
        print "Save error"
def html_save(result):
    global fout
    for line in result:
        fout.write(line.rstrip()+'\n')
    fout.write('\n\n')
    
def save_conf():
    global Configuration_text
    values()
    Configurations.update(Checkbox_values)
    for keys in Configurations:
        Configuration_text+=str(keys)+' = '+str(Configurations[keys])+'\n'
    os.remove('Config.ini')
    open('Config.ini','w').write(Configuration_text)
    print 'Data Saved!'
    
#----- menu CSC Verification  def---
def call_csc_verification(command):
    try:
        answer=get_info.boot(command)
        if answer==0:
            showerror("Device connection error!","Check device connection!")
        if 60<answer<176:
            showinfo("Device connection started!","Verificatiot  Started !\n Check Device!")
        if 177<answer<305:
            showinfo("Device connection started!","Check your device for the next step!!!")          
    except:
        showerror("Programm error!","Check device connection!")

def BOOT():
    call_csc_verification(CSC_verification_main)

def MAIN():
    call_csc_verification(CSC_verification_main)
       
#----- menu View  def---
    
def short_view_gms():
    fr2.forget()
    l1.grid(row=1,column=1,columnspan=3,sticky=W,pady=2)
    l2.grid(row=2,column=1,columnspan=3,sticky=W,pady=2)
    l3.grid(row=3,column=1,columnspan=3,sticky=W,pady=2)
    l4.grid(row=1,rowspan=3,column=5,columnspan=2,sticky=W, padx=5,pady=2)
    Configurations['View']='short_view_gms'
    
def short_view_adb():
    l1.grid_forget()
    l2.grid_forget()
    l3.grid_forget()
    l4.grid_forget()
    fr2.pack(side='bottom',expand=1,fill='both',anchor=E)
    Configurations['View']='short_view_adb'
    
def full_view():
    l1.grid(row=1,column=1,columnspan=3,sticky=W,pady=2)
    l2.grid(row=2,column=1,columnspan=3,sticky=W,pady=2)
    l3.grid(row=3,column=1,columnspan=3,sticky=W,pady=2)
    l4.grid(row=1,rowspan=3,column=5,columnspan=2,sticky=W, padx=5,pady=2)
    fr2.pack(side='bottom',expand=1,fill='both',anchor=E)
    Configurations['View']='full_view'

def df_add():
    try:
        if Configurations['df_addittion']=='1':
            Configurations['df_addittion']='0'
            showinfo("Adb shell!","' Adb shell df '  Turned OFF !!!")
        else:
            Configurations['df_addittion']='1'
            showinfo("Adb shell!","'Command adb shell  df ' answer will be attached to report!")# make one if else after config file!!!!
    except:
        pass
    
#--- main device info def ---Check All


def values():# gathering checkbox values for results when we need them
    Checkbox_values["df_addittion"] = Configurations['df_addittion']
    Checkbox_values["all_device_packages"] = all_device_packages.get()
    Checkbox_values["show_phone_package"] = show_phone_package.get()
    
    #Checkbox_values["Check All"] = show_all.get()
    Checkbox_values["ro_build_type"] = ro_build_type.get()
    Checkbox_values["ro_product_model"] = ro_product_model.get()
    Checkbox_values["ro_product_name"] = ro_product_name.get()
    Checkbox_values["ro_bootloader"] = ro_bootloader.get()
    Checkbox_values["ro_build_PDA"] = ro_build_PDA.get()
    Checkbox_values["ril_official_cscver"] = ril_official_cscver.get()
    Checkbox_values["gsm_version_baseband"] = gsm_version_baseband.get()
    Checkbox_values["ro_csc_sales_code"] = ro_csc_sales_code.get()
    Checkbox_values["ro_csc_countryiso_code"] = ro_csc_countryiso_code.get()
    Checkbox_values["ro_csc_country_code"] = ro_csc_country_code.get()
    Checkbox_values["ro_product_ship"] = ro_product_ship.get()
    Checkbox_values["ro_build_changelist"] = ro_build_changelist.get()
    Checkbox_values["ro_build_version_release"] = ro_build_version_release.get()
    Checkbox_values["ro_com_google_gmsversion"] = ro_com_google_gmsversion.get()
    Checkbox_values["ro_build_fingerprint"] = ro_build_fingerprint.get()
    Checkbox_values["ro_build_date"] = ro_build_date.get()
    Checkbox_values["ril_hw_ver"] = ril_hw_ver.get()
    Checkbox_values["ril_ecclist0"] = ril_ecclist0.get()
    Checkbox_values["ril_ecclist"] = ril_ecclist.get()
    Checkbox_values["ril_serialnumber"] = ril_serialnumber.get()
    Checkbox_values["gsm_operator_numeric"] = gsm_operator_numeric.get()
    Checkbox_values["ro_boot_hardware"] = ro_boot_hardware.get()
    Checkbox_values["gsm_sim_state"] = gsm_sim_state.get()

# --- set ALL to check ---
def check_all(event):
    if show_all.get()==0:
        state=1
    if show_all.get()==1:
        state=0
    ro_build_type.set(state)
    ro_product_model.set(state)
    ro_product_name.set(state)
    ro_bootloader.set(state)
    ro_build_PDA.set(state)
    ril_official_cscver.set(state)
    gsm_version_baseband.set(state)
    ro_csc_sales_code.set(state)
    ro_csc_countryiso_code.set(state)
    ro_csc_country_code.set(state)
    ro_product_ship.set(state)
    ro_build_changelist.set(state)
    ro_build_version_release.set(state)
    ro_com_google_gmsversion.set(state)
    ro_build_fingerprint.set(state)
    ro_build_date.set(state)
    ril_hw_ver.set(state)
    ril_ecclist0.set(state)
    ril_ecclist.set(state)
    ril_serialnumber.set(state)
    gsm_operator_numeric.set(state)
    ro_boot_hardware.set(state)
    gsm_sim_state.set(state)


   
def info_text():
    global info, customer,l22
    info=get_info.info()
    customer=info[2]
    if info[0]!='  --//--': #get this item from get_info.py
        linfo["text"]='Connected !!!'
        l22.grid(row=1,column=2,columnspan=1,sticky=W,padx=4,pady=2)
    else:
        linfo["text"]=' Not Connected  !!!'
    lmv["text"]=info[0]+'\n'+info[1]
    lcc["text"]=info[2]+'\n  --//--'
    global ltemp,logo
    if info[0]=='  --//--':
        logo.grid_forget()
        ltemp["text"]=''
        resbtn["text"]=' Restart Connection '
        resbtn["width"]=28
        resbtn["fg"]=fgtext
        resbtn["bd"]=2
        resbtn.grid(row=1,column=6,columnspan=2,sticky=E, padx=3,pady=0)#--- restart btn
        l22.grid(row=1,column=2,columnspan=1,sticky=W,padx=17,pady=2)#--- width 2-d row on frame2
    else:
        resbtn.grid_forget()
        ltemp["text"]='         '
        logo.grid(row=1,column=6,columnspan=2,padx=4,pady=2,sticky=E)
    ltemp.grid(row=1,column=5,padx=3,pady=2,sticky=E)
    
def get_country(path):
    try:
        global country # [lists: aplications,aplications_value,mandatory_value]
        country='None'
        
        for en in encodings:
            try:
                if 'a' in io.open(path, 'r', encoding = en).read():
                    e=en ;print e ; break
            except:
                pass
        for line in io.open(path, 'r', encoding = e).readlines():
            if customer in line:
                country=line.split(':')[0]
                break
        if country!='None':
            Configurations['csc_btn_path']=path
            #print Configurations['csc_btn_path']
            state3s["image"]=img2
            lcc["text"]=customer+'\n'+country
            ent3.insert(0,path.split('/')[-1])
        else:
            lcc["text"]=customer+'\n  --//--'
            state3s["image"]=img3 ; country=''
            ent3.insert(0,'Country not found!')
    except:
        state3s["image"]=img3 ; country=''
        ent3.insert(0,'Country not found!')

#--- events def---

def resbtn_event(event):
    info_text()
    print('restarted', info[0])

def gms_btn(event):
    path=askopenfilename(filetypes=mask)
    path=path.replace('u','')
    global gms # {'GMS APKs':[],'Packages':[],'App':[],'Revision':[],'Description':[]}
    ent1.delete(0,END)
    try:
        gms=gms_search.get_gms(path)
        if len(gms['GMS APKs'])>0:
            state1s["image"]=img2
            ent1.insert(0,path.split('/')[-1])
    except:
        state1s["image"]=img3 ; gms=''
        ent1.insert(0,'Packages not found!')
        
def availability_btn(event):
    path=askopenfilename(filetypes=mask)
    global availability # [lists: aplications,aplications_value,mandatory_value]
    ent2.delete(0,END)
    try:
        availability=availability_search.availability(country,path)
        if len(availability[0])>10:
            state2s["image"]=img2
            ent2.insert(0,path.split('/')[-1])
    except:
        state2s["image"]=img3 ; availability=''
        ent2.insert(0,'Applications not found!')

def csc_btn(event):
    
    ent3.delete(0,END)
    path=askopenfilename(filetypes=mask)
    get_country(path)

def analize(event):
    del result_com[0:] ;del result_packages[0:] ;del result_df[0:] ; result_app_phone[0:]
    global win
    win.destroy()
    win=Toplevel(root)
    #win.minsize(540,300)
    win.title("Adb shell results")
    win.resizable(True,True)
    note = ttk.Notebook(win)
    note.pack(fill='both',expand=1)
    
    values()
    row_index=2
    if len(Comm_list)>0:
        note_adb = ttk.Frame(win)
        note.add(note_adb, text ='Adb commands')
        frame_note1=Frame(note_adb,bg=bgcolor)
        try:
            for command in Comm_list:
                for key in Checkbox_values:
                    if command.replace('_','.')==key.replace('_','.'):
                        if Checkbox_values[key]==1:
                            print command
                            
                            command_answer=os.popen('adb shell getprop '+command).readlines()[0]
                            Label(frame_note1, text='adb shell getprop '+command.upper()+' : ',bg=bgcolor, fg=fgtext).grid(sticky=E, row=row_index,column=1,padx=5,pady=3)
                            Label(frame_note1, text=command_answer.rstrip()+'    ',bg=bgcolor, fg=fgtext).grid(sticky=W, row=row_index,column=2,padx=5,pady=5)
                            result_com.append(command + ' : ' + command_answer.rstrip())
                            row_index+=1
                            

        except:
            showerror('Command error!!!',"Command can't read answer from Device\ !!!")
        frame_note1.pack(fill='both',expand=1)
    if Configurations['df_addittion']=='1':
        note_df=ttk.Frame(win)
        note.add(note_df, text ='Adb Shell df')
        text_df=Text(note_df, font=('times',10))
        for line in os.popen('adb shell df').readlines():
            text_df.insert(END,line.replace(' ','  '))
            text_df.insert(END,'- '*45+'\n')
            result_df.append(line)
        text_df.pack(expand=1,fill='both')
   
    if show_phone_package.get()==1 : # gms = {'GMS APKs':[],'Packages':[],'App':[],'Revision':[],'Description':[]}

        try:
            note_gms = ttk.Frame(win)
            note.add(note_gms, text ='GMS Packages')
            frame_note2=Frame(note_gms,bg=bgcolor)
            row_index=2

            for (package,apks,app,gms_revision,gms_description) in zip(gms["Packages"],gms["GMS APKs"],gms["App"],gms["Revision"],gms["Description"]):
                command='adb shell dumpsys package '+package+' | findstr -r  -i  "codePath=  versionName="'
                #print command,'---//---',apks
                try:
                    try:
                        command_answer=os.popen(command).readlines()[1]#read versions only "versionName=3.1.59 (736673-30)"
                    except:
                        command_answer='   None'
                        print 'none for -',package

                    if gms_revision not in command_answer:
                        Label(frame_note2, text=gms_revision,bg=bgcolor, fg='red').grid(sticky=W, row=row_index,column=4,padx=5,pady=2)
                        Label(frame_note2, text=apks,bg=bgcolor, fg=fgtext).grid(sticky=W, row=row_index,column=1,padx=5,pady=2)
                        Label(frame_note2, text=package,bg=bgcolor, fg=fgtext).grid(sticky=W, row=row_index,column=2,padx=5,pady=2)
                        Label(frame_note2, text=app,bg=bgcolor, fg=fgtext).grid(sticky=W, row=row_index,column=3,padx=5,pady=2)
                        try:
                            answer=(command_answer.replace('versionName=','')).rstrip()
                        except:
                            print "replace versionName failed "
                        if command_answer!='   None':
                            Label(frame_note2, text=answer,bg=bgcolor, fg='red').grid(sticky=W, row=row_index,column=5,padx=5,pady=2)
                        else:
                            Label(frame_note2, text=answer,bg=bgcolor, fg=fgtext).grid(sticky=W, row=row_index,column=5,padx=5,pady=2)
                        try:
                            if app in availability[0] : # [lists: aplications,aplications_value,mandatory_value]
                                print app, 'found in availability'
                                ind=availability[0].index(app)
                                Label(frame_note2, text=availability[2][ind],bg=bgcolor, fg=fgtext).grid(sticky=W, row=row_index,column=6,padx=5,pady=2)
                                Label(frame_note2, text=availability[1][ind],bg=bgcolor, fg=fgtext).grid(sticky=W, row=row_index,column=7,padx=5,pady=2)
                        except:
                            showerror('Command error!!!',"No Availability file \n or wrong data!!!")
                        result_packages.append( apks+'\t'+package+'\t'+app+'\t'+gms_revision+'\t'+answer)
                        row_index+=1
                
                except:
                    print 'error'
            frame_note2.pack(fill='both',expand=1)
        except:
            showerror('Package error!!!',"GMS packages not found!!!")
        print row_index
        
    if all_device_packages.get()==1:
        note_devpack=ttk.Frame(win)
        note.add(note_devpack, text ='Device Packages (All)')
        text=Text(note_devpack) ; scr=Scrollbar(note_devpack)
        
        text.configure(yscrollcommand=scr.set)
        scr.config(command=text.yview)
        all_phone_res = os.popen('adb shell dumpsys package 0 | findstr -r  -i  "codePath=  versionName="').read()
        text.insert(END,all_phone_res)
        text.config(font=('times',10))
        text.pack(side='left',expand=1,fill='both')
        scr.pack(side='right',fill='y')
        for app_phone_line in all_phone_res.split('codePath=/'):
            if len(app_phone_line)>10:
                result_app_phone.append(app_phone_line)
        
#showerror('head','body')        
#----- add menu
m=Menu(root, tearoff=0)
root.config(menu=m)
fm=Menu(m)
hm=Menu(m)
cm=Menu(m)
vm=Menu(m)
m.add_cascade(label='File',menu=fm)
m.add_cascade(label='CSC Verifications',menu=cm)
m.add_cascade(label='View',menu=vm)
m.add_cascade(label='Help',menu=hm)
#----- menu File ---
fm.add_command(label='Restart device connection',command=rdc)
fm.add_command(label='Save Configuration',command=save_conf)
fm.add_command(label='Save to file..',command=file_save)
#fm.add_cascade(label="Save to HTML",command='')
#fm.add_command(label='Exit',command='')
#----- menu Configuration ---
cm.add_command(label='CSC Verification 1 (BOOT)',command=BOOT)
cm.add_command(label='CSC Verification 2 (MAIN)',command=MAIN)

#----- menu View ---
vm.add_command(label='Short view (Adb command)',command=short_view_adb)
vm.add_command(label='Short view (GMS)',command=short_view_gms)
vm.add_command(label='Full view (Adb command + GMS)',command=full_view)
vm.add_command(label='Result ends with "adb shell df"',command=df_add)
#----- menu Help ---
hm.add_command(label='About',command='')
hm.add_command(label='Hot Keys',command='')
hm.add_command(label='Used colors',command='')
#----- image files ----
img1 = ImageTk.PhotoImage(Image.open("img/b-ya-widget__search.jpg"))#search button
img2 = ImageTk.PhotoImage(Image.open("img/b-ya-widget__down.jpg"))#indicator green
img3 = ImageTk.PhotoImage(Image.open("img/b-ya-widget__down-off1.jpg"))#indicator grey
img4=ImageTk.PhotoImage(Image.open("img/resbutton.png"))#refresh button
img5=ImageTk.PhotoImage(Image.open("img/Samsung_grey1.png"))#refresh button

fr1=Frame(root,bd=2)
fr2=Frame(root,bd=2)

#--- box for files choosing and device info (Labelframe)---

l1=LabelFrame(fr1, padx=5, pady=3)
l2=LabelFrame(fr1, padx=5, pady=3)
l3=LabelFrame(fr1, padx=5, pady=3)
l4=LabelFrame(fr1, padx=5, pady=3)#--- device info block Labelframe
l5=LabelFrame(fr1, padx=5, pady=3)#--- analyzing button block Labelframe
    
l1.grid(row=1,column=1,columnspan=3,sticky=W,pady=2)
l2.grid(row=2,column=1,columnspan=3,sticky=W,pady=2)
l3.grid(row=3,column=1,columnspan=3,sticky=W,pady=2)
l4.grid(row=1,rowspan=3,column=5,columnspan=2,sticky=W, padx=5,pady=2)#--- device info
l5.grid(row=4,column=1,columnspan=6,sticky=W, padx=1,pady=2)#--- frame for analizy button
# dinamic text
resbtn=Button(l5)
ltemp=Label(l5)
logo=Label(l5,image=img5)
#--- File name Label (1)-> Search Button (2) -> Entry(file name) (3) -> State Button (4)

Label(l1,text='GMS apps Package ',fg=fgtext).grid(row=1,column=1,padx=5,pady=2)
Label(l2,text='Geo Availability       ',fg=fgtext).grid(row=2,column=1,padx=5,pady=2)
Label(l3,text='CSC Customer List  ',fg=fgtext).grid(row=3,column=1,padx=5,pady=2)
# --->Search Button (2)
sbtn1=Button(l1,image=img1) ; sbtn2=Button(l2,image=img1) ; sbtn3=Button(l3,image=img1)
sbtn1.grid(row=1,column=2,padx=5,pady=0,sticky=W)
sbtn2.grid(row=2,column=2,padx=5,pady=0,sticky=W)
sbtn3.grid(row=3,column=2,padx=5,pady=0,sticky=W)
#--->Entry(file name) (3)
ent1=Entry(l1,width=30,bd=3); ent2=Entry(l2,width=30,bd=3); ent3=Entry(l3,width=30,bd=3)
ent1.grid(row=1,column=3,padx=5,pady=2)
ent2.grid(row=2,column=3,padx=5,pady=2)
ent3.grid(row=3,column=3,padx=5,pady=2)
#--->State Button (4)
state1s=Label(l1,image=img3); state1s.grid(row=1,column=4,padx=3,pady=0)
state2s=Label(l2,image=img3); state2s.grid(row=2,column=4,padx=3,pady=0)
state3s=Label(l3,image=img3); state3s.grid(row=3,column=4,padx=3,pady=0)
#---end block ---

#--- Device info block--- row 1-3 col 5-6
Label(l4,text='    Device info:',fg=fgtext).grid(row=1,column=5,padx=3,pady=2,sticky=W)#1 str
Label(l4,text='Model:       \n    Android Ver.: ',fg=fgtext).grid(row=2,column=5,padx=3,pady=3,sticky=W)#2,3 str
Label(l4,text='    Customer: \nCountry:',fg=fgtext).grid(row=3,column=5,padx=3,pady=3,sticky=W)#4,5 str

linfo=Label(l4,text=' Not Connected !!! ',fg=fgtext)
lmv=Label(l4,fg=fgtext)
lcc=Label(l4,fg=fgtext)
linfo.grid(row=1,column=6,padx=3,pady=2,sticky=W)#info state
lmv.grid(row=2,column=6,padx=3,pady=2,sticky=W)#model \n android version
lcc.grid(row=3,column=6,padx=3,pady=2,sticky=W)#customer and country


#--- Device Analizing button block--- row 4 col 1-6
abtn=Button(l5,text='Start Package Analizing',fg=fgtext,bd=2)
abtn.grid(row=1,column=1,padx=2,pady=2)

show_phone_package=IntVar()
show_phone_package_cbtn = Checkbutton(l5,text="GMS packages", fg=fgtext, variable=show_phone_package,onvalue=1,offvalue=0)
show_phone_package_cbtn.grid(row=1,column=2,padx=4,pady=2,sticky=W)

all_device_packages = IntVar()
all_packages = Checkbutton(l5, text="All device packages",fg=fgtext, variable=all_device_packages, onvalue=1, offvalue=0)
all_packages.grid(row=1,column=3,columnspan=1,padx=1,pady=2,sticky=W)

#--- frame 2 LabelFrames ---
#--- LabelFrames 1.2.3
l20=LabelFrame(fr2, padx=5, pady=3); l20.grid(row=1,rowspan=3,column=1,columnspan=3,sticky=W,padx=5,pady=2)
l21=LabelFrame(l20, padx=5, pady=3)
l22=LabelFrame(l20, padx=5, pady=3)
l23=LabelFrame(l20, padx=5, pady=3)
l21.grid(row=1,column=1,columnspan=1,sticky=W,padx=5,pady=2)
l22.grid(row=1,column=2,columnspan=1,sticky=W,padx=17,pady=2)
l23.grid(row=1,column=3,columnspan=1,sticky=W,padx=5,pady=2)



#--- frame2 elements ---
show_all=IntVar()
show_all_cbtn = Checkbutton(l21,text=" Check All                             ", fg=fgtext, variable=show_all,onvalue=1,offvalue=0)
show_all_cbtn.grid(row=1,column=1,padx=2,pady=2,sticky=W)
#--- vars for command checkbox
#--- 1-st column ---
ro_build_type=IntVar() ; ro_product_model=IntVar() ; ro_product_name=IntVar() ; ro_bootloader=IntVar()
ro_build_PDA=IntVar() ; ril_official_cscver=IntVar() ; gsm_version_baseband=IntVar()
#--- 2-nd column ---
ro_csc_sales_code=IntVar() ; ro_csc_countryiso_code=IntVar() ; ro_csc_country_code=IntVar() ; ro_product_ship=IntVar()
ro_build_changelist=IntVar() ; ro_build_version_release=IntVar() ; ro_com_google_gmsversion=IntVar() ; ro_build_fingerprint=IntVar()
#--- 3-d column ---
ro_build_date=IntVar() ; ril_hw_ver=IntVar() ; ril_ecclist0=IntVar() ; ril_ecclist=IntVar()
ril_serialnumber=IntVar() ; gsm_operator_numeric=IntVar() ; ro_boot_hardware=IntVar() ; gsm_sim_state=IntVar()

#--- obj for command checkbox command_cbtn
#--- 1-st column ---
ro_build_type_cbtn = Checkbutton(l21,text="[ro.build.type]",fg=fgtext, variable=ro_build_type,onvalue=1,offvalue=0)
ro_product_model_cbtn = Checkbutton(l21,text="[ro.product.model]",fg=fgtext, variable=ro_product_model,onvalue=1,offvalue=0)
ro_product_name_cbtn = Checkbutton(l21,text="[ro.product.name]",fg=fgtext, variable=ro_product_name,onvalue=1,offvalue=0)
ro_bootloader_cbtn = Checkbutton(l21,text="[ro.bootloader]",fg=fgtext, variable=ro_bootloader,onvalue=1,offvalue=0)
ro_build_PDA_cbtn = Checkbutton(l21,text="[ro.build.PDA]",fg=fgtext, variable=ro_build_PDA,onvalue=1,offvalue=0)
ril_official_cscver_cbtn = Checkbutton(l21,text="[ril.official_cscver]",fg=fgtext, variable=ril_official_cscver,onvalue=1,offvalue=0)
gsm_version_baseband_cbtn = Checkbutton(l21,text="[gsm.version.baseband]",fg=fgtext, variable=gsm_version_baseband,onvalue=1,offvalue=0)
#--- 2-nd column ---
ro_csc_sales_code_cbtn = Checkbutton(l22,text="[ro.csc.sales_code]",fg=fgtext, variable=ro_csc_sales_code,onvalue=1,offvalue=0)
ro_csc_countryiso_code_cbtn = Checkbutton(l22,text="[ro.csc.countryiso_code]",fg=fgtext, variable=ro_csc_countryiso_code,onvalue=1,offvalue=0)
ro_csc_country_code_cbtn = Checkbutton(l22,text="[ro.csc.country_code]",fg=fgtext, variable=ro_csc_country_code,onvalue=1,offvalue=0)
ro_product_ship_cbtn = Checkbutton(l22,text="[ro.product_ship]",fg=fgtext, variable=ro_product_ship,onvalue=1,offvalue=0)
ro_build_changelist_cbtn = Checkbutton(l22,text="[ro.build.changelist]",fg=fgtext, variable=ro_build_changelist,onvalue=1,offvalue=0)
ro_build_version_release_cbtn = Checkbutton(l22,text="[ro.build.version.release]",fg=fgtext, variable=ro_build_version_release,onvalue=1,offvalue=0)
ro_com_google_gmsversion_cbtn = Checkbutton(l22,text="[ro.com.google.gmsversion]",fg=fgtext, variable=ro_com_google_gmsversion,onvalue=1,offvalue=0)
ro_build_fingerprint_cbtn = Checkbutton(l22,text="[ro.build.fingerprint]",fg=fgtext, variable=ro_build_fingerprint,onvalue=1,offvalue=0)
#--- 3-d column ---
ro_build_date_cbtn = Checkbutton(l23,text="[ro.build.date]",fg=fgtext, variable=ro_build_date,onvalue=1,offvalue=0)
ril_hw_ver_cbtn = Checkbutton(l23,text="[ril.hw_ver]",fg=fgtext, variable=ril_hw_ver,onvalue=1,offvalue=0)
ril_ecclist0_cbtn = Checkbutton(l23,text="[ril.ecclist0]",fg=fgtext, variable=ril_ecclist0,onvalue=1,offvalue=0)
ril_ecclist_cbtn = Checkbutton(l23,text="[ril.ecclist]",fg=fgtext, variable=ril_ecclist,onvalue=1,offvalue=0)
ril_serialnumber_cbtn = Checkbutton(l23,text="[ril.serialnumber]",fg=fgtext, variable=ril_serialnumber,onvalue=1,offvalue=0)
gsm_operator_numeric_cbtn = Checkbutton(l23,text="[gsm.operator.numeric]",fg=fgtext, variable=gsm_operator_numeric,onvalue=1,offvalue=0)
ro_boot_hardware_cbtn = Checkbutton(l23,text="[ro.boot.hardware]",fg=fgtext, variable=ro_boot_hardware,onvalue=1,offvalue=0)
gsm_sim_state_cbtn = Checkbutton(l23,text="[gsm.sim.state]",fg=fgtext, variable=gsm_sim_state,onvalue=1,offvalue=0)
#--- grid for chbtn obj ----
#--- 1-st column ----
ro_build_type_cbtn.grid(row=2,column=1,padx=2,pady=2,sticky=W);ro_product_model_cbtn.grid(row=3,column=1,padx=2,pady=2,sticky=W)
ro_product_name_cbtn.grid(row=4,column=1,padx=2,pady=2,sticky=W);ro_bootloader_cbtn.grid(row=5,column=1,padx=2,pady=2,sticky=W)
ro_build_PDA_cbtn.grid(row=6,column=1,padx=2,pady=2,sticky=W);ril_official_cscver_cbtn.grid(row=7,column=1,padx=2,pady=2,sticky=W)
gsm_version_baseband_cbtn.grid(row=8,column=1,padx=2,pady=2,sticky=W)
#--- 2-nd column ---
ro_csc_sales_code_cbtn.grid(row=1,column=2,padx=2,pady=2,sticky=W) ; ro_csc_countryiso_code_cbtn.grid(row=2,column=2,padx=2,pady=2,sticky=W)
ro_csc_country_code_cbtn.grid(row=3,column=2,padx=2,pady=2,sticky=W) ; ro_product_ship_cbtn.grid(row=4,column=2,padx=2,pady=2,sticky=W)
ro_build_changelist_cbtn.grid(row=5,column=2,padx=2,pady=2,sticky=W) ; ro_build_version_release_cbtn.grid(row=6,column=2,padx=2,pady=2,sticky=W)
ro_com_google_gmsversion_cbtn.grid(row=7,column=2,padx=2,pady=2,sticky=W) ; ro_build_fingerprint_cbtn.grid(row=8,column=2,padx=2,pady=2,sticky=W)
#--- 3-d column ---
ro_build_date_cbtn.grid(row=1,column=2,padx=2,pady=2,sticky=W)
ril_hw_ver_cbtn.grid(row=2,column=2,padx=2,pady=2,sticky=W)
ril_ecclist0_cbtn.grid(row=3,column=2,padx=2,pady=2,sticky=W)
ril_ecclist_cbtn.grid(row=4,column=2,padx=2,pady=2,sticky=W)
ril_serialnumber_cbtn.grid(row=5,column=2,padx=2,pady=2,sticky=W)
gsm_operator_numeric_cbtn.grid(row=6,column=2,padx=2,pady=2,sticky=W)
ro_boot_hardware_cbtn.grid(row=7,column=2,padx=2,pady=2,sticky=W)
gsm_sim_state_cbtn.grid(row=8,column=2,padx=2,pady=2,sticky=W)


#--- bindings ---
abtn.bind("<Button-1>",analize)
resbtn.bind("<Button-1>",resbtn_event)
sbtn1.bind("<Button-1>",gms_btn)
sbtn2.bind("<Button-1>",availability_btn)
sbtn3.bind("<Button-1>",csc_btn)
show_all_cbtn.bind("<Button-1>",check_all)

fr1.pack(side='top',padx=5,pady=5,expand=0,fill='x',anchor=N)
fr2.pack(side='bottom',expand=1,fill='both',anchor=E)

#--- Get values for info text ---
info_text()   #from def
print(info[0])
#--- end Device info block---

#config_file=open('Config.ini','a')
for line in open('Config.ini').readlines():
    try:
        #view check
        if line.rstrip()=='View = short_view_gms':
            short_view_gms()
        if line.rstrip()=='View = short_view_adb':
            short_view_adb()
        if line.rstrip()=='View = full_view':
            full_view()
        #btns path
        if 'csc_btn_path = ' in line:
            path=(line.split('csc_btn_path = ')[1]).rstrip()
            print path
            get_country(path)
        if 'df_addittion = 1' in line:
            Configurations['df_addittion']='1'
        #checkbox check
        if line.rstrip()=="ro_build_changelist = 1":
            ro_build_changelist.set(1)
        if line.rstrip()=="gsm_operator_numeric = 1":
            gsm_operator_numeric.set(1)
        if line.rstrip()=="ro_build_type = 1":
            ro_build_type.set(1)
        if line.rstrip()=="ro_build_fingerprint = 1":
            ro_build_fingerprint.set(1)
        if line.rstrip()=="ro_product_name = 1":
            ro_product_name.set(1)
        if line.rstrip()=="ro_product_model = 1":
            ro_product_model.set(1)
        if line.rstrip()=="ro_com_google_gmsversion = 1":
            ro_com_google_gmsversion.set(1)
        if line.rstrip()=="gsm_sim_state = 1":
            gsm_sim_state.set(1)
        if line.rstrip()=="gsm_version_baseband = 1":
            gsm_version_baseband.set(1)
        if line.rstrip()=="ro_build_date = 1":
            ro_build_date.set(1)
        if line.rstrip()=="ro_product_ship = 1":
            ro_product_ship.set(1)
        if line.rstrip()=="ril_ecclist = 1":
            ril_ecclist.set(1)
        if line.rstrip()=="show_phone_package = 1":
            show_phone_package.set(1)
        if line.rstrip()=="ro_bootloader = 1":
            ro_bootloader.set(1)
        if line.rstrip()=="ro_csc_sales_code = 1":
            ro_csc_sales_code.set(1)
        if line.rstrip()=="ril_ecclist0 = 1":
            ril_ecclist0.set(1)
        if line.rstrip()=="ro_build_version_release = 1":
            ro_build_version_release.set(1)
        if line.rstrip()=="ro_csc_country_code = 1":
            ro_csc_country_code.set(1)
        if line.rstrip()=="View = full_view":
            View = full_view.set(1)
        if line.rstrip()=="ril_hw_ver = 1":
            ril_hw_ver.set(1)
        if line.rstrip()=="ro_csc_countryiso_code = 1":
            ro_csc_countryiso_code.set(1)
        if line.rstrip()=="ro_build_PDA = 1":
            ro_build_PDA.set(1)
        if line.rstrip()=="ril_serialnumber = 1":
            ril_serialnumber.set(1)
        if line.rstrip()=="ril_official_cscver = 1":
            ril_official_cscver.set(1)
        if line.rstrip()=="ro_boot_hardware = 1":
            ro_boot_hardware.set(1)            
         
    except:
        pass

Comm_list=["ro.build.type","ro.product.model","ro.product.name","ro.bootloader","ro.build.PDA",
           "ril.official_cscver","gsm.version.baseband","ro.csc.sales_code","ro.csc.countryiso_code",
           "ro.csc.country_code","ro.product_ship","ro.build.changelist","ro.build.version.release",
           "ro.com.google.gmsversion","ro.build.fingerprint","ro.build.date","ril.hw_ver","ril.ecclist0",
           "ril.ecclist","ril.serialnumber","gsm.operator.numeric","ro.boot.hardware","gsm.sim.state"]

root.mainloop()
               
