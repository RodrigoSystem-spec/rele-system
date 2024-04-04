import os
import time
import datetime
import os.path, time
import RPi.GPIO as GPIO
import multiprocessing as mp

pin=40
flagOnOff=0
flagsdfull = 0
statusOn=0
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.IN)

def start_recording():
    os.system('/home/pi/R-System/stream.sh')
    
while True:
    now=datetime.datetime.now()
    file=open('/home/pi/R-System/camara-tiempo.txt', 'r')
    line=file.readline()
    start=int(line[9:11])
    end=int(line[12:14])
    file.close()    
    if now.hour>=start and now.hour<end:
        statusOn=1    
        if GPIO.input(pin)==True and statusOn==1:
           time.sleep(50/1000)
           if GPIO.input(pin)==False:
              print('Descarto Video')
           else:
            if flagOnOff==0:
                flagOnOff=1
                if flagsdfull==0:
                   if __name__=='__main__':
                       p=mp.Process(target=start_recording)
                       p.start()
                       print('Rele ON')
                       time.sleep(1)
                else:
                      print('Rele ON - FullSD')     
                      time.sleep(1)
        else:
            if GPIO.input(pin)==False:
                if flagOnOff==1:
                    flagOnOff=0
                    os.system('sudo killall ffmpeg')
                    print('Rele OFF')
                    print('Esperando Rele ON')
                    folder = ("/home/pi/R-System/Videos")
                    folder_size = 0
                    for (path, dirs, files) in os.walk(folder):
                        for file in files:
                            filename = os.path.join(path, file)
                            folder_size += os.path.getsize(filename)
                    if folder_size>44000000000:
                        flagsdfull = 1
                        print('Espacio insuficiente')
                        log=open('/home/pi/R-System/informes.txt', 'a')
                        log.write('Espacio insuficiente en la micro SD ' + str(datetime.datetime.now()))
                        log.close()
                        time.sleep(1)
                        break
                    else:
                        flagsdfull=0 
                        pass                 
                                        
                else:
                    now = datetime.datetime.now()
                    if now.hour >= end and statusOn == 1:
                        statusOn = 0
                        os.system('sudo killall ffmpeg')
            else:
                pass
                time.sleep(1)
    else:
        print('En tiempo de inactividad')
        time.sleep(1)

