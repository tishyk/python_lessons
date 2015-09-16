import os
import re
import sys
import xlwt
import time
import argparse

from get_device_id_console import get_device_id

__author__ = 's.tischenko'

'''Open-Close test for any package, package list can be run also!
Test command:
-p com.samsung.android.sdk.sgi.samples.sgbluranimation -a SampleActivity -c 100
'''

parser = argparse.ArgumentParser()

parser.add_argument("-p",'--name', type=str, default='com.samsung.android.sdk.sgi.samples.sgbluranimation',
                    help= "Set package name!(Ex. 'com.sec.android.app.bath')")

parser.add_argument("-a",'--activity', type=str, default='SampleActivity',
                    help= "Set activity name!(Ex. 'ActivityBath')")

parser.add_argument("-c", '--count', type=int, default=50,
                    help= "Set count value for test! (Ex. '100')")

args = parser.parse_args()

package = args.name
activity = args.activity
count = args.count

    
def openApp(package,activity,device_id):
    os.popen("adb -s "+device_id+" wait-for-device shell am start -n " +package+'/.'+ activity)

def closeApp(package,device_id):
    os.popen("adb -s "+device_id+" shell input keyevent 4")

def get_memory_usage(package,device_id):
    total = ''
    lines = os.popen('adb -s '+device_id+' shell dumpsys meminfo '+package).readlines()
    for line in lines:
        if 'TOTAL' in line:
            total = int(re.findall('\d{1,8}',line)[0])
            break
    return total

def check_package_activity(package,device_id):
    lines = os.popen('adb -s'+device_id+' shell dumpsys window').readlines()
    a = ['Crash' for x in lines[-20:] if 'mCurrentFocus=Window' and 'Application Error' in x]
    if len(a)>0:
        return 1
    
def run_test(package,count,add):
    print package
    memory_list,crash,i = [],0,0
    demo_name = package.split('.')[-1]
    os.popen('mkdir Test_details_'+add)
    f_name = 'Test_details_'+add+os.sep+demo_name+'.txt'
    with open(f_name,'a') as f:
        while i<=count:
            openApp(package, activity, device_id)
            time.sleep(2)
            i+=1
            res = get_memory_usage(package,device_id)
            if check_package_activity(package,device_id)==1:
                os.popen("adb -s "+device_id+" shell input keyevent 66 66")
                crash+=1
                f.write('Crash\n')
                print 'Crash'
                os.popen("adb -s "+device_id+" logcat -d>>"+f_name.replace('.txt','_log.txt'))
                os.popen("adb -s "+device_id+" logcat -c")
                os.popen("adb -s "+device_id+" shell am force-stop " + package)
                closeApp(package,device_id)
                continue
            memory_list.append(res)                
            closeApp(package,device_id)
            time.sleep(0.5)
            if i%10==0: print 'Test', i,'from', count
            f.write(str(memory_list[-1])+'\n')
            
        result = (package+'\nCrash count - %s\nMin/Max memmory (%s/%s)\n'+'-'*80+'\n') % (
            crash,min(memory_list),max(memory_list))
        f.write(result)
        f.flush()
        os.popen("adb -s "+device_id+" shell am force-stop " + package)
        return result,crash,min(memory_list),max(memory_list)
        
def run_test_for_demo_apps(device_id,count,package_name='com.samsung.android.sdk.sgi.samples'):
    command = "adb -s "+device_id+" shell pm list packages -f "+package_name
    package_list = [x.split('.apk=')[-1].strip() for x in os.popen(command).readlines() if package_name in x]
        
    add = time.ctime().replace(':','_')
    add=add.replace(' ','_')
    wb = xlwt.Workbook()
    ws = wb.add_sheet(add)
    ws.write(0,0,'Package Name')
    ws.write(0,1,"Count")
    ws.write(0,2,"Total Crash")
    ws.write(0,3,"Memory min")
    ws.write(0,4,"Memory max")
    with open('Test_result_'+add+'.txt','a+') as f:
        for e,package in enumerate(package_list):
            print 'Run package %s from %s'%(e,len(package_list))
            result,crash,minimum,maximum = run_test(package,count,add)
            ws.write(e+1,0,package.split('.')[-1])
            ws.write(e+1,1,count)
            ws.write(e+1,2,crash)
            ws.write(e+1,3,minimum)
            ws.write(e+1,4,maximum)
            try:
                wb.save('Test_result_'+add+'.xls')
            except IOError as e:
                print e          
            f.write(result)
            print result
            f.flush()

                
device_id = get_device_id()     
print 'Count - %s\n'% count

run_test_for_demo_apps(device_id,count,package)

print "Test Done"
time.sleep(1000)




















