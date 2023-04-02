from telnetlib import Telnet

debug_enable = True
telnet_enable = False

if telnet_enable:
    tn = Telnet('localhost', 23)

def cmd(command):
    if telnet_enable:
        global tn
    if debug_enable:
        print("run cmd(command):")
        print("command = " + repr(command))
    formatted_command = str(command + "\n")
    if debug_enable:
        print("formatted_command = " + repr(formatted_command))
    if telnet_enable:
        tn.write(bytes(formatted_command, "utf-8"))
        print("cmd(command) done")

def cancel():
    if debug_enable:
        print("run cancel():")
    if telnet_enable:
        global tn
        tn.write('\x03')
    print("cancel() done")

cmd("test")
cancel()

print("master.py done")
