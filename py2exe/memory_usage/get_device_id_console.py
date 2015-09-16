# -*- coding: utf-8 -*-
import os

device_info = {'id':[],'model':[],'android_ver':[],'build_type':[]}

def get_prop():
    print 'Wait for device connection..'
    for device_id in device_info['id']:
        comm = 'adb -s '+device_id+' wait-for-device shell getprop ro.'
        device_info['model'].append(os.popen(comm+'product.model').read().rstrip())
        device_info['android_ver'].append(os.popen(comm+'build.version.release').read().rstrip())
        device_info['build_type'].append(os.popen(comm+'build.type').read().rstrip())

def get_device_id():
    device_info['id'] = []
    try:
        check = os.popen('adb devices').read()
        if len(check.split('\n')) == 3:
            device_info['id'].append("Device not connected!")
            device_info['model'].append('')
            device_info['android_ver'].append('')
            device_info['build_type'].append('')
        else:
            for line in check.split('\n')[1:]:
                device_id = line.split('\t')[0]
                if len(device_id)>4:
                    device_info['id'].append(device_id)
            get_prop()
            print 'Next device connected:'
            for ind,device in enumerate(device_info['id']):
                device_line = device_info['model'][ind]+'('+device_info['android_ver'][ind]+\
                              '/'+device_info['build_type'][ind]+'/'+device+')'
                print ind,'-'*3,device_line
            if ind>0:
                while True:
                    try:
                        index = int(raw_input("Choose device:"))
                        return device_info['id'][index]
                        break
                    except:
                        print 'Incorrect symbol'
                        
                
            else:
                return device_info['id'][0]
    except:
        device_info['id'].append("Device not connected!")
        device_info['model'].append('0')
        device_info['android_ver'].append('0')
        device_info['build_type'].append('0')
