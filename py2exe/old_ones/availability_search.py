import io
encodings=('utf-16-le','utf-8','utf-16','utf-16-be','cp1251','cp1252','cp1255')

def availability(country,path):
    print country
    for en in encodings:
        try:
            if 'a' in io.open(path, 'r', encoding = en).read():
                e=en ;print e; break
        except:
            pass
    try:
        lines=io.open(path, 'r', encoding = e).readlines()
        apps=''
        ind_start=''
        country_len=0
    except:
        print 'Start Values not initialized'
    try:    
        for line in lines[:30]:# 
            if 'Google Application\t' in line:
                ind_start=lines.index(line)#get index of applications name line start
            if ('Android version' in line and
                ind_start):
                ind_end=lines.index(line)#get index of applications name line end
                break
    except:
        print 'Application not found!!!'
    try:
        #print ind_start,ind_end
        for line in lines[ind_start:ind_end]:
            apps+=(line.rstrip()).replace('"','')# delete \n and " from applications line
            
        aplications=apps.replace('Google Application\t','').split('\t')
        app_len=len(aplications)
    except:
        print "check Application separator"
    #print (len(apps.replace('Google Application\t','').split('\t')))
    try:
        for line in lines[ind_end:] :
            
            # block for Mandatory applications or optional
            if 'Mandatory or Optional' in line:
                mandatory_len=len(line.replace('Mandatory or Optional\t','').split('\t'))
                mandatory_line=(line.replace('Mandatory or Optional\t','')).rstrip()#delete 'Mandat..' and \n from line
                if mandatory_len==app_len:
                    mandatory_len2=mandatory_len
                    mandatory_value=mandatory_line.split('\t')
                    
                else:
                    mandatory_ind=lines.index(line)
                    for l in lines[mandatory_ind+1:mandatory_ind+7]:
                        mandatory_line+=l.rstrip()
                        mandatory_len2=len(mandatory_line.split('\t'))# get values for all applications
                        if mandatory_len2==app_len:# stop when len applications=len values after Country
                            mandatory_value=mandatory_line.split('\t')
                            break
                        else:
                            continue
                    
            # block for country   
            if country in line:
                country_len=len(line.replace(country+'\t','').split('\t'))
                country_line=(line.replace(country+'\t','')).rstrip()#delete country name and \n from line
                #print line,len((line.replace(country+'\t','')).split('\t'))
                if country_len==app_len:
                    country_len2=country_len
                    aplications_value=country_line.split('\t')
                    break
                else:
                    country_ind=lines.index(line)
                    for l in lines[country_ind+1:country_ind+7]:
                        country_line+=l.rstrip()
                        country_len2=len(country_line.split('\t'))# get values for all applications
                        if country_len2==app_len:# stop when len applications=len values after Country
                            aplications_value=country_line.split('\t')
                            break
                        else:
                            continue
                        
        print 'Counts aplications/aplication values/mandatory values:',app_len,'/',country_len2,'/',mandatory_len2
        print '\nAplications:\n',aplications,'\nAplications value:\n',aplications_value,'\nMandatory_value:\n',mandatory_value
        
        return aplications,aplications_value,mandatory_value
    
    except:
        print 'Mandatory or Optional or country line errors'
       

