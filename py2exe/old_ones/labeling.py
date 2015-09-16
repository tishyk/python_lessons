# -*- coding: utf-8 -*-
import re
from P4 import P4
from base64 import b16encode as e1, b32encode as e3, b64encode as e6
from magic import _

try:
    config_ini=open('config.ini','a+').read()
    print 'read config.ini...'
    p4server=re.findall('p4_ser.*',config_ini)[0].split(':')[1]
    print p4server
except:
    p4server="p4proxy"
    pass

p4=P4()

f=open('temp.data','r').readlines()
data = [_(line[:-1]) for line in f]


p4.user=data[0]
p4.password=data[1]
p4.port=p4server+":"+data[2].rstrip()
TemplateName=data[3]
LabelName=data[4]
model=data[5]
sw_pl=data[6]
devgroup=data[7]
step=data[8]
version=data[9]
cl_full=data[10]
cl_partials=data[11].replace(' ','')
code=data[12]
csc=data[13]
modem=data[14]
comment=data[15]

#open('temp.data','w').write('0')

module_name=(str(p4.user).upper()).replace('.', '_')
#SRK_RT_S_TISCHENKO_AUTOMATITION-LABELING-TOOL
workspace = "SRK_RT_"+module_name+"_AUTOMATITION-LABELING-TOOL"

p4.connect()
# reload workspace
try:
    p4.run('reload', '-c',workspace)[0]
    print "Workspace reloaded!"
except:
    print "No need Workspace reloading!"

p4.client=workspace
#print p4.client
label_Description="""[MODEL] %s
[SW PL] %s
[DEV_GROUP] %s
[STEP] %s
[VERSION] %s

[BASE CL] %s
[ADD CL] %s

[Code] %s
[CSC] %s
[Modem] %s
[Comment] %s


***** Created by SRK RT Help Box 1.0. (dev. s.tischenko)  ***** """ % (
    model,sw_pl,devgroup,step,version,cl_full,cl_partials, code,csc,modem,comment)

w_description="""
Created by SRK RT Help Box 1.0
Developer - s.tischenko
Copy View from: """ + TemplateName+'\n\n'


# Find template on p4 (copy view for workspace from here)
template=p4.run('client','-o',TemplateName)[0]

# replace TemplateName from view by workspace view
w_view=[view.replace(TemplateName,p4.client)for view in template['View']]
l_view=[view.split(' ')[0] for view in template['View']]

# Workspace creation with p4.client name
clientspec = p4.fetch_client()
clientspec['View'] = w_view
clientspec['Description'] = w_description

p4.save_client( clientspec ) # saving workspace to p4
clientspec = p4.fetch_client() # connection to workspace
print p4.client,'Client was created!\nView copied from:\n',TemplateName

# Label Creation on p4 with LabelName

labelspec = p4.fetch_label(LabelName) 
labelspec['View']=l_view
#labelspec['Options']= 'noautoreload'
labelspec['Description']= label_Description
#labelspec['Revision']='@'+cl_full
p4.save_label( labelspec )
print 'Label -',LabelName

#p4 label -d SM-T210_EUR_KK_XX_T210ILOBNI1_NI09R2_CSC_TEST  - coomand for delete

# --------- Labeling view line by full -------
print 'Start Labeling (Full -'+cl_full+')'

'''
for line in l_view:
    #p4 command: p4 tag -l SM-T210_EUR_KK_XX_T210ILOBNI1_NI09R2_CSC_TEST //CSC/Maple/PXA986/lt02wifi/LATIN/...@2732000
    p4.run('tag','-l',LabelName,line+'@'+cl_full)

'''
for line in l_view:
    try:
        #p4 command: p4 tag -l SM-T210_EUR_KK_XX_T210ILOBNI1_NI09R2_CSC_TEST //CSC/Maple/PXA986/lt02wifi/LATIN/...@2732000
        p4.run('tag','-l',LabelName,line+'@'+cl_full)
        print line+"- labeling complete!"
    except:
        print 'Exception raised! -',line 



#--------- Labeling partials ---------------
exception_cl_list=[]

for partial in re.findall('[0-9]{3,10}',cl_partials):
    if len(partial)>3:
        try:
            try:
                partial=partial.rstrip()
                print partial
                change = p4.run('describe','-s', partial)[0] #connect to partial
                depotFiles = change['depotFile'] # get list of files that should be under label
                revisions = change['rev']
        
                file_revs=[depotFile+'#'+revision for depotFile,revision in zip(depotFiles,revisions)]
                
                #labeling all files in Cl partial
                for  file_rev in  file_revs:
                    #commands look like - p4 tag -l SM-T210_EUR_KK_XX_T210ILOBNI1_NI09R2_CSC_TEST //CSC/Maple/PXA986/lt02wifi/LATIN/ZTO/system/csc/default_workspace.xml#4
                    labeling = p4.run('tag','-l',LabelName,file_rev)[0]
                    print  file_rev,'partial file added!'
            except:
                if partial not in exception_cl_list:
                    exception_cl_list.append(file_rev)
        except:
            print 'Labeling partial failed! Label will be deleted!' 
            p4.run('label','-d',LabelName)
            p4.disconnect()

labelspec = p4.fetch_label(LabelName) 
labelspec['Options']= 'locked noautoreload'
p4.save_label( labelspec )
for file_rev in exception_cl_list:
    print 'Files not added! Check Changelist view! -',file_rev
p4.disconnect()
print 'Locked', LabelName
print 'All Done!'


