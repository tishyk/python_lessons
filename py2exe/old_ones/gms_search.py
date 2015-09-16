# -*- coding: utf-8 -*-
import io
encodings=('ascii','utf-8','utf-16','utf-16-le','utf-16-be','cp1251','cp1252','cp1255')

def get_gms(path):
    print (path)
    D={'GMS APKs':[],'Packages':[],'App':[],'Revision':[],'Description':[]}
#    path='GMS_apps_Package_4.2.txt'
    for en in encodings:
        try:
            x=io.open(path, 'r', encoding = en)
            if 's' in x.readline():
                f=x.readlines()
                print en, x.readline()
                break
        except:
            print en,' - failed'

    for line in f[:3]:
        print line,('Packages' in line)
        if 'ackag' in line: #try to find headers index
            start_index=f.index(line)#start point for analizing
            lind=line.split('\t')
            print line,lind
            #get index for headers(app,pack..)
            for l in lind:
                if 'APK' in l:
                    index_gms=lind.index(l)
                    #print index_gms
                if 'ackag' in l:
                    index_packages=lind.index(l)
                    #print index_packages
                if 'pp' in l:
                    index_app=lind.index(l)
                    #print index_app
                if 'R' in l:
                    index_rev=lind.index(l)
                    #print index_rev
                if 'escript' in l:
                    index_desc=lind.index(l)
                    #print index_desc
            print('index_gms:'+str(index_gms),'index_packages:'+str(index_packages),
                  'index_app:'+str(index_app),'index_rev:'+str(index_rev),
                  'index_desc:'+str(index_desc))
            break
        else: # if headers not in file, set default index
            index_gms=0
            index_packages=1
            index_app=2
            index_rev=3
            index_desc=4
            start_index=-1
            
    for line in f[start_index+1:]:#
        D['GMS APKs'].append((line.split('\t')[index_gms]).rstrip())
        D['Packages'].append((line.split('\t')[index_packages]).rstrip())
        D['App'].append((line.split('\t')[index_app]).rstrip())
        D['Revision'].append((line.split('\t')[index_rev]).rstrip())
        D['Description'].append((line.split('\t')[index_desc]).rstrip())
    #print (D)
    return D

#get_gms('')
