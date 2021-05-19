import RPi.GPIO as GPIO
from time import sleep
import time
import _tkinter as tk
from tkinter import ttk
from typing import Sized
from ttkthemes import themed_tk as tk
from tkinter import *
import multiprocessing 
########################
root = tk.ThemedTk()	
root.get_themes()
root.set_theme("radiance")
root1 = tk.ThemedTk()
root1.get_themes()
root1.set_theme("radiance")
root1.withdraw()
root2 = tk.ThemedTk()
root2.get_themes()
root2.set_theme("radiance")
root2.withdraw()
root3 = tk.ThemedTk()
root3.get_themes()
root3.set_theme("radiance")
root3.withdraw()
root4 = tk.ThemedTk()
root4.get_themes()
root4.set_theme("radiance")
root4.withdraw()
root5 = tk.ThemedTk()
root5.get_themes()
root5.set_theme("radiance")
root5.withdraw()
root6 = tk.ThemedTk()
root6.get_themes()
root6.set_theme("radiance")
root6.withdraw()
root7 = tk.ThemedTk()
root7.get_themes()
root7.set_theme("radiance")
root7.withdraw()
root8 = tk.ThemedTk()
root8.get_themes()
root8.set_theme("radiance")
root8.withdraw()
root9 = tk.ThemedTk()
root9.get_themes()
root9.set_theme("radiance")
root9.withdraw()
root10 = tk.ThemedTk()
root10.get_themes()
root10.set_theme("radiance")
root10.withdraw()
root11 = tk.ThemedTk()
root11.get_themes()
root11.set_theme("radiance")
root11.withdraw()
#######################
bdelay = 0.05
bsteps = 50
bpower = 50
bduration = 5.0
sdelay = 0.05
ssteps = 50
spower = 50
sduration = 5.0
option1 = "false"
option2 = "false"
delay=0.005
b = ""
s = ""
f = ""
start_time=0.0
stop_time=0.0
time_total=0.0
start_time2=0.0
stop_time2=0.0
time_total2=0.0
temp = 0.0
total = 0.0
rp=0.0
rsteps1=0.0
rsteps2=0.0
temp1=0.0
temp2=0.0
temp3=0.0
temp4=0.0
temp5=0.0
temp6=0.0
temp7=0.0
rduration1=0.0
rduration2=0.0	
######################
dc1_in1 = 23
dc1_in2 = 24
dc1_en = 25
###
dc2_in1 = 16
dc2_in2 = 20
dc2_en = 21
###
s1_in1 = 7
s1_in2 = 9
s1_in3 = 10
s1_en = 8
###
s2_in1 = 6
s2_in2 = 13
s2_in3 = 19
s2_en = 5
####
r1_gnd = 26
r2_gnd = 12
####
i=0
y=0

##########################
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(dc1_in1,GPIO.OUT)
GPIO.setup(dc1_in2,GPIO.OUT)
GPIO.setup(dc1_en,GPIO.OUT)
GPIO.setup(dc2_in1,GPIO.OUT)
GPIO.setup(dc2_in2,GPIO.OUT)
GPIO.setup(dc2_en,GPIO.OUT)
GPIO.setup(r1_gnd, GPIO.OUT)
GPIO.setup(r2_gnd, GPIO.OUT)
GPIO.output(r1_gnd, GPIO.LOW)
GPIO.output(r2_gnd, GPIO.LOW)
GPIO.output(dc1_in1,GPIO.LOW)
GPIO.output(dc1_in2,GPIO.LOW)
GPIO.output(dc2_in1,GPIO.LOW)
GPIO.output(dc2_in2,GPIO.LOW)
p=GPIO.PWM(dc1_en,1000)
q=GPIO.PWM(dc2_en,1000)
###########################
def set_delay(sleep_delay):
    delay=sleep_delay
def setup1():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(s1_in1, GPIO.OUT)
    GPIO.setup(s1_in2, GPIO.OUT)
    GPIO.setup(s1_in3, GPIO.OUT)
    GPIO.setup(s1_en, GPIO.OUT)
def setup2():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(s2_in1, GPIO.OUT)
    GPIO.setup(s2_in2, GPIO.OUT)
    GPIO.setup(s2_in3, GPIO.OUT)
    GPIO.setup(s2_en, GPIO.OUT)
def forwardStep1():
    global i
    global y  
    x=bsteps
    out1=s1_in1
    out2=s1_in2
    out3=s1_in3
    out4=s1_en
    for y in range(x,0,-1):  
        if i==0:
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(delay)
            #time.sleep(1)
        elif i==1:
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(delay)
            #time.sleep(1)
        elif i==2:  
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(delay)
            #time.sleep(1)
        elif i==3:    
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(delay)
            #time.sleep(1)
        elif i==4:  
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(delay)
            #time.sleep(1)
        elif i==5:
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(delay)
            #time.sleep(1)
        elif i==6:    
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(delay)
            #time.sleep(1)
        elif i==7:    
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(delay)
            #time.sleep(1)
        if i==7:
            i=0
            continue
        i=i+1
