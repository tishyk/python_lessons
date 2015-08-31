import getpass

# Start
name = ' '
if name:
    while True:
        print '''Who are you?'''
        name = raw_input()
        
        if name!='Alice':
            continue
        
        print "Hello, Alice!\n What is the password? (it is a fish)"
        password  = getpass.getpass('Password:')
        
        if password == 'swordfish':
            break
        else:
            continue
        
print ('Access Granted!')
#End
