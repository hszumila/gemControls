import os
import time


#average the current readback over n [s]
timeavg = 3

#####################
# Some contants here:
#####################
#cur0 = [63,158,64,72,49,47,31]
diffR03 = 5.0/60.
diffR45 = 0.5/60.

#resistors [MOhms]
res = [0.85,0.45,0.85,0.5,0.85,0.55,0.85]
resTot = 0.0
for ii in range(len(res)):
    resTot += res[ii]


#############################################################
# Gets the current from the IMon and averages over some time:--not implented yet!
#############################################################
def calcCurrent(layer,timeavg):
    cur0 = []
    for jj in range(timeavg):
        if jj == 0:
            if layer==0:
                for ii in range(7): 
                    cur0.append(os.system('caget HAHV70:00:00%d:IMon' % ii))
            elif layer==1:
                for ii in range(7,10):
                    cur0.append(os.system('caget HAHV70:00:00%d:IMon' % ii))
                for ii in range(10,14):
                    cur0.append(os.system('caget HAHV70:00:0%d:IMon' % ii))
            elif layer==2:
                for ii in range(7): 
                    cur0.append(os.system('caget HAHV70:01:00%d:IMon' % ii))
            elif layer==3:
                for ii in range(7,10):
                    cur0.append(os.system('caget HAHV70:01:00%d:IMon' % ii))
                for ii in range(10,14):
                    cur0.append(os.system('caget HAHV70:01:0%d:IMon' % ii))
            elif layer==4:
                for ii in range(7): 
                    cur0.append(os.system('caget HAHV70:02:00%d:IMon' % ii))        
            elif layer==5:
                for ii in range(7,10):
                    cur0.append(os.system('caget HAHV70:02:00%d:IMon' % ii))
                for ii in range(10,14):
                    cur0.append(os.system('caget HAHV70:02:0%d:IMon' % ii))
            elif layer==6:
                for ii in range(7): 
                    cur0.append(os.system('caget HAHV71:00:00%d:IMon' % ii))        
            elif layer==7:
                for ii in range(7,10):
                    cur0.append(os.system('caget HAHV71:00:00%d:IMon' % ii))
                for ii in range(10,14):
                    cur0.append(os.system('caget HAHV71:00:0%d:IMon' % ii))
            elif layer==8:
                for ii in range(7): 
                    cur0.append(os.system('caget HAHV70:03:00%d:IMon' % ii))        
            elif layer==9:
                for ii in range(7,10):
                    cur0.append(os.system('caget HAHV70:03:00%d:IMon' % ii))
                for ii in range(10,14):
                    cur0.append(os.system('caget HAHV70:03:0%d:IMon' % ii))
            elif layer==10:
                for ii in range(7): 
                    cur0.append(os.system('caget HAHV70:04:00%d:IMon' % ii))        
            elif layer==11:
                for ii in range(7,10):
                    cur0.append(os.system('caget HAHV70:04:00%d:IMon' % ii))
                for ii in range(10,14):
                    cur0.append(os.system('caget HAHV70:04:0%d:IMon' % ii))
            elif layer==12:
                for ii in range(7): 
                    cur0.append(os.system('caget HAHV71:01:00%d:IMon' % ii))        
            elif layer==13:
                for ii in range(7,10):
                    cur0.append(os.system('caget HAHV71:01:00%d:IMon' % ii))
                for ii in range(10,14):
                    cur0.append(os.system('caget HAHV71:01:0%d:IMon' % ii))
            elif layer==14:
                for ii in range(7): 
                    cur0.append(os.system('caget HAHV72:00:00%d:IMon' % ii))        
            elif layer==15:
                for ii in range(7,10):
                    cur0.append(os.system('caget HAHV72:00:00%d:IMon' % ii))
                for ii in range(10,14):
                    cur0.append(os.system('caget HAHV72:00:0%d:IMon' % ii))
            elif layer==16:
                for ii in range(7): 
                    cur0.append(os.system('caget HAHV72:01:00%d:IMon' % ii))        
            elif layer==17:
                for ii in range(7,10):
                    cur0.append(os.system('caget HAHV72:01:00%d:IMon' % ii))
                for ii in range(10,14):
                    cur0.append(os.system('caget HAHV72:01:0%d:IMon' % ii))
            elif layer==18:
                for ii in range(7): 
                    cur0.append(os.system('caget HAHV71:02:00%d:IMon' % ii))        
            elif layer==19:
                for ii in range(7,10):
                    cur0.append(os.system('caget HAHV71:02:00%d:IMon' % ii))
                for ii in range(10,14):
                    cur0.append(os.system('caget HAHV71:02:0%d:IMon' % ii))
            elif layer==20:
                for ii in range(7): 
                    cur0.append(os.system('caget HAHV71:03:00%d:IMon' % ii))        
            elif layer==21:
                for ii in range(7,10):
                    cur0.append(os.system('caget HAHV71:03:00%d:IMon' % ii))
                for ii in range(10,14):
                    cur0.append(os.system('caget HAHV71:03:0%d:IMon' % ii))
            elif layer==22:
                for ii in range(7): 
                    cur0.append(os.system('caget HAHV71:04:00%d:IMon' % ii))        
            elif layer==23:
                for ii in range(7,10):
                    cur0.append(os.system('caget HAHV71:04:00%d:IMon' % ii))
                for ii in range(10,14):
                    cur0.append(os.system('caget HAHV71:04:0%d:IMon' % ii))
        else:
            if layer==0:
                for ii in range(7):
                    cur0[ii] += os.system('caget HAHV70:00:00%d:IMon' % ii)
            elif layer==1:
                for ii in range(7,10):
                    cur0[ii-7] += os.system('caget HAHV70:00:00%d:IMon' % ii)
                for ii in range(10,14):
                    cur0[ii-7] += os.system('caget HAHV70:00:0%d:IMon' % ii)
            elif layer==2:
                for ii in range(7): 
                    cur0[ii] += os.system('caget HAHV70:01:00%d:IMon' % ii)
            elif layer==3:
                for ii in range(7,10):
                    cur0[ii-7] += os.system('caget HAHV70:01:00%d:IMon' % ii)
                for ii in range(10,14):
                    cur0[ii-7] += os.system('caget HAHV70:01:0%d:IMon' % ii)
            elif layer==4:
                for ii in range(7): 
                    cur0[ii] += os.system('caget HAHV70:02:00%d:IMon' % ii)       
            elif layer==5:
                for ii in range(7,10):
                    cur0[ii-7] += os.system('caget HAHV70:02:00%d:IMon' % ii)
                for ii in range(10,14):
                    cur0[ii-7] += os.system('caget HAHV70:02:0%d:IMon' % ii)
            elif layer==6:
                for ii in range(7): 
                    cur0[ii] += os.system('caget HAHV71:00:00%d:IMon' % ii)        
            elif layer==7:
                for ii in range(7,10):
                    cur0[ii-7] += os.system('caget HAHV71:00:00%d:IMon' % ii)
                for ii in range(10,14):
                    cur0[ii-7] += os.system('caget HAHV71:00:0%d:IMon' % ii)
            elif layer==8:
                for ii in range(7): 
                    cur0[ii] += os.system('caget HAHV70:03:00%d:IMon' % ii)       
            elif layer==9:
                for ii in range(7,10):
                    cur0[ii-7] += os.system('caget HAHV70:03:00%d:IMon' % ii)
                for ii in range(10,14):
                    cur0[ii-7] += os.system('caget HAHV70:03:0%d:IMon' % ii)
            elif layer==10:
                for ii in range(7): 
                    cur0[ii] += os.system('caget HAHV70:04:00%d:IMon' % ii)        
            elif layer==11:
                for ii in range(7,10):
                    cur0[ii-7] += os.system('caget HAHV70:04:00%d:IMon' % ii)
                for ii in range(10,14):
                    cur0[ii-7] += os.system('caget HAHV70:04:0%d:IMon' % ii)
            elif layer==12:
                for ii in range(7): 
                    cur0[ii] += os.system('caget HAHV71:01:00%d:IMon' % ii)        
            elif layer==13:
                for ii in range(7,10):
                    cur0[ii-7] += os.system('caget HAHV71:01:00%d:IMon' % ii)
                for ii in range(10,14):
                    cur0[ii-7] += os.system('caget HAHV71:01:0%d:IMon' % ii)
            elif layer==14:
                for ii in range(7): 
                    cur0[ii] += os.system('caget HAHV72:00:00%d:IMon' % ii)       
            elif layer==15:
                for ii in range(7,10):
                    cur0[ii-7] += os.system('caget HAHV72:00:00%d:IMon' % ii)
                for ii in range(10,14):
                    cur0[ii-7] += os.system('caget HAHV72:00:0%d:IMon' % ii)
            elif layer==16:
                for ii in range(7): 
                    cur0[ii] += os.system('caget HAHV72:01:00%d:IMon' % ii)        
            elif layer==17:
                for ii in range(7,10):
                    cur0[ii-7] += os.system('caget HAHV72:01:00%d:IMon' % ii)
                for ii in range(10,14):
                    cur0[ii-7] += os.system('caget HAHV72:01:0%d:IMon' % ii)
            elif layer==18:
                for ii in range(7): 
                    cur0[ii] += os.system('caget HAHV71:02:00%d:IMon' % ii)        
            elif layer==19:
                for ii in range(7,10):
                    cur0[ii-7] += os.system('caget HAHV71:02:00%d:IMon' % ii)
                for ii in range(10,14):
                    cur0[ii-7] += os.system('caget HAHV71:02:0%d:IMon' % ii)
            elif layer==20:
                for ii in range(7): 
                    cur0[ii] += os.system('caget HAHV71:03:00%d:IMon' % ii)       
            elif layer==21:
                for ii in range(7,10):
                    cur0[ii-7] += os.system('caget HAHV71:03:00%d:IMon' % ii)
                for ii in range(10,14):
                    cur0[ii-7] += os.system('caget HAHV71:03:0%d:IMon' % ii)
            elif layer==22:
                for ii in range(7): 
                    cur0[ii] += os.system('caget HAHV71:04:00%d:IMon' % ii)        
            elif layer==23:
                for ii in range(7,10):
                    cur0[ii-7] += os.system('caget HAHV71:04:00%d:IMon' % ii)
                for ii in range(10,14):
                    cur0[ii-7] += os.system('caget HAHV71:04:0%d:IMon' % ii)
        time.sleep(1)

    for ii in timeavg:
        cur0[ii] = cur0[ii]/timeavg
    return cur0   
    
    
