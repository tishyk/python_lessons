# -*- coding: utf-8 -*-
import re

def get_fingerprint(data):
    fingerprint=""
    temp=re.findall('fingerprint=.*[\s"]', data)
    if len(temp)>0:
        temp=temp[0].replace('"',"")
        temp=temp.replace("'","")
        temp=temp.split(" ")[0]
        fingerprint=temp
        #print "case 1 ", temp
    if fingerprint=="":  #SSL version case
        temp=re.findall('ro.build.fingerprint.*[]]', data)
        if len(temp)==1:
            #print "case2. 1"
            fingerprint=temp[0].split("[")[1][:-1]
            #print "21",fingerprint
        if len(temp)==2: #case with txt files getprop
            #print "case2. 2"
            if str(temp[0]) == str(temp[1]):
                fingerprint=temp[0].split("[")[1][:-1]
                #print "2. 2",fingerprint
            else:
                fingerprint=temp[0].split("[")[1][:-1]+" / "+temp[1].split("[")[1][:-1]
            
    if fingerprint=="":#case with txt files SDT
        temp=re.findall('Fingerprint[\W].*', data)
        #print "case 3",temp
        if len(temp)==2:
            if str(temp[0]) == str(temp[1]):
                fingerprint=temp[0].split(": ")[1][:-1]
                #print "case 3.1",fingerprint
            else:
                fingerprint=temp[0].split(": ")[1][:-1]+" / "+temp[1].split(": ")[1][:-1]
        else:
            fingerprint=temp[0].split('"')[1]
            #print "case 3.2",fingerprint
    return fingerprint
        
def get_starttime(data,io=""):
    starttime=""
    for line in data.split("\n"):
        if 'creation-time="' in line and "ctsVerifierReport" in io:
            temp=re.findall('creation-time=.*',line)
            temp=temp[0].replace("'",'"')
            starttime=temp.split('"')[1]
            print "ctsverifier    ------  ",starttime
            break 
        if "starttime=" in line:
            temp=re.findall("starttime=.*",line)
            starttime=temp[0].split('"')[1]
            print starttime, temp
            break
        if "TestDate=" in line and starttime == "":
            temp=re.findall("TestDate=.*",line)
            starttime=temp[0].split('"')[1]
            print starttime, temp
            break
        if "testDate=" in line and starttime == "" and "BSI":
            temp=re.findall('testDate=.*',line)
            temp=temp[0].replace("'",'"')
            starttime=temp.split('"')[1]
            print starttime, temp
            break
           
    return starttime
        
def get_endtime(data,io=""):
    endtime=""
    for line in data.split("\n"):
        if "ctsVerifierReport" in io :
            io_time=io.split("-")[1]+"-"+io.split("-")[2]
            endtime=io_time
            print "ctsverifier    ------  "+io_time
            break
        if "endtime=" in line:
            temp=re.findall("endtime=.*",line)
            endtime=temp[0].split('"')[1]
            #print endtime#, temp
            break
        if "TestDate=" in line and endtime == "":
            temp=re.findall("TestDate=.*",line)
            endtime=temp[0].split('"')[1]
            #print endtime#, temp 
            break        
        if "testDate=" in line and endtime == "":
            temp=re.findall("testDate=.*",line)
            temp=temp[0].replace("'",'"')
            endtime=temp.split('"')[1]
            #print endtime#, temp
            break
    return endtime
            
            
        
        
        
        
        