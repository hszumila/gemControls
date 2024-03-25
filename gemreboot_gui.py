import tkinter as tk
from tkinter import *
import os

def rebootBB():
    os.system("reboot_scripts/reboot_all.sh BB")

def rebootSBS():
    os.system("reboot_scripts/reboot_all.sh SBS")

def reboot_sbsvtp3():
    os.system("reboot_scripts/reboot_vxs.sh hallavme12")

def reboot_sbsvtp2():
    os.system("reboot_scripts/reboot_vxs.sh sbsgemcrate02")

def reboot_sbsvtp4():
    os.system("reboot_scripts/reboot_vxs.sh sbsgemcrate01")

def reboot_intelbbmpd():
    os.system("reboot_scripts/reboot_outlet.sh hareboot6 7 2")

def reboot_intelbbmpd2():
    os.system("reboot_scripts/reboot_caen.sh 129.57.192.139")

def reboot_sbsvme32():
    os.system("reboot_scripts/reboot_outlet.sh prexreboot01 1 1")

def reboot_sbsvme30():
    os.system("reboot_scripts/reboot_outlet.sh prexreboot01 2 1")

def reboot_sbsvme25():
    os.system("reboot_scripts/reboot_outlet.sh prexreboot02 3 1")

def reboot_sbsvme26():
    os.system("reboot_scripts/reboot_outlet.sh prexreboot02 6 1")

def reboot_BBLV():
    os.system("reboot_scripts/reboot_outlet.sh hareboot32 5 3")

def reboot_SBSLV():
    os.system("reboot_scripts/reboot_outlet.sh prexreboot01 6 1")

def reboot_CAENHV0():
    os.system("reboot_scripts/reboot_outlet.sh prexreboot01 6 1")##change this
    
def reboot_CAENHV1():
    os.system("reboot_scripts/reboot_outlet.sh prexreboot01 6 1")##change this
    
def reboot_CAENHV2():
    os.system("reboot_scripts/reboot_outlet.sh prexreboot01 6 1")##change this
    
window=tk.Tk()

window.geometry('800x680')
#frame=gui.frame(master=window,height=500,bg="black")
#frame.pack()

label1=tk.Label(text="For the shift worker:", fg='black',font=("Arial",24))
btn1=Button(window, text='Reset BB GEMs',font=("Arial",15),bd='5',width=25,height=4,bg='orange red',fg='black',command=rebootBB)
btn2=Button(window, text='Reset SBS GEMs',font=("Arial",15),bd='5',width=25,height=4,bg='orange red',fg='black',command=rebootSBS)

label1.pack()
btn1.place(x=80,y=40)
btn2.place(x=400,y=40)

#expert buttons:
label2=tk.Label(text="\n GEM experts only:", fg='black',font=("Arial",20))
label2.place(x=280,y=175)

#VTP crates:
label3=tk.Label(text="VTP crates", fg='black',font=("Arial",12))
label3.place(x=0,y=250)
btn3=Button(window, text='(BB) sbsvtp3:vtpROC20',font=("Arial",10),bd='5',bg='cyan',fg='black',command=reboot_sbsvtp3)
btn4=Button(window, text='(SBS) sbsvtp2:sbsvtpROC24',font=("Arial",10),bd='5',bg='cyan',fg='black',command=reboot_sbsvtp2)
btn5=Button(window, text='(SBS) sbsvtp4:sbsvtpROC25',font=("Arial",10),bd='5',bg='cyan',fg='black',command=reboot_sbsvtp4)
btn3.place(x=0,y=275)
btn4.place(x=180,y=275)
btn5.place(x=390,y=275)

#MPD crates:
label4=tk.Label(text="MPD crates", fg='black',font=("Arial",12))
label4.place(x=0,y=325)
btn6=Button(window, text='(BB) Intelbbmpd',font=("Arial",10),bd='5',bg='medium purple',fg='black',command=reboot_intelbbmpd)
btn7=Button(window, text='(BB) Intelbbmpd2',font=("Arial",10),bd='5',bg='medium purple',fg='black',command=reboot_intelbbmpd2)
btn8=Button(window, text='(SBS) sbsvme32',font=("Arial",10),bd='5',bg='medium purple',fg='black',command=reboot_sbsvme32)
btn9=Button(window, text='(SBS) sbsvme30',font=("Arial",10),bd='5',bg='medium purple',fg='black',command=reboot_sbsvme30)
btn10=Button(window, text='(SBS) sbsvme25',font=("Arial",10),bd='5',bg='medium purple',fg='black',command=reboot_sbsvme25)
btn11=Button(window, text='(SBS) sbsvme26',font=("Arial",10),bd='5',bg='medium purple',fg='black',command=reboot_sbsvme26)
btn6.place(x=0,y=350)
btn7.place(x=130,y=350)
btn8.place(x=265,y=350)
btn9.place(x=400,y=350)
btn10.place(x=535,y=350)
btn11.place(x=670,y=350)

#LV:
label5=tk.Label(text="\n Low voltage", fg='black',font=("Arial",12))
label5.place(x=0,y=390)
btn11=Button(window, text='BB LV',font=("Arial",10),bd='5',bg='NavajoWhite2',fg='black',command=reboot_BBLV)
btn12=Button(window, text='SBS LV',font=("Arial",10),bd='5',bg='NavajoWhite2',fg='black',command=reboot_SBSLV)
btn11.place(x=0,y=440)
btn12.place(x=80,y=440)

#CAEN SY5527 crates
label6=tk.Label(text="\n High voltage", fg='black',font=("Arial",12))
label6.place(x=0,y=480)
btn13=Button(window, text='c0',font=("Arial",10),bd='5',bg='NavajoWhite2',fg='black',command=reboot_CAENHV0)
btn14=Button(window, text='c1',font=("Arial",10),bd='5',bg='NavajoWhite2',fg='black',command=reboot_CAENHV1)
btn15=Button(window, text='c2',font=("Arial",10),bd='5',bg='NavajoWhite2',fg='black',command=reboot_CAENHV2)
btn13.place(x=0,y=530)
btn14.place(x=80,y=530)
btn15.place(x=160,y=530)

window.mainloop()
