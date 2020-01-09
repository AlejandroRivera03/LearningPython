import datetime
import time
import os

def fixNumber( num ):
    if num < 10:
        return '0'+str(num)
    else:
        return num

while True:
    os.system('cls')
    dt = datetime.datetime.now()
    print('{}:{}:{}'.format( 
        dt.hour, 
        fixNumber( dt.minute ), 
        fixNumber( dt.second ) ) )
    time.sleep( 1 )