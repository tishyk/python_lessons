#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 's.tischenko'

import urllib, urllib2
import zipfile, time, os
import xml.etree.ElementTree as ET
from magic import _
from base64 import b16encode as e1, b32encode as e3, b64encode as e6


time.clock() # start timer
SERVER = '106.125.34.167:443'

def login_data_coding():
    if os.path.exists('login.data'):
        f=open('login.data','r').readlines()
        data = [_(line[:-1]) for line in f]
        login = data[0]
        password = data[1]
        print 'Welcome',login,'!\n'
    else:
        login = raw_input('Enter mySingle_id: ')
        password  = raw_input('Enter password: ')
        f = open('login.data','a')
        [f.write(e1(e3(e6(str(line))))[::-1]+'\n') for line in (login,password)]
    return login, password

def get_page_xml(page):
    authinfo.add_password(None, SERVER, Login, Pass)
    handler = urllib2.HTTPBasicAuthHandler(authinfo)
    myopener = urllib2.build_opener(handler)
    urllib2.install_opener(myopener)
    tries = 0
    output = urllib2.urlopen(page, timeout=5)
    while True:
        try:
            output = urllib2.urlopen(page, timeout=5)
            break
        except:
            tries += 1
            if tries >= 10:
                print 'TeamCity: Fatal error: Repeated timeouts'
                break
    print "\nConnected to TeamCity!"
    page_xml = output.read()
    output.close()
    #print page_xml
    return page_xml

def page_parse(page_xml,build_info):
    page = ET.fromstring(page_xml)
    for obj in page:
        if "SUCCESS" not in obj.get("status"):
            continue
        build_info['buildNumber'].append(obj.get("number"))
        build_info['build_id'].append(obj.get("id"))

        build_info['status'].append (obj.get("status"))
        build_info['branchId'].append (obj.get("branchId"))
        build_info['href'].append(obj.get("href") )
        build_info['webUrl'].append(obj.get("webUrl"))
    return build_info

def get_artifacts(build_info,buildNumber = None):
    index = 0
    if buildNumber:
        index = build_info['buildNumber'].index(buildNumber)
    build_id = build_info['build_id'][index]
    webUrl = build_info['webUrl'][index]
    artifact_link = webUrl.replace('viewLog.html?buildId='+str(build_id)+'&buildTypeId=', 'repository/downloadAll/')
    artifact_link = artifact_link+'/'+build_id+':id/artifacts.zip'
    print 'Artifacts link :\n', artifact_link,'\nBuild number is -', build_info['buildNumber'][index]
    return artifact_link, build_info['buildNumber'][index]

def artifact_release(zip_name,dir_name):
    z = zipfile.ZipFile(zip_name, "r")
    z.extractall(dir_name)
    z.close()
    try:
        os.remove(zip_name)
    except:
        print 'Zip file not removed '

login_data = login_data_coding()
Login = login_data[0]
Pass = login_data[1]
    
urllib.FancyURLopener.prompt_user_passwd = lambda a,b,c : (Login, Pass)
authinfo = urllib2.HTTPPasswordMgrWithDefaultRealm()