def forwardStep2():
    global i
    global y  
    x=ssteps
    out1=s2_in1
    out2=s2_in2
    out3=s2_in3
    out4=s2_en
    for y in range(x,0,-1):
        if i==0:
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(delay)
            #time.sleep(1)
        elif i==1:
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(delay)
            #time.sleep(1)
        elif i==2:  
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(delay)
            #time.sleep(1)
        elif i==3:    
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(delay)
            #time.sleep(1)
        elif i==4:  
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(delay)
            #time.sleep(1)
        elif i==5:
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(delay)
            #time.sleep(1)
        elif i==6:    
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(delay)
            #time.sleep(1)
        elif i==7:    
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(delay)
            #time.sleep(1)
        if i==7:
            i=0
            continue
        i=i+1
def backwardStep1():
    global i
    global y  
    x=bsteps
    out1=s1_in1
    out2=s1_in2
    out3=s1_in3
    out4=s1_en
    for y in range(x,0,-1):
        if i==0:
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(delay)
            #time.sleep(1)
        elif i==1:
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(delay)
            #time.sleep(1)
        elif i==2:  
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(delay)
            #time.sleep(1)
        elif i==3:    
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(delay)
            #time.sleep(1)
        elif i==4:  
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(delay)
            #time.sleep(1)
        elif i==5:
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(delay)
            #time.sleep(1)
        elif i==6:    
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(delay)
            #time.sleep(1)
        elif i==7:    
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(delay)
            #time.sleep(1)
        if i==0:
            i=7
            continue
        i=i-1
def backwardStep2():
    global i
    global y  
    x=ssteps
    out1=s2_in1
    out2=s2_in2
    out3=s2_in3
    out4=s2_en
    for y in range(x,0,-1):
        if i==0:
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(delay)
            #time.sleep(1)
        elif i==1:
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(delay)
            #time.sleep(1)
        elif i==2:  
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(delay)
            #time.sleep(1)
        elif i==3:    
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(delay)
            #time.sleep(1)
        elif i==4:  
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(delay)
            #time.sleep(1)
        elif i==5:
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(delay)
            #time.sleep(1)
        elif i==6:    
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(delay)
            #time.sleep(1)
        elif i==7:    
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(delay)
            #time.sleep(1)
        if i==0:
            i=7
            continue
        i=i-1
setup1()
setup2()
def start_brush_process(power, duration, steps):
    duration=duration/2.0
    p.start(power)
    GPIO.output(r1_gnd,GPIO.HIGH)
    GPIO.output(dc1_in1,GPIO.LOW)
    GPIO.output(dc1_in2,GPIO.HIGH)
    GPIO.output(dc1_en,GPIO.HIGH)
    sleep(duration)
    for i in range(steps):
        forwardStep1()
    GPIO.output(dc1_in1,GPIO.HIGH)
    GPIO.output(dc1_in2,GPIO.LOW)
    GPIO.output(dc1_en,GPIO.HIGH)
    sleep(duration)
    GPIO.output(r1_gnd,GPIO.LOW)
    GPIO.output(dc1_en,GPIO.LOW)
    GPIO.output(dc1_in2,GPIO.LOW)
    GPIO.output(dc1_in1,GPIO.LOW)
    for i in range(steps):
        backwardStep1()
def start_spray_process(power, duration, steps):
    for i in range(steps):
       backwardStep2()
    duration=duration/2.0
    q.start(power)
    GPIO.output(r2_gnd,GPIO.HIGH)
    GPIO.output(dc2_in1,GPIO.LOW)
    GPIO.output(dc2_in2,GPIO.HIGH)
    GPIO.output(dc2_en,GPIO.HIGH)
    sleep(duration)
    for i in range(steps):
    	forwardStep2()
    GPIO.output(dc2_in1,GPIO.HIGH)
    GPIO.output(dc2_in2,GPIO.LOW)
    GPIO.output(dc2_en,GPIO.HIGH)
    sleep(duration)
    GPIO.output(r2_gnd,GPIO.LOW)
    GPIO.output(dc2_en,GPIO.LOW)
    GPIO.output(dc2_in2,GPIO.LOW)
    GPIO.output(dc2_in1,GPIO.LOW)
def start_full_process():
    start_brush_process(bpower, bduration, bsteps)
    start_spray_process(spower, sduration, ssteps)
def setTime(time_total_):
    time_total=time_total_
    return time_total
