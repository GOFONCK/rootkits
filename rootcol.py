import os
import time                                             
import random
from termcolor import colored, cprint

print("Ключ аккаунта")
rootkits = int(input())-4000
print("VM")
skid = int(input())
print("TFS")                                            
timeFS = int(input())

if(skid > rootkits or rootkits < 0 or rootkits > 200):
 print("Ошибка по ключам!")                              
 exit()

i = 0
speed = 25

cprint('Сканирование...', 'green', 'on_blue')
time.sleep(4)
cprint('Компютер был распознан, начинается удаление возможных руткитов!', 'white', 'on_blue')
time.sleep(12)

if(rootkits > 0):
    rootkits += skid
    while i < rootkits:
        if( i == 7):
            time.sleep(timeFS)
        i += 1
        cprint("\tудаление руткитов: "+str(i)+" 0x00"+ str(random.uniform(100,999))+"\t", 'red', 'on_white')
        time.sleep(random.uniform(speed*0.001,speed*1.20))

    print("-----УДАЛЕНИЕ РУТКИТОВ ЗАВЕРШЕНО!-----")
    cprint("Было удалено "+str(rootkits)+" руткитов. использовано "+str(rootkits-skid)+" ключей декриптеров, у вас 3 дня для оплаты", 'white', 'on_blue')
else:
    time.sleep(1*speed)
    print("-----УДАЛЕНИЕ РУТКИТОВ ЗАВЕРШЕНО!-----")
