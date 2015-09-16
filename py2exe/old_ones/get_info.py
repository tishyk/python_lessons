# -*- coding: utf-8 -*-
import os

def info():
    try:
        try:
            model=(os.popen('adb shell getprop ro.product.model').read()).rstrip()
        except IOError:
            pass
        if model:
            av=(os.popen('adb shell getprop ro.build.version.release').read()).rstrip()
            customer=(os.popen('adb shell getprop ro.csc.sales_code').read()).rstrip()
        else:
            print('adb shell not started !')
            model='  --//--'
            av='  --//--'
            customer='  --//--'
        return model,av,customer
    except Exception:
        return '0','0','0'

def boot(command):
    answer=(os.popen(command).read()).rstrip()
    return(len(answer))
     