def reset_brush_process(power, duration, steps):
    global rp
    global rsteps1
    global rsteps2
    global temp1
    global temp2
    global temp3
    global temp4
    global rduration1
    global rduration2
    global b
    rp=steps*0.0204
    duration=duration/2.0
    temp1=rp
    temp2=temp1+duration
    temp3=temp2+duration
    temp4=temp3+rp
    if time_total < temp1:
       rsteps1 = int(time_total/0.0204)
       for i in range(rsteps1):
           forwardStep1()
    elif time_total < temp2:
        rduration1=time_total-rp
        p.start(power)
        GPIO.output(r1_gnd,GPIO.HIGH)
        GPIO.output(dc1_in1,GPIO.HIGH)
        GPIO.output(dc1_in2,GPIO.LOW)
        GPIO.output(dc1_en,GPIO.HIGH)
        sleep(rduration1)
        GPIO.output(r1_gnd,GPIO.LOW)
        GPIO.output(dc1_en,GPIO.LOW)
        GPIO.output(dc1_in2,GPIO.LOW)
        GPIO.output(dc1_in1,GPIO.LOW)
        for i in range(steps):
    	    forwardStep1()
    elif time_total < temp3:
        rduration2=temp3-time_total
        p.start(power)
        GPIO.output(r1_gnd,GPIO.HIGH)
        GPIO.output(dc1_in1,GPIO.HIGH)
        GPIO.output(dc1_in2,GPIO.LOW)
        GPIO.output(dc1_en,GPIO.HIGH)
        sleep(rduration2)
        GPIO.output(r1_gnd,GPIO.LOW)
        GPIO.output(dc1_en,GPIO.LOW)
        GPIO.output(dc1_in2,GPIO.LOW)
        GPIO.output(dc1_in1,GPIO.LOW)
        for i in range(steps):
    	    forwardStep1()
    elif time_total < temp4:
        rsteps2 = int((temp4-time_total)/0.0204)
        for i in range(rsteps2):
    	    forwardStep1()
    btn1ClickFunction()
def reset_brush_process1(power, duration, steps):
    global rp
    global rsteps1
    global rsteps2
    global temp1
    global temp2
    global temp3
    global temp4
    global rduration1
    global rduration2
    global b
    rp=steps*0.0204
    duration=duration/2.0
    temp1=rp
    temp2=temp1+duration
    temp3=temp2+duration
    temp4=temp3+rp
    if time_total < temp1:
       rsteps1 = int(time_total/0.0204)
       for i in range(rsteps1):
           forwardStep1()
    elif time_total < temp2:
        rduration1=time_total-rp
        p.start(power)
        GPIO.output(r1_gnd,GPIO.HIGH)
        GPIO.output(dc1_in1,GPIO.HIGH)
        GPIO.output(dc1_in2,GPIO.LOW)
        GPIO.output(dc1_en,GPIO.HIGH)
        sleep(rduration1)
        GPIO.output(r1_gnd,GPIO.LOW)
        GPIO.output(dc1_en,GPIO.LOW)
        GPIO.output(dc1_in2,GPIO.LOW)
        GPIO.output(dc1_in1,GPIO.LOW)
        for i in range(steps):
    	    forwardStep1()
    elif time_total < temp3:
        rduration2=temp3-time_total
        p.start(power)
        GPIO.output(r1_gnd,GPIO.HIGH)
        GPIO.output(dc1_in1,GPIO.HIGH)
        GPIO.output(dc1_in2,GPIO.LOW)
        GPIO.output(dc1_en,GPIO.HIGH)
        sleep(rduration2)
        GPIO.output(r1_gnd,GPIO.LOW)
        GPIO.output(dc1_en,GPIO.LOW)
        GPIO.output(dc1_in2,GPIO.LOW)
        GPIO.output(dc1_in1,GPIO.LOW)
        for i in range(steps):
    	    forwardStep1()
    elif time_total < temp4:
        rsteps2 = int((temp4-time_total)/0.0204)
        for i in range(rsteps2):
    	    forwardStep1()
    btn3ClickFunction()
