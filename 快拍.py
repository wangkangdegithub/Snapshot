'''
create on 2017/8/3
@author: wangkang
'''

import numpy as np
import cv2
import time
import win32api,win32con,win32gui
import threading


def accSum(n):
    sum = 0
    for i in range(1, n): #[1,n+1)
        sum += i
    return sum


def auto_picture(n):
    cap = cv2.VideoCapture(0)           #读取摄像头，0表示系统默认摄像头
    win32api.keybd_event(81,0,0,0)      #模拟键盘输入   q键  位码是81
    win32api.keybd_event(81,0,win32con.KEYEVENTF_KEYUP,0)   #模拟键盘输入
    count = 0
    for i in range(n):
        ret,photo=cap.read()            #读取图像
        cv2.imshow('TEST',photo)        #将图像传送至窗口
        key=cv2.waitKey(1)              #设置等待时间，若数字为0则图像定格

        win32api.keybd_event(8,0,0,0)   #空格键  位码是8
        win32api.keybd_event(8,0,win32con.KEYEVENTF_KEYUP,0)
        #filename = "F:/auto_picture/%s.jpg" % time.strftime('%Y%m%d-%H%M%S',time.localtime())
        filename = "F:/auto_picture/noman.%s.jpg" % i       #文件名以‘noman.’开头
        cv2.imwrite(filename,photo)                         #保存位置
        time.sleep(1)
        count += i
        if count == accSum(n):
            break
    cap.release()
    cv2.destroyAllWindows()
    print ('快拍结束')


auto_picture(100)


'''
#demo

cap = cv2.VideoCapture(0)     #读取摄像头，0表示系统默认摄像头  
  
while (True):  
    ret,photo=cap.read()      #读取图像  
    cv2.imshow('TEST',photo)  #将图像传送至窗口  
    key=cv2.waitKey(1)        #设置等待时间，若数字为0则图像定格  
    
    if key==ord(" "):         #按空格获取图像  
        filename = "F:\%s.jpg" % time.strftime('%Y%m%d-%H%M%S',time.localtime())
        #filename = time.strftime('%Y%m%d-%H%M%S') + ".jpg"  #以当前时间存储  
        cv2.imwrite(filename,photo)                         #保存位置  
        #cv.SaveImage(filename,img)
        
    if key==ord("q"):         #按“q”退出程序  
        break  

cap.release()
cv2.destroyAllWindows()
'''