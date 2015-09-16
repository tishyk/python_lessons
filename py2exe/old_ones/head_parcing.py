# -*- coding: utf-8 -*-

import re, time
p4={"CODE":{},"CSC":{},"MODEM":{},"LABEL":{"CODE":[],"CSC":[],"MODEM":[]}}
label_data={"activation":[]}

alphabet={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I', 10:'J',
          11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q', 18:'R',19:'S',
          20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}
alpha="a b c d e f g h i j k l m n o p q r s t u  v w x y z . @"

year=time.strftime("%y", time.localtime())
month=time.strftime("%m", time.localtime())
day=time.strftime("%d", time.localtime())
symbol_date=alphabet[int(year)]+alphabet[int(month)]+day
#print symbol_date

def fget_versions(info_text):

    for bin in ["Code Version","CSC Version","CP Version"]:
        for line in info_text.split("\n"):
            if bin in line:
                
                if "mapping" not in line :
                    
                    if bin=="Code Version": data_key="CODE"
                    if bin=="CSC Version" : data_key="CSC"
                    if bin=="CP Version"  : data_key="MODEM"
                    
                    if data_key not in p4["LABEL_MARK"]:
                        p4["LABEL_MARK"].append(data_key)
                        print data_key,p4["LABEL_MARK"]
                    
                #print line
                temp=line
                temp=temp.replace(bin,"")
                temp=temp.replace(" ","")
                temp=temp.replace("/","")
                temp=temp.replace("\t","")
                temp=temp.replace("mapping","")
                
                if bin=="Code Version":
                    code_version=temp
                    for separator in [",",";"," ",".","//","-"]:
                            
                        if len(code_version.split(separator))>1:
                            print code_version.split(separator)
                            p4["CODE"]["VERSION"]=code_version.split(separator)
                            break
                        else:    
                            p4["CODE"]["VERSION"]=[code_version]
                            break                    

                if bin=="CSC Version" :
                    csc_version=temp
                    for separator in [",",";"," ",".","//"]:
                            
                        if len(csc_version.split(separator))>1:
                            print csc_version.split(separator)
                            p4["CSC"]["VERSION"]=csc_version.split(separator)
                            break
                        else:    
                            p4["CSC"]["VERSION"]=[csc_version]
                            break
                if bin=="CP Version" :
                    cp_version=temp
                    for separator in [",",";"," ",".","//",'/']:
                            
                        if len(cp_version.split(separator))>1:
                            print cp_version.split(separator)
                            p4["MODEM"]["VERSION"]=cp_version.split(separator)
                            break
                        else:    
                            p4["MODEM"]["VERSION"]=[cp_version]
                            break
                break
    return code_version,csc_version,cp_version

def fversion_name_correction(model):
    for bin_type in ["CODE","CSC","MODEM"]:
        for values in p4[bin_type]["VERSION"]:
            if model[:-2] not in values and len(values)>1:
                p4[bin_type]["VERSION"].insert(p4[bin_type]["VERSION"].index(values),model+values)
                p4[bin_type]["VERSION"].remove(values)

def fmake_smd_name():
    p4["SMD_NAME"],p4["SMD_NAME_HOME"]=[],[]
    
    for code in p4["CODE"]["VERSION"]:
        for csc in p4["CSC"]["VERSION"]:
            for modem in p4["MODEM"]["VERSION"]:
                
                if len(modem)>3:
                    if len(code)>3:
                        p4["SMD_NAME"].append(code+"_"+csc+"_"+modem)
                        p4["SMD_NAME_HOME"].append(code+"_"+csc+"_"+modem+"_HOME")
                    else:
                        p4["SMD_NAME"].append(csc+"_"+modem)
                        p4["SMD_NAME_HOME"].append(csc+"_"+modem+"_HOME")
                else:
                    p4["SMD_NAME"].append(code+"_"+csc)
                    p4["SMD_NAME_HOME"].append(code+"_"+csc+"_HOME")


def fget_manager(info_text):
    temp=re.findall("Project Manager[\t].*[)]",info_text)[0]
    print temp
    manager_name_temp=temp[:-1].split("(")
    manager_name=manager_name_temp[0].replace("Project Manager\t","")
    print len(manager_name)
    if len(manager_name)<2:
        manager_name=temp[:-1].split("(")[1]
        manager_name=manager_name.replace(")","")
        #print temp+"- Get: "+manager_name
    return manager_name