def reset_spray_process(power, duration, steps):
    global rp
    global rsteps1
    global rsteps2
    global temp1
    global temp2
    global temp3
    global temp4
    global temp5
    global rduration1
    global rduration2
    global b
    rp=steps*0.0204
    duration1=duration/2.0
    duration2=duration/4.0
    temp1=rp
    temp2=temp1+duration1
    temp3=temp2+duration2
    temp4=temp3+duration1
    temp5=temp4+rp
    if time_total < temp1:
       rsteps1 = int(time_total/0.0204)
       for i in range(rsteps1):
           forwardStep2()
    elif time_total < temp2:
        rduration1=time_total-rp
        q.start(power)
        GPIO.output(r2_gnd,GPIO.HIGH)
        GPIO.output(dc2_in1,GPIO.LOW)
        GPIO.output(dc2_in2,GPIO.HIGH)
        GPIO.output(dc2_en,GPIO.HIGH)
        sleep(rduration1)
        GPIO.output(r2_gnd,GPIO.LOW)
        GPIO.output(dc2_en,GPIO.LOW)
        GPIO.output(dc2_in2,GPIO.LOW)
        GPIO.output(dc2_in1,GPIO.LOW)
        for i in range(steps):
    	    forwardStep2()
    elif time_total < temp3:
        rduration2=temp3-time_total
        q.start(power)
        GPIO.output(r2_gnd,GPIO.HIGH)
        GPIO.output(dc2_in1,GPIO.LOW)
        GPIO.output(dc2_in2,GPIO.HIGH)
        GPIO.output(dc2_en,GPIO.HIGH)
        sleep(rduration2)
        GPIO.output(dc2_in1,GPIO.LOW)
        GPIO.output(dc2_in2,GPIO.HIGH)
        GPIO.output(dc2_en,GPIO.HIGH)
        sleep(duration2)
        GPIO.output(r2_gnd,GPIO.LOW)
        GPIO.output(dc2_en,GPIO.LOW)
        GPIO.output(dc2_in2,GPIO.LOW)
        GPIO.output(dc2_in1,GPIO.LOW)
        for i in range(steps):
    	    forwardStep2()
    elif time_total < temp4:
        rduration2=temp4-time_total
        q.start(power)
        GPIO.output(r2_gnd,GPIO.HIGH)
        GPIO.output(dc2_in1,GPIO.LOW)
        GPIO.output(dc2_in2,GPIO.HIGH)
        GPIO.output(dc2_en,GPIO.HIGH)
        sleep(rduration2)
        GPIO.output(r2_gnd,GPIO.LOW)
        GPIO.output(dc2_en,GPIO.LOW)
        GPIO.output(dc2_in2,GPIO.LOW)
        GPIO.output(dc2_in1,GPIO.LOW)
        for i in range(steps):
    	    forwardStep2()
    elif time_total < temp5:
        rsteps2 = int((temp5-time_total)/0.0204)
        for i in range(rsteps2):
    	    forwardStep2()
    btn2ClickFunction()
def reset_spray_process1(power, duration, steps):
    global rp
    global rsteps1
    global rsteps2
    global temp1
    global temp2
    global temp3
    global temp4
    global temp5
    global rduration1
    global rduration2
    global b
    rp=steps*0.0204
    duration1=duration/2.0
    duration2=duration/4.0
    temp1=rp
    temp2=temp1+duration1
    temp3=temp2+duration2
    temp4=temp3+duration1
    temp5=temp4+rp
    if time_total < temp1:
       rsteps1 = int(time_total/0.0204)
       for i in range(rsteps1):
           forwardStep2()
    elif time_total < temp2:
        rduration1=time_total-rp
        q.start(power)
        GPIO.output(r2_gnd,GPIO.HIGH)
        GPIO.output(dc2_in1,GPIO.LOW)
        GPIO.output(dc2_in2,GPIO.HIGH)
        GPIO.output(dc2_en,GPIO.HIGH)
        sleep(rduration1)
        GPIO.output(r2_gnd,GPIO.LOW)
        GPIO.output(dc2_en,GPIO.LOW)
        GPIO.output(dc2_in2,GPIO.LOW)
        GPIO.output(dc2_in1,GPIO.LOW)
        for i in range(steps):
    	    forwardStep2()
    elif time_total < temp3:
        rduration2=temp3-time_total
        q.start(power)
        GPIO.output(r2_gnd,GPIO.HIGH)
        GPIO.output(dc2_in1,GPIO.LOW)
        GPIO.output(dc2_in2,GPIO.HIGH)
        GPIO.output(dc2_en,GPIO.HIGH)
        sleep(rduration2)
        GPIO.output(dc2_in1,GPIO.LOW)
        GPIO.output(dc2_in2,GPIO.HIGH)
        GPIO.output(dc2_en,GPIO.HIGH)
        sleep(duration2)
        GPIO.output(r2_gnd,GPIO.LOW)
        GPIO.output(dc2_en,GPIO.LOW)
        GPIO.output(dc2_in2,GPIO.LOW)
        GPIO.output(dc2_in1,GPIO.LOW)
        for i in range(steps):
    	    forwardStep2()
    elif time_total < temp4:
        rduration2=temp4-time_total
        q.start(power)
        GPIO.output(r2_gnd,GPIO.HIGH)
        GPIO.output(dc2_in1,GPIO.LOW)
        GPIO.output(dc2_in2,GPIO.HIGH)
        GPIO.output(dc2_en,GPIO.HIGH)
        sleep(rduration2)
        GPIO.output(r2_gnd,GPIO.LOW)
        GPIO.output(dc2_en,GPIO.LOW)
        GPIO.output(dc2_in2,GPIO.LOW)
        GPIO.output(dc2_in1,GPIO.LOW)
        for i in range(steps):
    	    forwardStep2()
    elif time_total < temp5:
        rsteps2 = int((temp5-time_total)/0.0204)
        for i in range(rsteps2):
    	    forwardStep2()
    btn3ClickFunction()
