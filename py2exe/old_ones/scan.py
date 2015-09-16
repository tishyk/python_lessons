import glob, os,re
from zipfile import  ZipFile
from main import *

file_info={"abs_path":["Summary",]}
file_table={}

def clean(l,sep='"'):
    new_list=[]
    for line in l:
        line=line.split(sep)[1]
        new_list.append(line)
    return new_list

def read_zip(path):
    data=""
    z=ZipFile(path)
    zip_files=z.namelist()
    #print zip_files
    for z_name in zip_files:
        if ".xml" in z_name and "~" not in z_name and "_" not in z_name:
            data=z.read(z_name)
        if "test_result" in z_name:
            data=z.read(z_name)
    if data == "":
        for z_name in zip_files:
            if ".txt" in z_name and "~" not in z_name : 
                data+=z.read(z_name)
    return data

def open_function(data,path):
    if "BSI" in path:
        BSI(data,path)
    if "BVT" in path:
        BVT(data,path)
    if "CscCh" in path:
        CscChecker(data,path)
    if "ctsVer" in path:
        ctsVerifier(data,path)
    if "cts_res" in path:
        cts_result(data,path)
    if "getprop" in path:
        getprop(data,path)
    if "LoggingCh" in path:
        LoggingChecker(data,path)
    if "OpenSSL" in path:
        OpenSSL(data,path)
    if "SCAT" in path:
        SCAT(data,path)
    if "SDT" in path:        
        SDT(data,path)
    if "SSLver" in path:
        SSLver(data,path)
    if "Wwd" in path:
        Wwd(data,path)
    if "xtsTest" in path:
        xtsTest(data,path)
    
    
def BSI(data,path):
    print "BSI found!" 
    file_table[path]=[]
    values=["testName","modelName","fingerprint",'FingerPrint',"result","latestDate",'TestDate','FinalResult']
    for value in values:
        temp=re.findall(value+'=".*',data)
        result=clean(temp)[0]
        file_table[path].append([value,result])
            
    FileName=re.findall(' FileName=.{70}',data)
    Result=re.findall(' Result=\"\w*\"',data)

    for i,value in enumerate(FileName):
        print value, Result[i]         
        file_table[path].append(["FileName ",clean([value])[0]])
        file_table[path].append(["Result ",clean([Result[i]])[0]])

def BVT(data,path):
    print "BVT found!" 
    file_table[path]=[]
    values=["testPlan","build_fingerprint","build_model","buildVersion",'build_type','imei']
    for value in values:
        temp=re.findall(value+'=".*',data)
        result=clean(temp)[0]
        file_table[path].append([value,result])
        #print result
    for i,line in enumerate(data.split("\n")):
        if "<Test endtime=" in line and  "result" in line and 'result="fail"' in line:  
             
            temp=re.findall('name=".*',line)
            result=clean(temp)[0]
            file_table[path].append(["Failed item",result])
            
            next_line=data.split("\n")[i+1]
            temp=re.findall("FailedScene message=.*",next_line)
            print temp, next_line
            result=clean(temp)[0]

            file_table[path].append(["Error message",result])
            
def CscChecker(data,path):
    print "CscChecker found!" 
    file_table[path]=[]
    values=["testName","fingerprint","modelName","buildVersion","result"]
    for value in values:
        temp=re.findall(value+'=".*',data)
        result=clean(temp)[0]
        file_table[path].append([value,result])
        #print result
    for line in data.split("\n"):
        if "CSC name=" in line:   
            temp=re.findall('CSC name=".*',line)
            result=clean(temp)[0]
            file_table[path].append(["CSC name",result])

def ctsVerifier(data,path):
    print "ctsVerifier found!" 
    file_table[path]=[]
    values=["fingerprint","model","release","creation-time"]
    for value in values:
        temp=re.findall(value+'=".*',data)
        result=clean(temp)[0]
        file_table[path].append([value,result])
        #print result
    for line in data.split("\n"):
        if "<test title=" in line and  "result" in line and 'result="pass"' not in line:   
            temp=re.findall('title=".*',line)
            result=clean(temp)[0]
            file_table[path].append(["Failed item",result])

def cts_result(data,path):
    print "cts_result found!" 
    file_table[path]=[]
    values=["testPlan","build_fingerprint","build_model","buildVersion",'build_type','imei',"starttime","endtime"]
    for value in values:
        temp=re.findall(value+'=".*',data)
        result=clean(temp)[0]
        file_table[path].append([value,result])
        #print result
    file_table[path].append(["",""])
    for i, line in enumerate(data.split("\n")):
        if "<Test name=" in line and  "starttime" in line and 'result="fail"' in line:  
             
            temp=re.findall('name=".*',line)
            result=clean(temp)[0]
            file_table[path].append(["Failed item",result])
 
            next_line=data.split("\n")[i+1]
            temp=re.findall("FailedScene message=.*",next_line)
            print temp, next_line
            result=clean(temp)[0]

            file_table[path].append(["Error message",result])
            
def getprop(data,path):
    print "getprop found!" 
    file_table[path]=[]
    temp=re.findall("ril.sales_code"+'.*[]]',data)
    result=clean(temp,"[")
    for res in result:
        file_table[path].append(["ril.sales_code",res[:-1]])    
    values=["ril.official_cscver","ro.build.fingerprint","ro.build.type","ro.com.google.gmsversion","ril.hw.ver"]
    for value in values:
        temp=re.findall(value+'.*[]]',data)
        
        result=clean(temp,"[")
        for i,res in enumerate(result):
            file_table[path].append(["["+file_table[path][i][1]+"] "+value,res[:-1]])      
            
