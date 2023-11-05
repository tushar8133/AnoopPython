import socket
import time
import tkinter as tk
from tkinter import scrolledtext

def connectSocket():
    global vna
    vna = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = "127.0.0.1"
    port = 5001
    vna.connect((ip, port))
    display("SOCKET CONNECTED AT, " + str(ip) + ", " + str(port))

def sendData(raw):
    try:
        cmd = raw.rstrip('\\n') + '\n'
        vna.send(cmd.encode())
    except:
        display("Data could not be sent!")

def recvData():
    try:
        vna.settimeout(2)
        output = vna.recv(2056).decode().rstrip('\n')
        display(output)
    except:
        display("Nothing received!")

def middleInput():
    display(234)

def enterCommand():
    user = takeInput()
    sendData(user)
    recvData()

def cmdIDN():
    sendData("*IDN?")
    recvData()

def preset():
    display("Preset in progress. Please wait...")
    sendData(":SYSTem:PRESet")
    time.sleep(3)
    display("Preset Complete!")

def setMarker():
    display("SET MARKER")
    display("Enter Frequency [2.2]")
    freq = takeInput()
    sendData("CALC1:PAR3:MARK2:ACT")
    sendData("CALC1:PAR3:MARK2:X "+freq+"E9")
    sendData("CALC1:PAR3:MARK2:X?")
    recvData()
  
def Qmeasure():
    display("Q Measurement")
    sendData("CALC1:PAR1:DEF S21")
    time.sleep(.5)
    sendData("CALC1:ALT:TRAC:NAM:STAT ON")
    sendData(':CALC1:ALT:TRAC:NAMe "QMeasurement"')
    time.sleep(.25)
    sendData("CALC1:PAR1:MARK1:ACT")
    sendData("CALC1:MARK:SEA:TRACK ON")
    sendData("CALC1:MARK:SEA MAX")
    sendData("CALC1:MARK:SEA:BAND ON")
    sendData("CALC1:MARK:SEA:BAND:DEF 3.0")
    sendData("DISP:WIND1:TRAC1:SIZ MAX")
    sendData("CALC1:MARK:SEA:BAND:DATA?")
    recvData()
    time.sleep(2)
    sendData("CALC1:MARK:X?")
    #sendData("DISP:WIND1:TRAC1:SIZ NORM")
    recvData()
    time.sleep(.5)
    sendData("CALC1:PAR1:DEF S11")
    sendData("CALC1:MARK:SEA:BAND OFF")
    sendData("CALC1:MARK:OFF")
    sendData("CALC1:ALT:TRAC:NAM:STAT OFF")
    time.sleep(.25)
    sendData("DISP:WIND1:TRAC1:SIZ NORM")
    sendData("RTL")


root = tk.Tk()
root.title("Anritsu Shockline VNA Automation")
width=600
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
userInput = tk.IntVar()

tkIdn=tk.Button(root)
tkIdn["text"] = "*IDN?"
tkIdn.place(x=30,y=30,width=150,height=30)
tkIdn["command"] = cmdIDN

tkPreset=tk.Button(root)
tkPreset["text"] = "PRESET"
tkPreset.place(x=200,y=30,width=150,height=30)
tkPreset["command"] = preset

tkMarker=tk.Button(root)
tkMarker["text"] = "SET MARKER"
tkMarker.place(x=370,y=30,width=150,height=30)
tkMarker["command"] = setMarker

tkQmeasure=tk.Button(root)
tkQmeasure["text"] = "Q Measurement"
tkQmeasure.place(x=30,y=80,width=150,height=30)
tkQmeasure["command"] = Qmeasure

tkCustomCmd=tk.Button(root)
tkCustomCmd["text"] = "CUSTOM COMMAND"
tkCustomCmd.place(x=200,y=80,width=150,height=30)
tkCustomCmd["command"] = enterCommand

tkEntry=tk.Entry(root)
tkEntry["borderwidth"] = "1px"
tkEntry["fg"] = "#333333"
tkEntry["justify"] = "left"
tkEntry["text"] = ""
tkEntry.place(x=30,y=-100,width=450,height=30)

tkSend=tk.Button(root)
tkSend["text"] = "SEND"
tkSend.place(x=500,y=-100,width=66,height=30)
tkSend["command"] = lambda: userInput.set(1)

tkDisplay = scrolledtext.ScrolledText(root, wrap = tk.WORD, width = 65, height = 18)
tkDisplay.grid(column = 500, pady = 130, padx = 30)

def display(x):
    tkDisplay.insert(tk.INSERT, "\n" + "-"*65 + "\n")
    tkDisplay.insert(tk.INSERT, x)
    tkDisplay.yview_pickplace("end")

def takeInput():
    tkEntry.place(x=30,y=450,width=450,height=30)
    tkSend.place(x=500,y=450,width=66,height=30)
    # tkEntry.set = ""
    tkEntry.delete(0, 'end')
    tkSend.wait_variable(userInput)
    tkEntry.place(x=30,y=-100,width=450,height=30)
    tkSend.place(x=500,y=-100,width=66,height=30)
    return tkEntry.get()

connectSocket()
root.mainloop()