def reset_full_process(duration1,steps1,duration2,steps2):
    global temp6
    global temp7
    global total
    global time_total
    temp6=steps1*0.0204
    temp7=steps2*0.0204
    total=temp6+temp6+duration1
    if time_total < total:
       reset_brush_process1(bpower,bduration,bsteps)
    else:
       total=temp7+temp7+duration2
       time_total=time_total-total
       reset_spray_process1(spower,sduration,ssteps)
def verify(duration,steps):
    global start_time2
    global stop_time2
    global time_total2
    global temp
    global total
    stop_time2=time.time()
    time_total2=stop_time2-start_time2
    temp=steps*0.0204
    total=temp+temp+duration
    if time_total2 < total:
        temp=total-time_total2
        sleep(temp)
        start_time2=0.0
        stop_time2=0.0
        time_total2=0.0
        return
    else:
        start_time2=0.0
        stop_time2=0.0
        time_total2=0.0
        return
def verify_full(duration1,steps1,duration2,steps2):
    global start_time2
    global stop_time2
    global time_total2
    global temp
    global temp6
    global temp7
    global total
    stop_time2=time.time()
    time_total2=stop_time2-start_time2
    temp6=steps1*0.0204
    temp7=steps2*0.0204
    total=temp6+temp6+temp7+temp7+duration1+duration2
    if time_total2 < total:
        temp=total-time_total2
        sleep(temp)
        start_time2=0.0
        stop_time2=0.0
        time_total2=0.0
        return
    else:
        start_time2=0.0
        stop_time2=0.0
        time_total2=0.0
        return
def exit():
    GPIO.output(dc1_in1,GPIO.LOW)
    GPIO.output(dc1_in2,GPIO.LOW)
    GPIO.output(dc1_en,GPIO.LOW)
    GPIO.output(dc2_in1,GPIO.LOW)
    GPIO.output(dc2_in2,GPIO.LOW)
    GPIO.output(dc2_en,GPIO.LOW)
    GPIO.output(s1_in1, GPIO.LOW)
    GPIO.output(s1_in2, GPIO.LOW)
    GPIO.output(s1_in3, GPIO.LOW)
    GPIO.output(s1_en, GPIO.LOW)
    GPIO.output(s2_in1, GPIO.LOW)
    GPIO.output(s2_in2, GPIO.LOW)
    GPIO.output(s2_in3, GPIO.LOW)
    GPIO.output(s2_en, GPIO.LOW)
    GPIO.output(r1_gnd,GPIO.LOW)
    GPIO.output(r2_gnd,GPIO.LOW)
############## GUI #####################
def btn1ClickFunction():
   root3.deiconify()
   root3.get_themes()
   root3.set_theme("radiance")  
   root3.attributes('-fullscreen', True)
   root3.title('Brush Process')
   ttk.Button(root3,text='Start Process',state=NORMAL, command=lambda:[root3.withdraw(),btn1AClickFunction()]).place(x=85, y=279)
   ttk.Button(root3,text='Stop Process',state=DISABLED, command=lambda:[root3.withdraw(),btn1BClickFunction()]).place(x=330, y=279)
   ttk.Button(root3,text='Reset Process',state=DISABLED, command=lambda:[root3.withdraw(),btn1CClickFunction()]).place(x=575, y=279)
   ttk.Label(root3,text='Brush Process',font=('arial','24')).place(x=300, y=203)
   ttk.Button(root3,text='Back',state=NORMAL, command=lambda:[root3.withdraw(),home()]).place(x=635, y=29)
   root3.mainloop()
def btn1AClickFunction():
   global b
   global start_time
   global start_time2
   set_delay(bdelay)
   b = multiprocessing.Process(target = start_brush_process, args = (bpower,bduration,bsteps,))
   start_time=time.time()
   start_time2=time.time()
   b.start()
   root4.deiconify()
   root4.get_themes()
   root4.set_theme("radiance")  
   root4.attributes('-fullscreen', True)
   root4.title('Brush Process')
   ttk.Button(root4,text='Start Process',state=NORMAL, command=lambda:[verify(bduration,bsteps),root4.withdraw(),btn1AClickFunction()]).place(x=85, y=279)
   ttk.Button(root4,text='Stop Process',state=NORMAL, command=lambda:[root4.withdraw(),btn1BClickFunction()]).place(x=330, y=279)
   ttk.Button(root4,text='Reset Process',state=DISABLED, command=lambda:[root4.withdraw(),btn1CClickFunction()]).place(x=575, y=279)
   ttk.Label(root4,text='Brush Process',font=('arial','24')).place(x=300, y=203)
   ttk.Button(root4,text='Back',state=NORMAL, command=lambda:[verify(bduration,bsteps),root4.withdraw(),home()]).place(x=635, y=29)
   root4.mainloop()