def LoggingChecker(data,path):
    print "LoggingChecker found!" 
    file_table[path]=[]
    values=["testName","fingerprint","modelName","testDate","result","tester"]
    for value in values:
        temp=re.findall(value+'=".*',data)
        result=clean(temp)[0]
        file_table[path].append([value,result])
    file_table[path].append(["",""])
    #print result
    for line in data.split("\n"):
        if "<Detailed package=" in line and  "type=" in line and 'result="Pass"' not in line and 'result="Optional"' not in line :  
             
            temp=re.findall('package=".*',line)
            result=clean(temp)[0]
            file_table[path].append(["Failed item",result])
            
            temp=re.findall('type=".*',line)
            result=clean(temp)[0]
            file_table[path].append(["Item type",result])
            
def OpenSSL(data,path):
    print "OpenSSL found!" 
    file_table[path]=[]
    values=["build_fingerprint","build_model","build_type","buildVersion","starttime","endtime"]
    for value in values:
        temp=re.findall(value+'=".*',data)
        result=clean(temp)[0]
        file_table[path].append([value,result])
    file_table[path].append(["",""])
    #print result
    for line in data.split("\n"):
        if "<Test name=" in line and  "starttime=" in line and 'result="pass"' not in line :  
             
            temp=re.findall('name=".*',line)
            result=clean(temp)[0]
            file_table[path].append(["Failed item",result])

def SCAT(data,path):
    print "SCAT found!" 
    file_table[path]=[]
    values=["ro.build.fingerprint","ro.product.model","ril.official_cscver","labelName","ro.build.changelist"]
    for value in values:
        temp=re.findall(value+'=".*',data)
        result=clean(temp)[0]
        file_table[path].append([value,result])
    file_table[path].append(["",""])
    #print result
    for line in data.split("\n"):
        if "<Test name=" in line and  "deadline=" in line and 'result="PASS"' not in line :  
             
            temp=re.findall('name=".*',line)
            result=clean(temp)[0]
            file_table[path].append(["Failed item",result])          
              
            temp=re.findall('deadline=".*',line)
            result=clean(temp)[0]
            file_table[path].append(["Item deadline",result]) 
            
            temp=re.findall('changelist=".*',line)
            result=clean(temp)[0]
            file_table[path].append(["Item changelist",result])             
                       
def SDT(data,path):
    print "SDT found!" 
    file_table[path]=[]
    temp=re.findall("ro.csc.sales_code"+'.*',data)
    result=clean(temp,":")
    for res in result:
        file_table[path].append(["ro.csc.sales_code",res]) 
        print res   
    values=["Fingerprint","ril.official_cscver","ro.com.google.gmsversion"]
    for value in values:
        temp=re.findall(value+'.*',data)
        result=clean(temp,": ")
        for i,res in enumerate(result):
            file_table[path].append(["["+file_table[path][i][1]+"] "+value,res[:-1]])            
    file_table[path].append(["",""])
    values=["Warn","Fail"]
    
    for value in values:
        temp=re.findall("[[ ]"+value+'.*',data)
        result=clean(temp,"]")
        print result
        for i,res in enumerate(result):
            file_table[path].append(["["+file_table[path][i][1]+"] "+value,res])  
            
def SSLver(data,path):
    print "SSLver found!" 
    file_table[path]=[]
    values=["ro.build.fingerprint","ro.csc.sales_code","ro.product.model"]
    for value in values:
        value1=value.replace(".","[.]")
        temp=re.findall(value1+'.*',data)
        result=clean(temp,": ")[0]
        file_table[path].append([value+" ",result[1:-5]])
    file_table[path].append(["",""])

    for line in data.split("\n"):
        if "Test target=" in line and  "comment=" in line and 'result="PASS"' not in line:
            if 'result="GOOGLE"' in line:
                continue
 
            temp=re.findall('target=".*',line)
            result=clean(temp)[0]
            file_table[path].append(["Failed item",result])
            
            temp=re.findall('comment=".*',line)
            result=clean(temp)[0]
            file_table[path].append(["Target comment",result])     

def Wwd(data,path):
    print "BSI found!" 
    file_table[path]=[]
    values=["modelName","fingerprint",'version',"result","testDate"]
    for value in values:
        temp=re.findall(value+"=.*",data)
        print temp
        result=clean(temp,"'")[0]
        file_table[path].append([value,result])            
            
def xtsTest(data,path):
    print "xtsTestResult found!" 
    file_table[path]=[]
    values=["testPlan","buildFingerprint","buildModel","buildVersion","buildType","starttime","endtime"]
    for value in values:
        temp=re.findall(value+'=".*',data)
        result=clean(temp)[0]
        file_table[path].append([value,result])
        #print result
    for line in data.split("\n"):
        if "<Test name=" in line and  "result" in line and 'result="pass"' not in line:  
             
            temp=re.findall('name=".*',line)
            result=clean(temp)[0]
            file_table[path].append(["Failed item",result])
            
            
            
            
            
            
            
            
            