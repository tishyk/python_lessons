#! -*- coding:utf-8 -*-
import traceback
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s
- %(message)s')
#logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s
#- %(message)s')  for saving debug info into file myProgramLog.txt

'Example 1. Raise Exeption '

def spam():
    bacon()
def bacon():
    raise Exception('This is the error message.')

spam()

#---------------------------------------------------------------------------  

'Example 2. Raise Exeption '

def boxPrint(symbol, width, height):
       if len(symbol) != 1:
         raise Exception('Symbol must be a single character string.')
       if width <= 2:
         raise Exception('Width must be greater than 2.')
       if height <= 2:
         raise Exception('Height must be greater than 2.')
       print(symbol * width)
       for i in range(height - 2):
           print(symbol + (' ' * (width - 2)) + symbol)
       print(symbol * width)

   for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
     try:
       boxPrint(sym, w, h)
     except Exception as err:
      print('An exception happened: ' + str(err))

#----------------------------------------------------------------------------

'Example 3. Saving traceback to file'

try:
         raise Exception('This is the error message.')
except:
         with open('errorInfo.txt', 'w+') as f:
          f.write(traceback.format_exc()) # traceback.format_exc() - contain trace info about exeption in your programm
          print('The traceback info was written to errorInfo.txt.')
          
#----------------------------------------------------------------------------

'Example 4. Assertion'

doorStatus = 'open'
assert doorStatus == 'open', 'The doors need to be "open".'
doorStatus = 'closed'
assert doorStatus == 'open', 'The doors need to be "open".'

#----------------------------------------------------------------------------

'Example 5. Traffic Light Simulation without/with assertion'

market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
        #print stoplight
        assert 'red' in stoplight, "traffic warning!!!\n No red light!"

switchLights(market_2nd) 

# Assertions can be disabled by passing the -O option when running Python ('python -O filename.py')

#----------------------------------------------------------------------------

'Example 6. Debugging with logging module'
'''Next rows should be inserted after shebang line !#
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s
- %(message)s')  '''
# logging.disable(logging.CRITICAL) set this line for dissabling debug info
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')

''' 
Level    Logging Function    Description
DEBUG    logging.debug()     The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems.
INFO     logging.info()      Used to record information on general events in your program or confirm that things are working at their point in the program.
WARNING  logging.warning()   Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.
ERROR    logging.error()     Used to record an error that caused the program to fail to do something.
CRITICAL logging.critical()  The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely.
'''