def btn1BClickFunction():
   global b
   global start_time
   global stop_time
   global time_total
   stop_time=time.time()
   time_total=stop_time-start_time
   setTime(time_total)
   exit()
   b.terminate()
   b.join()
   root5.deiconify()
   root5.get_themes()
   root5.set_theme("radiance")  
   root5.attributes('-fullscreen', True)
   root5.title('Brush Process')
   ttk.Button(root5,text='Start Process',state=DISABLED, command=lambda:[root5.withdraw(),btn1AClickFunction()]).place(x=85, y=279)
   ttk.Button(root5,text='Stop Process',state=DISABLED, command=lambda:[root5.withdraw(),btn1BClickFunction()]).place(x=330, y=279)
   ttk.Button(root5,text='Reset Process',state=NORMAL, command=lambda:[btn1CClickFunction()]).place(x=575, y=279)
   ttk.Label(root5,text='Brush Process',font=('arial','24')).place(x=300, y=203)
   ttk.Button(root5,text='Back',state=DISABLED, command=lambda:[root5.withdraw(),home()]).place(x=635, y=29)
   root5.mainloop()
def btn1CClickFunction():
   reset_brush_process(bpower,bduration,bsteps)
def btn2ClickFunction():  
   root8.deiconify()
   root8.get_themes()
   root8.set_theme("radiance")  
   root8.attributes('-fullscreen', True)
   root8.title('Spray Process')
   ttk.Button(root8,text='Start Process',state=NORMAL, command=lambda:[root8.withdraw(),btn2AClickFunction()]).place(x=85, y=279)
   ttk.Button(root8,text='Stop Process',state=DISABLED, command=lambda:[root8.withdraw(),btn2BClickFunction()]).place(x=330, y=279)
   ttk.Button(root8,text='Reset Process',state=DISABLED, command=lambda:[root8.withdraw(),btn2CClickFunction()]).place(x=575, y=279)
   ttk.Label(root8,text='Spray Process',font=('arial','24')).place(x=300, y=203)
   ttk.Button(root8,text='Back',state=NORMAL, command=lambda:[root8.withdraw(),home()]).place(x=635, y=29)
   root8.mainloop()
def btn2AClickFunction():
   global s
   global start_time
   global start_time2
   set_delay(bdelay)
   s = multiprocessing.Process(target = start_spray_process, args = (spower,sduration,ssteps,))
   start_time=time.time()
   start_time2=time.time()
   s.start()
   root6.deiconify()
   root6.get_themes()
   root6.set_theme("radiance")  
   root6.attributes('-fullscreen', True)
   root6.title('Spray Process')
   ttk.Button(root6,text='Start Process',state=NORMAL, command=lambda:[verify(sduration,ssteps),root6.withdraw(),btn2AClickFunction()]).place(x=85, y=279)
   ttk.Button(root6,text='Stop Process',state=NORMAL, command=lambda:[root6.withdraw(),btn2BClickFunction()]).place(x=330, y=279)
   ttk.Button(root6,text='Reset Process',state=DISABLED, command=lambda:[root6.withdraw(),btn2CClickFunction()]).place(x=575, y=279)
   ttk.Label(root6,text='Spray Process',font=('arial','24')).place(x=300, y=203)
   ttk.Button(root6,text='Back',state=NORMAL, command=lambda:[verify(sduration,ssteps),root6.withdraw(),home()]).place(x=635, y=29)
   root6.mainloop()
def btn2BClickFunction():
   global s
   global start_time
   global stop_time
   global time_total
   stop_time=time.time()
   time_total=stop_time-start_time
   setTime(time_total)
   exit()
   s.terminate()
   s.join()
   root7.deiconify()
   root7.get_themes()
   root7.set_theme("radiance")  
   root7.attributes('-fullscreen', True)
   root7.title('Spray Process')
   ttk.Button(root7,text='Start Process',state=DISABLED, command=lambda:[root7.withdraw(),btn2AClickFunction()]).place(x=85, y=279)
   ttk.Button(root7,text='Stop Process',state=DISABLED, command=lambda:[root7.withdraw(),btn2BClickFunction()]).place(x=330, y=279)
   ttk.Button(root7,text='Reset Process',state=NORMAL, command=lambda:[btn2CClickFunction()]).place(x=575, y=279)
   ttk.Label(root7,text='Spray Process',font=('arial','24')).place(x=300, y=203)
   ttk.Button(root7,text='Back',state=DISABLED, command=lambda:[root7.withdraw(),home()]).place(x=635, y=29)
   root7.mainloop()
def btn2CClickFunction():
   reset_spray_process(spower,sduration,ssteps)
