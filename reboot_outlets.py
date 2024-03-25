import sys
import pexpect
import telnetlib
import time

outlet_type=1 # 1/2 = less/more commands (see below)

if len(sys.argv) < 3:
    print ('\nUsage:')
    print ('reboot.py <crate hostname> <outlet number> <outlet type>\n')
elif len(sys.argv) == 4:
    outlet_type = int(sys.argv[3])
    if outlet_type != 1 and outlet_type != 2 and outlet_type != 3:
        print("outlet_type must be 1, 2, or 3")
        sys.exit(1)

HOST=str(sys.argv[1])
outlet_num=str(sys.argv[2])
user='hlauser'
pw='hlauser'


tn=telnetlib.Telnet(HOST)

#credentials
tn.read_until(b'User Name : ')
tn.write(user.encode('utf-8')+b"\r\n")
tn.read_until(b'Password  : ')
tn.write(pw.encode('utf-8')+b"\r\n")

#This type of outlet needs one command to reboot
if outlet_type == 1:
    #send command
    resp=tn.read_until(b"apc>",timeout=5)
    tn.write(('olReboot ' + outlet_num).encode() + b"\r\n")

#This type of outlet needs multiple commands to reboot
if outlet_type == 2:
    #send command
    resp=tn.read_until(b">",timeout=5)
    tn.write(b'1\r\n')#device manager
    resp=tn.read_until(b">",timeout=5)
    tn.write(outlet_num.encode() + b"\r\n")#outlet number
    resp=tn.read_until(b">",timeout=5)
    tn.write(b'3\r\n')#immediate reboot
    time.sleep(1)
    tn.write(b'YES\r\n')#confirm
    time.sleep(1)
    tn.write(b'\r\n')#enter to continue

#This type of outlet needs multiple commands to reboot
if outlet_type == 3:
    #send command
    resp=tn.read_until(b">",timeout=5)
    tn.write(b'1\r\n')#device manager
    resp=tn.read_until(b">",timeout=5)
    tn.write(b'2\r\n')#outlet management
    resp=tn.read_until(b">",timeout=5)
    tn.write(b'1\r\n')#outlet control/configuration
    resp=tn.read_until(b">",timeout=5)
    tn.write(outlet_num.encode() + b"\r\n")#outlet number
    resp=tn.read_until(b">",timeout=5)
    tn.write(b'1\r\n')#control outlet
    resp=tn.read_until(b">",timeout=5)
    tn.write(b'3\r\n')#immediate reboot
    time.sleep(1)
    tn.write(b'YES\r\n')#confirm
    time.sleep(1)
    tn.write(b'\r\n')#enter to continue


print('***Rebooting***')
tn.close()