##########################################################################
# Intermediate calculation of the currents on the top/bottom of each foil:
##########################################################################
def calcIntCurrent(curN):
    #calc I_T1,I_B1,I_T2,I_B2,I_T3,I_B3
    iT1 = curN[5] - curN[6]
    iB1 = curN[4] - curN[5]
    iT2 = curN[3] - curN[4]
    iB2 = curN[3] - curN[2]
    iT3 = curN[1] - curN[2]
    iB3 = curN[1] - curN[0]

    intCur = [iT1,iB1,iT2,iB2,iT3,iB3]

    return intCur

#########################################################
# Calculates the voltage per channel independent of IMon:
#########################################################
def calcVch(hv):
    v0ch = []
    vNch = []
    for ii in range(len(res)):
        v0ch.append(hv*res[ii]/resTot)
    return v0ch

def setHVch(layer,hv,setitrip,itripOverhead,niter):
    v0ch = calcVch(hv)
    curN = []
    intCur = []
    if setitrip!=0 or niter!=0:
        curN = calcCurrent(layer,timeavg)
        intCur = calcIntCurrent(curN)

    #############################################################################
    # Improves the voltage per channel by reading back the current and iterating:
    # This option is only used when niter != 0
    # Ensure the beam is stable if using
    #############################################################################
    if niter > 0:
        vNch.append(v0ch[0] - intCur[5]*diffR45)
        vNch.append(v0ch[1] + intCur[5]*diffR45 + intCur[4]*diffR45)
        vNch.append(v0ch[2] - intCur[4]*diffR45 - intCur[3]*diffR03)
        vNch.append(v0ch[3] + intCur[3]*diffR03 + intCur[2]*diffR03)
        vNch.append(v0ch[4] - intCur[2]*diffR03 + intCur[1]*diffR03)
        vNch.append(v0ch[5] - intCur[1]*diffR03 + intCur[0]*diffR03)
        vNch.append(v0ch[6] - intCur[0]*diffR03)   
    
    print('')
    #print to screen the original voltage and if iterating print that one too
    if niter == 0:
        print('For layer',layer,'the set voltages are:')
        print('ch0:    ',f'{v0ch[0]:.2f}')
        print('ch1:    ',f'{v0ch[1]:.2f}')
        print('ch2:    ',f'{v0ch[2]:.2f}')
        print('ch3:    ',f'{v0ch[3]:.2f}')
        print('ch4:    ',f'{v0ch[4]:.2f}')
        print('ch5:    ',f'{v0ch[5]:.2f}')
        print('ch6:    ',f'{v0ch[6]:.2f}')
        if setitrip != 0:
            print('These are the readback currents:')
            print('Imon ch0:    ',curN[0])
            print('Imon ch1:    ',curN[1])
            print('Imon ch2:    ',curN[2])
            print('Imon ch3:    ',curN[3])
            print('Imon ch4:    ',curN[4])
            print('Imon ch5:    ',curN[5])
            print('Imon ch6:    ',curN[6])
    else:
        print('****Iterating!****')
        print('For layer',layer,'the original and iterative voltages are:')
        print('ch0:    ',f'{v0ch[0]:.2f}',', iterated ch0:    ',f'{vNch[0]:.2f}')
        print('ch1:    ',f'{v0ch[1]:.2f}',', iterated ch1:    ',f'{vNch[1]:.2f}')
        print('ch2:    ',f'{v0ch[2]:.2f}',', iterated ch2:    ',f'{vNch[2]:.2f}')
        print('ch3:    ',f'{v0ch[3]:.2f}',', iterated ch3:    ',f'{vNch[3]:.2f}')
        print('ch4:    ',f'{v0ch[4]:.2f}',', iterated ch4:    ',f'{vNch[4]:.2f}')
        print('ch5:    ',f'{v0ch[5]:.2f}',', iterated ch5:    ',f'{vNch[5]:.2f}')
        print('ch6:    ',f'{v0ch[6]:.2f}',', iterated ch6:    ',f'{vNch[6]:.2f}')
        print('This is based on the following readback currents:')
        print('Imon ch0:    ',curN[0])
        print('Imon ch1:    ',curN[1])
        print('Imon ch2:    ',curN[2])
        print('Imon ch3:    ',curN[3])
        print('Imon ch4:    ',curN[4])
        print('Imon ch5:    ',curN[5])
        print('Imon ch6:    ',curN[6])
    print('')
    reply = input('Do you wish to apply the above voltages? [y/n]')

    if reply=='y':
        #############################################################
        # Set the set voltage:
        #############################################################
        if layer==0: #UV L0
            for ii in range(7):
                os.system('caput HAHV70:00:00%d:V0Set %.2f' % (ii,v0ch[ii]))
                if setitrip !=0:
                    os.system('caput HAHV70:00:00%d:I0Set %.2f' % (ii,curN[ii]+itripOverhead))
        elif layer==1: #UV L1
            for ii in range(7,10):
                os.system('caput HAHV70:00:00%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV70:00:00%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
            for ii in range(10,14):
                os.system('caput HAHV70:00:0%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV70:00:0%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
        elif layer==2: #UV L2
            for ii in range(7): 
                os.system('caput HAHV70:01:00%d:V0Set %.2f' % (ii,v0ch[ii]))
                if setitrip !=0:
                    os.system('caput HAHV70:01:00%d:I0Set %.2f' % (ii,curN[ii]+itripOverhead))
        elif layer==3: #UV L3
            for ii in range(7,10):
                os.system('caput HAHV70:01:00%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV70:01:00%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
            for ii in range(10,14):
                os.system('caput HAHV70:01:0%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV70:01:0%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
        elif layer==4: #XY M01
            for ii in range(7): 
                os.system('caput HAHV70:02:00%d:V0Set %.2f' % (ii,v0ch[ii]))
                if setitrip !=0:
                    os.system('caput HAHV70:02:00%d:I0Set %.2f' % (ii,curN[ii]+itripOverhead))
        elif layer==5: #XY M23
            for ii in range(7,10):
                os.system('caput HAHV70:02:00%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV70:02:00%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
            for ii in range(10,14):
                os.system('caput HAHV70:02:0%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV70:02:0%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
        elif layer==6: #XW L0
            for ii in range(7): 
                os.system('caput HAHV71:00:00%d:V0Set %.2f' % (ii,v0ch[ii]))
                if setitrip !=0:
                    os.system('caput HAHV71:00:00%d:I0Set %.2f' % (ii,curN[ii]+itripOverhead))
        elif layer==7: #XW L1
            for ii in range(7,10):
                os.system('caput HAHV71:00:00%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV71:00:00%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
            for ii in range(10,14):
                os.system('caput HAHV71:00:0%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV71:00:0%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
        elif layer==8: #XY L2M23
            for ii in range(7): 
                os.system('caput HAHV70:03:00%d:V0Set %.2f' % (ii,v0ch[ii]))
                if setitrip !=0:
                    os.system('caput HAHV70:03:00%d:I0Set %.2f' % (ii,curN[ii]+itripOverhead))
        elif layer==9: #XY L3M01
            for ii in range(7,10):
                os.system('caput HAHV70:03:00%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV70:03:00%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
            for ii in range(10,14):
                os.system('caput HAHV70:03:0%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV70:03:0%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
        elif layer==10: #XY L3M2L2M0
            for ii in range(7): 
                os.system('caput HAHV70:04:00%d:V0Set %.2f' % (ii,v0ch[ii]))
                if setitrip !=0:
                    os.system('caput HAHV70:04:00%d:I0Set %.2f' % (ii,curN[ii]+itripOverhead))
        elif layer==11: #XY L5M1L4M3
            for ii in range(7,10):
                os.system('caput HAHV70:04:00%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV70:04:00%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
            for ii in range(10,14):
                os.system('caput HAHV70:04:0%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV70:04:0%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
        elif layer==12: #XY L6M01
            for ii in range(7): 
                os.system('caput HAHV71:01:00%d:V0Set %.2f' % (ii,v0ch[ii]))
                if setitrip !=0:
                    os.system('caput HAHV71:01:00%d:I0Set %.2f' % (ii,curN[ii]+itripOverhead))
        elif layer==13: #XY L7M12
            for ii in range(7,10):
                os.system('caput HAHV71:01:00%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV71:01:00%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
            for ii in range(10,14):
                os.system('caput HAHV71:01:0%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV71:01:0%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
        elif layer==14: #XY L9M23
            for ii in range(7): 
                os.system('caput HAHV72:00:00%d:V0Set %.2f' % (ii,v0ch[ii]))
                if setitrip !=0:
                    os.system('caput HAHV72:00:00%d:I0Set %.2f' % (ii,curN[ii]+itripOverhead))
        elif layer==15: #XY L8M01
            for ii in range(7,10):
                os.system('caput HAHV72:00:00%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV72:00:00%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
            for ii in range(10,14):
                os.system('caput HAHV72:00:0%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV72:00:0%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
        elif layer==16: #XY L8M23
            for ii in range(7): 
                os.system('caput HAHV72:01:00%d:V0Set %.2f' % (ii,v0ch[ii]))
                if setitrip !=0:
                    os.system('caput HAHV72:01:00%d:I0Set %.2f' % (ii,curN[ii]+itripOverhead))
        elif layer==17: #XY L9M01
            for ii in range(7,10):
                os.system('caput HAHV72:01:00%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV72:01:00%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
            for ii in range(10,14):
                os.system('caput HAHV72:01:0%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV72:01:0%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
        elif layer==18: #XY L3M3L2M1
            for ii in range(7): 
                os.system('caput HAHV71:02:00%d:V0Set %.2f' % (ii,v0ch[ii]))
                if setitrip !=0:
                    os.system('caput HAHV71:02:00%d:I0Set %.2f' % (ii,curN[ii]+itripOverhead))
        elif layer==19: #XY L4M01
            for ii in range(7,10):
                os.system('caput HAHV71:02:00%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV71:02:00%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
            for ii in range(10,14):
                os.system('caput HAHV71:02:0%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV71:02:0%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
        elif layer==20: #XY L5M0L4M2
            for ii in range(7): 
                os.system('caput HAHV71:03:00%d:V0Set %.2f' % (ii,v0ch[ii]))
                if setitrip !=0:
                    os.system('caput HAHV71:03:00%d:I0Set %.2f' % (ii,curN[ii]+itripOverhead))
        elif layer==21: #XY L5M23
            for ii in range(7,10):
                os.system('caput HAHV71:03:00%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV71:03:00%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
            for ii in range(10,14):
                os.system('caput HAHV71:03:0%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV71:03:0%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
        elif layer==22: #XY L6M23
            for ii in range(7): 
                os.system('caput HAHV71:04:00%d:V0Set %.2f' % (ii,v0ch[ii]))
                if setitrip !=0:
                    os.system('caput HAHV71:04:00%d:I0Set %.2f' % (ii,curN[ii]+itripOverhead))
        elif layer==23: #XY L7M03
            for ii in range(7,10):
                os.system('caput HAHV71:04:00%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV71:04:00%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
            for ii in range(10,14):
                os.system('caput HAHV71:04:0%d:V0Set %.2f' % (ii,v0ch[ii-7]))
                if setitrip !=0:
                    os.system('caput HAHV71:04:0%d:I0Set %.2f' % (ii,curN[ii-7]+itripOverhead))
    else:
        print('Well, ok, fine then.')
        