def btn3ClickFunction(): 
   root9.deiconify()
   root9.get_themes()
   root9.set_theme("radiance")  
   root9.attributes('-fullscreen', True)
   root9.title('Full Process')
   ttk.Button(root9,text='Start Process',state=NORMAL, command=lambda:[root9.withdraw(),btn3AClickFunction()]).place(x=85, y=279)
   ttk.Button(root9,text='Stop Process',state=DISABLED, command=lambda:[root9.withdraw(),btn3BClickFunction()]).place(x=330, y=279)
   ttk.Button(root9,text='Reset Process',state=DISABLED, command=lambda:[root9.withdraw(),btn3CClickFunction()]).place(x=575, y=279)
   ttk.Label(root9,text='Full Process',font=('arial','24')).place(x=300, y=203)
   ttk.Button(root9,text='Back',state=NORMAL, command=lambda:[root9.withdraw(),home()]).place(x=635, y=29)
   root9.mainloop()
def btn3AClickFunction():
   global f
   global start_time
   global start_time2
   set_delay(bdelay)
   f = multiprocessing.Process(target = start_full_process, args = ())
   start_time=time.time()
   start_time2=time.time()
   f.start()
   root10.deiconify()
   root10.get_themes()
   root10.set_theme("radiance")  
   root10.attributes('-fullscreen', True)
   root10.title('Full Process')
   ttk.Button(root10,text='Start Process',state=NORMAL, command=lambda:[verify_full(bduration,bsteps,sduration,ssteps),root10.withdraw(),btn3AClickFunction()]).place(x=85, y=279)
   ttk.Button(root10,text='Stop Process',state=NORMAL, command=lambda:[root10.withdraw(),btn3BClickFunction()]).place(x=330, y=279)
   ttk.Button(root10,text='Reset Process',state=DISABLED, command=lambda:[root10.withdraw(),btn3CClickFunction()]).place(x=575, y=279)
   ttk.Label(root10,text='Full Process',font=('arial','24')).place(x=300, y=203)
   ttk.Button(root10,text='Back',state=NORMAL, command=lambda:[verify_full(bduration,bsteps,sduration,ssteps),root10.withdraw(),home()]).place(x=635, y=29)
   root10.mainloop()
def btn3BClickFunction():
   global f
   global start_time
   global stop_time
   global time_total
   stop_time=time.time()
   time_total=stop_time-start_time
   setTime(time_total)
   exit()
   f.terminate()
   f.join()
   root11.deiconify()
   root11.get_themes()
   root11.set_theme("radiance")  
   root11.attributes('-fullscreen', True)
   root11.title('Full Process')
   ttk.Button(root11,text='Start Process',state=DISABLED, command=lambda:[root11.withdraw(),btn3AClickFunction()]).place(x=85, y=279)
   ttk.Button(root11,text='Stop Process',state=DISABLED, command=lambda:[root11.withdraw(),btn3BClickFunction()]).place(x=330, y=279)
   ttk.Button(root11,text='Reset Process',state=NORMAL, command=lambda:[btn3CClickFunction()]).place(x=575, y=279)
   ttk.Label(root11,text='Full Process',font=('arial','24')).place(x=300, y=203)
   ttk.Button(root11,text='Back',state=DISABLED, command=lambda:[root11.withdraw(),home()]).place(x=635, y=29)
   root11.mainloop()
def btn3CClickFunction():
   reset_full_process(bduration,bsteps,sduration,ssteps)
def btn4ClickFunction(): 
   root = tk.ThemedTk()
   root.get_themes()
   root.set_theme("radiance")
   root.attributes('-fullscreen', True)
   root.title('Settings')
   ttk.Button(root, text='Brush Process',command=lambda:[root.withdraw(),btn4AClickFunction(option1)]).place(x=115, y=303)
   ttk.Button(root, text='Spray Process', command=lambda:[root.withdraw(),btn4BClickFunction(option2)]).place(x=475, y=303)
   ttk.Label(root, text='Settings',font=('arial','24')).place(x=315, y=203)
   ttk.Button(root, text='Back',command=lambda:[root.withdraw(),home()]).place(x=635, y=23)
   root.mainloop()
