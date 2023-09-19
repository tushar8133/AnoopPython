# AnritsuShockline-MS46122B
import socket
import time

def connectSocket():
    global vna
    vna = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = "127.0.0.1"
    port = 5001
    vna.connect((ip, port))
    print("SOCKET CONNECTED AT", ip , port)

def sendData(raw):
    cmd = raw.rstrip('\\n') + '\n'
    vna.send(cmd.encode())

def recvData():
    print("\n----------- MACHINE OUTPUT -----------")
    print(vna.recv(2056).decode().rstrip('\n'))
    print("--------------------------------------\n")

def enterCommand():
    user = input("Enter command: ")
    sendData(user)
    recvData()

def cmdIDN():
    sendData("*IDN?")
    recvData()

def preset():
    print("Preset in progress. Please wait...")
    sendData(":SYSTem:PRESet")
    time.sleep(3)
    print("Preset Complete!")

def setMarker():
    print("SET MARKER")
    freq = input("Enter frequency: ")
    sendData("CALC1:PAR3:MARK2:ACT")
    sendData("CALC1:PAR3:MARK2:X "+freq+"E9")
    sendData("CALC1:PAR3:MARK2:X?")
    recvData()

def loopCommands():
    while True:
        enterCommand()

def chooseOptions():
    print(
'''
***** Choose Command Number *****
1: *IDN?
2: PRESET
3: SET MARKER
4: SEND COMMAND
5: LOOP COMMANDS
''')
    choice = input('Enter your choice: ')
    match int(choice):
        case 1: cmdIDN()
        case 2: preset()
        case 3: setMarker()
        case 4: enterCommand()
        case 5: loopCommands()
        case _: print("Wrong input!")
    time.sleep(3)

connectSocket()
while True: chooseOptions()