def fget_approver(data):
    try:
        temp=re.findall("Approval User[\t].*[)]",data)[0]
        approver=temp[:-1].split("(")[1]
        user_name=temp[:-1].split("(")[0]
        user_name=user_name.replace("Approval User\t","")
        if len(user_name)<2:
            user_name=approver
        #print temp+"- Get: "+approver
    except:
        user_name,approver="-","-"
    return user_name,approver

def mail_list(mail_text):
    
    if "Recipients\t" in mail_text:
        mail_list=[]
        recipients=re.findall("Recipients[\t].*[\n]",mail_text)[0][11:-1]
        #print recipients
        for r in ["+","-",",", " ","@samsung.com","@samsung.co"]:
            recipients=recipients.replace(r,";")
        list_recipients=recipients.split(";")
        
        for r in list_recipients:
            if len(r)>3 and "@" not in r:
                for symbol in str(r):
                    if symbol.isupper()==False and (r+"@samsung.com") not in mail_list and symbol in alpha:
                        mail_list.append(r+"@samsung.com")
                        break
                    else:
                        break
        if len(mail_list)==0:
            try:
                mail_list.append(fget_approver(mail_text)[1]+"@samsung.com")
            except:
                mail_list.append("@samsung.com")
        mail_list.sort()
        return mail_list
    else:
        return ["id not found"]
    
def fget_project(data):
    temp=re.findall("Project\t.*[)]",data)[0]
    project=temp[:-1].split("(")[-1]
    print temp+"- Get: "+project
    return project

def fget_p4_path_port(info_text):
    if "Server" in info_text and "Path/Template" in info_text:
        if "AP/CSC" in info_text:
            temp=re.findall("AP/CSC.*[\n]Server.*[\n]Path/Template.*[\n]",info_text)[0]
            #'AP/CSC\t\nServer\t1716\nPath/Template\tTEMPLATE_D4_KLTE-EUR-OPEN-MR_REL\n'
            temp=temp.replace("\n",'').replace("AP/CSC",'')
            temp=temp.split("Path/Template")
            p4["CODE"]["Server"]=(temp[0].split(" ")[-1]).split("\t")[-1].rstrip()
            p4["CSC"]["Server"]=p4["CODE"]["Server"]
            p4["CODE"]["Path/Template"]=(temp[-1].split(" ")[-1]).split("\t")[-1].rstrip()
            p4["CSC"]["Path/Template"]=p4["CODE"]["Path/Template"]
            
        if "CP" in info_text:
            temp=re.findall("CP.*[\n]Server.*[\n]Path/Template.*[\n]",info_text)[0]
            temp=temp.replace("\n",'').replace("CP",'',1)
            temp=temp.split("Path/Template")
            p4["MODEM"]["Server"]=(temp[0].split(" ")[-1]).split("\t")[-1].rstrip()
            p4["MODEM"]["Path/Template"]=(temp[-1].split(" ")[-1]).split("\t")[-1].rstrip()   

def fget_full_partials(info_text):
    
    for cl_type in p4.keys():
        if cl_type=="SMD_NAME" or cl_type=="SMD_NAME_HOME" or cl_type=="LABEL" or cl_type=="LABEL_MARK":
            continue
        if cl_type=="CODE":
            find_type="AP"
        if cl_type=="CSC":
            find_type=cl_type            
        if cl_type=="MODEM":
            find_type="CP"
        if find_type in info_text and "Full" in info_text and "Partials" in info_text:
            temp=re.findall(find_type+"[\t][\n]Full.*[\n].*",info_text)[0]
            print temp
            temp=temp.replace("\n","")
            temp=temp.split("Partials")
            p4[cl_type]["Full"]=temp[0].split("\t")[-1]
            p4[cl_type]["Partials"]=temp[-1].split("\t")[-1]
            print "\n",p4[cl_type]["Full"],p4[cl_type]["Partials"]

def fget_label(info_text):
    if "Label" in info_text:
        temp=re.findall("Release Member .*[\n]Label.*",info_text)
        label=temp[0].split("\t")[-1]
        return label
    else:
        return ""


def fget_label_new(info_text,model):
    p4["LABEL"]={"CODE":[],"CSC":[],"MODEM":[]}
    for line in info_text.split("\n"):
        if "_OFFICIAL" in line and model in line:
            for separator in [",",";"," ",".","//","\t","Label"]:
                line=line.replace(separator,'') 
            for key in p4["LABEL"].keys():
                if key in line and line not in p4["LABEL"][key]:
                    p4["LABEL"][key].append(line)
                    print line  