def btn4AClickFunction(option1):
   if option1 == "true":
      root1.deiconify()
      root1.mainloop()
   else:   
      root1.deiconify()
      def getDelay(): 
         global bdelay
         if bDelay.get() == "":
            bdelay = 0.05
         else: 
            bdelay = float(bDelay.get())
      def getSteps():
         global bsteps
         if bSteps.get() == "":
            bsteps = 50.0
         else:   
            bsteps = int(bSteps.get())
      def getPower():
         global bpower
         if bPower.get() == "":
            bpower = 50
         else:
            bpower = int(bPower.get())
      def getDuration():
         global bduration
         if bDuration.get() == "":
            bduration = 5.0
         else:
            bduration = float(bDuration.get())
      root1.attributes('-fullscreen', True)
      root1.title('Brush Process Settings')
      ttk.Button(root1, text='Save', command=lambda:[root1.withdraw(),getDelay(), getSteps(), getPower(),getDuration(),option1(), home()]).place(x=215, y=403)
      ttk.Button(root1, text='Cancel', command=lambda:[root1.withdraw(),btn4ClickFunction()]).place(x=545, y=403)
      bDelay=ttk.Entry(root1)
      bDelay.insert(END, '0.05')
      bDelay.pack()
      bDelay.place(x=488, y=146)
      ttk.Label(root1, text='Enter Stepper Motor Delay: ', font=('arial', 12, 'normal')).place(x=278, y=146)
      bSteps=ttk.Entry(root1)
      bSteps.insert(END, '50')
      bSteps.pack()
      bSteps.place(x=488, y=206)
      ttk.Label(root1, text='Enter Stepper Motor Steps: ', font=('arial', 12, 'normal')).place(x=278, y=206)
      bPower=ttk.Entry(root1)
      bPower.insert(END, '50')
      bPower.pack()
      bPower.place(x=488, y=266)
      ttk.Label(root1, text='Enter DC Motor Power: ', font=('arial', 12, 'normal')).place(x=308, y=266)
      bDuration=ttk.Entry(root1)
      bDuration.insert(END, '5.0')
      bDuration.pack()
      bDuration.place(x=488, y=326)
      ttk.Label(root1, text='Enter DC Motor Duration: ',font=('arial', 12, 'normal')).place(x=288, y=326)
      ttk.Label(root1, text='Brush Process', font=('arial', 30, 'normal')).place(x=318, y=56)  
      root1.mainloop()
def btn4BClickFunction(option2):
   if option2 == "true":
      root2.deiconify()
      root2.mainloop()
   else:
      root2.deiconify()
      def getDelay(): 
         global sdelay
         if sDelay.get() == "":
            sdelay = 0.05
         else:
            sdelay = float(sDelay.get())
      def getSteps():
         global ssteps
         if sSteps.get() == "":
            ssteps = 50
         else:
            ssteps = int(sSteps.get())
      def getPower():
         global spower
         if sPower.get() == "":
            spower = 50
         else:
            spower = int(sPower.get())
      def getDuration():
         global sduration
         if sDuration.get() == "":
            sduration = 5.0
         else:
            sduration = float(sDuration.get())
      root2.attributes('-fullscreen', True)
      root2.title('Spray Process Settings')
      ttk.Button(root2, text='Save', command=lambda:[root2.withdraw(),getDelay(), getSteps(), getPower(),getDuration(),option2(), home()]).place(x=215, y=403)
      ttk.Button(root2, text='Cancel', command=lambda:[root2.withdraw(),btn4ClickFunction()]).place(x=545, y=403)
      sDelay=ttk.Entry(root2)
      sDelay.insert(END, '0.05')
      sDelay.pack()
      sDelay.place(x=488, y=146)
      ttk.Label(root2, text='Enter Stepper Motor Delay: ', font=('arial', 12, 'normal')).place(x=278, y=146)
      sSteps=ttk.Entry(root2)
      sSteps.insert(END, '50')
      sSteps.pack()
      sSteps.place(x=488, y=206)
      ttk.Label(root2, text='Enter Stepper Motor Steps: ', font=('arial', 12, 'normal')).place(x=278, y=206)
      sPower=ttk.Entry(root2)
      sPower.insert(END, '50')
      sPower.pack()
      sPower.place(x=488, y=266)
      ttk.Label(root2, text='Enter DC Motor Power: ', font=('arial', 12, 'normal')).place(x=308, y=266)
      sDuration=ttk.Entry(root2)
      sDuration.insert(END, '5.0')
      sDuration.pack()
      sDuration.place(x=488, y=326)
      ttk.Label(root2, text='Enter DC Motor Duration: ', font=('arial', 12, 'normal')).place(x=288, y=326)
      ttk.Label(root2, text='Spray Process',  font=('arial', 30, 'normal')).place(x=318, y=56)      
      root2.mainloop()
def option1():
   global option1
   option1 = "true"
def option2():
   global option2
   option2 = "true"
def home():
   root.deiconify()
   root.attributes('-fullscreen', True)
   root.title('Automation')
   ttk.Button(root, text='Brush Process', command=lambda:[root.withdraw(),btn1ClickFunction()]).place(x=330, y=303)
   ttk.Button(root, text='Spray Process',  command=lambda:[root.withdraw(),btn2ClickFunction()]).place(x=575, y=303)
   ttk.Button(root, text='Full Process',  command=lambda:[root.withdraw(),btn3ClickFunction()]).place(x=85, y=303)
   ttk.Label(root, text='Select The Process',font=('arial','24')).place(x=260, y=203)
   ttk.Button(root, text='Settings', command=lambda:[root.withdraw(),btn4ClickFunction()]).place(x=635, y=23)
   ttk.Button(root, text='Exit', command=lambda:[root.withdraw(),quit()]).place(x=25, y=23)
   root.mainloop()
def main():
	home()
if name =='main':
	main()