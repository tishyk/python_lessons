# -*- coding: utf-8 -*-

import os, glob,time, thread
from threading import Thread
from get_device_id import*

apk = {}
#app_name = ['dance','bath','feeding','makeover']

install = lambda device_id,a: os.popen('adb -s '+device_id+' install -r '+apk[a]['path'][2:])
del_package = lambda device_id,package: os.popen('adb -s '+device_id+'wait-for-device uninstall '+package.lstrip()).read()

def delete_3d_party_apk(device_id, filter='com.samsung.demo'):
    thread_list = []
    command = 'adb -s '+device_id+' shell pm list packages -f '+filter
    apk_name_list = [apk.split('=')[1] for apk in os.popen(command).readlines()]
    [thread.start_new_thread(del_package,(device_id, package.rstrip()))for package in apk_name_list[::3]]
    #time.sleep(4)
    [thread.start_new_thread(del_package,(device_id, package.rstrip()))for package in apk_name_list[1::3]]
    #time.sleep(4)
    [thread.start_new_thread(del_package,(device_id, package.rstrip()))for package in apk_name_list[2::3]]
    #time.sleep(4)
    print('Deleted from '+device_id)

def adb_install(dir_name,device_id):
    global apk
    apk.clear()
    print('Wait for apk install ..')
    thread_list = []
    path = glob.glob(dir_name+'\\*.apk')
    if path == []:
        path = glob.glob(dir_name+'\\*\\*.apk')
    for p in path:
        apk[os.path.basename(p)] = {'path':p.replace('/','\\')}
    for a in apk.keys():
        thread_list.append(Thread(target=install, args=(device_id,a)))
    [tr.start() for tr in thread_list]
    [tr.join() for tr in thread_list[::2]]
    [tr.join() for tr in thread_list[1::2]]
    print('Installed for '+device_id)

if __name__ == '__main__':
    get_device_id()# from get_device_id.py