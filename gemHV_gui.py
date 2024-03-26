import tkinter as tk
from tkinter import *
import os
import setHV

layer=0
hv=0

def setHVbb0():
    layer=0
    hv=float(bb0inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)

def setHVbb1():
    layer=1
    hv=float(bb1inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVbb2():
    layer=2
    hv=float(bb2inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVbb3():
    layer=3
    hv=float(bb3inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVbb4():
    layer=4
    hv=float(bb4inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVbb5():
    layer=5
    hv=float(bb5inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVsbs0():
    layer=6
    hv=float(sbs0inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVsbs1():
    layer=7
    hv=float(sbs1inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVsbs2():
    layer=8
    hv=float(sbs2inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVsbs3():
    layer=9
    hv=float(sbs3inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVsbs4():
    layer=10
    hv=float(sbs4inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVsbs5():
    layer=11
    hv=float(sbs5inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVsbs6():
    layer=12
    hv=float(sbs6inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)

def setHVsbs7():
    layer=13
    hv=float(sbs7inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVsbs8():
    layer=14
    hv=float(sbs8inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVsbs9():
    layer=15
    hv=float(sbs9inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVsbs10():
    layer=16
    hv=float(sbs10inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVsbs11():
    layer=17
    hv=float(sbs11inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVsbs12():
    layer=18
    hv=float(sbs12inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVsbs13():
    layer=19
    hv=float(sbs13inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVsbs14():
    layer=20
    hv=float(sbs14inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVsbs15():
    layer=21
    hv=float(sbs15inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVsbs16():
    layer=22
    hv=float(sbs16inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVsbs17():
    layer=23
    hv=float(sbs17inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
def setHVsbs18():
    layer=24
    hv=float(sbs18inp.get(1.0,"end-1c"))
    itrip=float(setitripinp.get(1.0,"end-1c"))
    itripover=float(setitripoverinp.get(1.0,"end-1c"))
    niter=float(setiterinp.get(1.0,"end-1c"))
    setHV.setHVch(layer,hv,itrip,itripover,niter)
    
window=tk.Tk()
window.geometry('975x680')
label1=tk.Label(text="BigBite HV:", fg='black',font=("Arial",12))
label2=tk.Label(text="Layer, type, module:", fg='black',font=("Arial",10))
bb0=tk.Label(text="0,  UV  :", fg='black',font=("Arial",10))
bb0inp=tk.Text(window, height=1, width=20)
bb0btn=tk.Button(window,text="Set",command=setHVbb0)
bb1=tk.Label(text="1,  UV  :", fg='black',font=("Arial",10))
bb1inp=tk.Text(window, height=1, width=20)
bb1btn=tk.Button(window,text="Set",command=setHVbb1)
bb2=tk.Label(text="2,  UV  :", fg='black',font=("Arial",10))
bb2inp=tk.Text(window, height=1, width=20)
bb2btn=tk.Button(window,text="Set",command=setHVbb2)
bb3=tk.Label(text="3,  UV  :", fg='black',font=("Arial",10))
bb3inp=tk.Text(window, height=1, width=20)
bb3btn=tk.Button(window,text="Set",command=setHVbb3)
bb4=tk.Label(text="4,  XY,  M01:", fg='black',font=("Arial",10))
bb4inp=tk.Text(window, height=1, width=20)
bb4btn=tk.Button(window,text="Set",command=setHVbb4)
bb5=tk.Label(text="5,  XY,  M23:", fg='black',font=("Arial",10))
bb5inp=tk.Text(window, height=1, width=20)
bb5btn=tk.Button(window,text="Set",command=setHVbb5)

label1.place(x=10,y=10)
label2.place(x=15,y=30)
bb0.place(x=15,y=70)
bb0inp.place(x=120,y=70)
bb0btn.place(x=280,y=70)
bb1.place(x=15,y=110)
bb1inp.place(x=120,y=110)
bb1btn.place(x=280,y=110)
bb2.place(x=15,y=150)
bb2inp.place(x=120,y=150)
bb2btn.place(x=280,y=150)
bb3.place(x=15,y=190)
bb3inp.place(x=120,y=190)
bb3btn.place(x=280,y=190)
bb4.place(x=15,y=230)
bb4inp.place(x=120,y=230)
bb4btn.place(x=280,y=230)
bb5.place(x=15,y=270)
bb5inp.place(x=120,y=270)
bb5btn.place(x=280,y=270)


label3=tk.Label(text="SBS HV:", fg='black',font=("Arial",12))
label4=tk.Label(text="Type, layer (L) & modules (M):", fg='black',font=("Arial",10))
label5=tk.Label(text="SBS HV (cont):", fg='black',font=("Arial",12))
label6=tk.Label(text="Type, layer (L) & modules (M):", fg='black',font=("Arial",10))
sbs0=tk.Label(text="XW, L0:", fg='black',font=("Arial",10))
sbs0inp=tk.Text(window, height=1, width=20)
sbs0btn=tk.Button(window,text="Set",command=setHVsbs0)
sbs1=tk.Label(text="XW, L1:", fg='black',font=("Arial",10))
sbs1inp=tk.Text(window, height=1, width=20)
sbs1btn=tk.Button(window,text="Set",command=setHVsbs1)
sbs2=tk.Label(text="XY, L2M23:", fg='black',font=("Arial",10))
sbs2inp=tk.Text(window, height=1, width=20)
sbs2btn=tk.Button(window,text="Set",command=setHVsbs2)
sbs3=tk.Label(text="XY, L3M01:", fg='black',font=("Arial",10))
sbs3inp=tk.Text(window, height=1, width=20)
sbs3btn=tk.Button(window,text="Set",command=setHVsbs3)
sbs4=tk.Label(text="XY, L3M2L2M0:", fg='black',font=("Arial",10))
sbs4inp=tk.Text(window, height=1, width=20)
sbs4btn=tk.Button(window,text="Set",command=setHVsbs4)
sbs5=tk.Label(text="XY, L5M1L4M3:", fg='black',font=("Arial",10))
sbs5inp=tk.Text(window, height=1, width=20)
sbs5btn=tk.Button(window,text="Set",command=setHVsbs5)
sbs6=tk.Label(text="XY, L5M1L4M3:", fg='black',font=("Arial",10))
sbs6inp=tk.Text(window, height=1, width=20)
sbs6btn=tk.Button(window,text="Set",command=setHVsbs6)
sbs7=tk.Label(text="XY, L6M01:", fg='black',font=("Arial",10))
sbs7inp=tk.Text(window, height=1, width=20)
sbs7btn=tk.Button(window,text="Set",command=setHVsbs7)
sbs8=tk.Label(text="XY, L7M12:", fg='black',font=("Arial",10))
sbs8inp=tk.Text(window, height=1, width=20)
sbs8btn=tk.Button(window,text="Set",command=setHVsbs8)
sbs9=tk.Label(text="XY, L9M23:", fg='black',font=("Arial",10))
sbs9inp=tk.Text(window, height=1, width=20)
sbs9btn=tk.Button(window,text="Set",command=setHVsbs9)
sbs10=tk.Label(text="XY, L8M01:", fg='black',font=("Arial",10))
sbs10inp=tk.Text(window, height=1, width=20)
sbs10btn=tk.Button(window,text="Set",command=setHVsbs10)
sbs11=tk.Label(text="XY, L8M23:", fg='black',font=("Arial",10))
sbs11inp=tk.Text(window, height=1, width=20)
sbs11btn=tk.Button(window,text="Set",command=setHVsbs11)
sbs12=tk.Label(text="XY, L9M01:", fg='black',font=("Arial",10))
sbs12inp=tk.Text(window, height=1, width=20)
sbs12btn=tk.Button(window,text="Set",command=setHVsbs12)
sbs13=tk.Label(text="XY, L3M3L2M1:", fg='black',font=("Arial",10))
sbs13inp=tk.Text(window, height=1, width=20)
sbs13btn=tk.Button(window,text="Set",command=setHVsbs13)
sbs14=tk.Label(text="XY, L4M01:", fg='black',font=("Arial",10))
sbs14inp=tk.Text(window, height=1, width=20)
sbs14btn=tk.Button(window,text="Set",command=setHVsbs14)
sbs15=tk.Label(text="XY, L5M0L4M2:", fg='black',font=("Arial",10))
sbs15inp=tk.Text(window, height=1, width=20)
sbs15btn=tk.Button(window,text="Set",command=setHVsbs15)
sbs16=tk.Label(text="XY, L5M23:", fg='black',font=("Arial",10))
sbs16inp=tk.Text(window, height=1, width=20)
sbs16btn=tk.Button(window,text="Set",command=setHVsbs16)
sbs17=tk.Label(text="XY, L6M23:", fg='black',font=("Arial",10))
sbs17inp=tk.Text(window, height=1, width=20)
sbs17btn=tk.Button(window,text="Set",command=setHVsbs17)
sbs18=tk.Label(text="XY, L7M03:", fg='black',font=("Arial",10))
sbs18inp=tk.Text(window, height=1, width=20)
sbs18btn=tk.Button(window,text="Set",command=setHVsbs18)
label3.place(x=10,y=310)
label4.place(x=15,y=330)
label5.place(x=400,y=10)
label6.place(x=415,y=30)
sbs0.place(x=415,y=70)
sbs0inp.place(x=520,y=70)
sbs0btn.place(x=680,y=70)
sbs1.place(x=415,y=110)
sbs1inp.place(x=520,y=110)
sbs1btn.place(x=680,y=110)
sbs2.place(x=415,y=150)
sbs2inp.place(x=520,y=150)
sbs2btn.place(x=680,y=150)
sbs3.place(x=415,y=190)
sbs3inp.place(x=520,y=190)
sbs3btn.place(x=680,y=190)
sbs4.place(x=415,y=230)
sbs4inp.place(x=520,y=230)
sbs4btn.place(x=680,y=230)
sbs5.place(x=415,y=270)
sbs5inp.place(x=520,y=270)
sbs5btn.place(x=680,y=270)
sbs6.place(x=415,y=310)
sbs6inp.place(x=520,y=310)
sbs6btn.place(x=680,y=310)
sbs7.place(x=415,y=350)
sbs7inp.place(x=520,y=350)
sbs7btn.place(x=680,y=350)
sbs8.place(x=415,y=390)
sbs8inp.place(x=520,y=390)
sbs8btn.place(x=680,y=390)
sbs9.place(x=415,y=430)
sbs9inp.place(x=520,y=430)
sbs9btn.place(x=680,y=430)
sbs10.place(x=415,y=470)
sbs10inp.place(x=520,y=470)
sbs10btn.place(x=680,y=470)
sbs11.place(x=415,y=510)
sbs11inp.place(x=520,y=510)
sbs11btn.place(x=680,y=510)
sbs12.place(x=415,y=550)
sbs12inp.place(x=520,y=550)
sbs12btn.place(x=680,y=550)
sbs13.place(x=15,y=370)
sbs13inp.place(x=120,y=370)
sbs13btn.place(x=280,y=370)
sbs14.place(x=15,y=410)
sbs14inp.place(x=120,y=410)
sbs14btn.place(x=280,y=410)
sbs15.place(x=15,y=450)
sbs15inp.place(x=120,y=450)
sbs15btn.place(x=280,y=450)
sbs16.place(x=15,y=490)
sbs16inp.place(x=120,y=490)
sbs16btn.place(x=280,y=490)
sbs17.place(x=15,y=530)
sbs17inp.place(x=120,y=530)
sbs17btn.place(x=280,y=530)
sbs18.place(x=15,y=570)
sbs18inp.place(x=120,y=570)
sbs18btn.place(x=280,y=570)

setitrip=tk.Label(text="Set trip limit? 0 to disable", fg='black',font=("Arial",10))
setitripinp=tk.Text(window, height=1, width=20)
setitrip.place(x=800,y=200)
setitripinp.place(x=800,y=230)
setitripover=tk.Label(text="Trip buffer [uA]:", fg='black',font=("Arial",10))
setitripoverinp=tk.Text(window, height=1, width=20)
setitripover.place(x=800,y=300)
setitripoverinp.place(x=800,y=330)
setiter=tk.Label(text="Iterate for V drop? 0 to disable", fg='black',font=("Arial",10))
setiterinp=tk.Text(window, height=1, width=20)
setiter.place(x=800,y=400)
setiterinp.place(x=800,y=430)

window.mainloop()
