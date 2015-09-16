# -*- coding: utf-8 -*-

import sys,time,subprocess
# send arguments to vars
stream=['a','b b','c12']
child=subprocess.Popen(['ar.py']+stream, shell=True, stdout=subprocess.PIPE) 
   
s=' ' 
while s: 
    s=child.stdout.readline() 
    print s.rstrip()
print 'done'
time.sleep(7)
