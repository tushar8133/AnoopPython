import tkinter as tk
from window import frame_vna_settings
from connection import connection
from log import Log
from common import setCutOffFreq
import re

class VnaSetting:

    def __init__(self):

        self.log = Log(frame_vna_settings, { 'x':65, 'y':310, 'w':485, 'h':100 })

        L_PeakFr = tk.Label(frame_vna_settings, borderwidth='1px', relief='groove')
        L_PeakFr["justify"] = "center"
        L_PeakFr.place(x=65, y=90, width=470, height=155)

        E_StartFr=tk.Entry(frame_vna_settings)
        self.E_StartFr = E_StartFr
        E_StartFr["borderwidth"] = "1px"
        E_StartFr["fg"] = "#333333"
        E_StartFr["justify"] = "center"
        E_StartFr.place(x=155, y=125, width=70, height=25)

        L_StartFr = tk.Label(frame_vna_settings, borderwidth='1px', relief='groove')
        L_StartFr["justify"] = "center"
        L_StartFr["bg"] = "#b9dcb9"
        L_StartFr["text"] = "Start Fr"
        L_StartFr.place(x=85, y=125, width=70, height=25)

        E_StopFr=tk.Entry(frame_vna_settings)
        self.E_StopFr = E_StopFr
        E_StopFr["borderwidth"] = "1px"
        E_StopFr["fg"] = "#333333"
        E_StopFr["justify"] = "center"
        E_StopFr.place(x=435, y=125, width=70, height=25)

        L_StopFr=tk.Label(frame_vna_settings, borderwidth='1px', relief='groove')
        L_StopFr["justify"] = "center"
        L_StopFr["bg"] = "#b9dcb9"
        L_StopFr["text"] = "Stop Fr"
        L_StopFr.place(x=365, y=125, width=70, height=25)

        E_Ifbw=tk.Entry(frame_vna_settings)
        self.E_Ifbw = E_Ifbw
        E_Ifbw["borderwidth"] = "1px"
        E_Ifbw["fg"] = "#333333"
        E_Ifbw["justify"] = "center"
        E_Ifbw.place(x=155, y=200, width=70, height=25)

        L_Ifbw=tk.Label(frame_vna_settings, borderwidth='1px', relief='groove')
        L_Ifbw["justify"] = "center"
        L_Ifbw["bg"] = "#b9dcb9"
        L_Ifbw["text"] = "IFBW"
        L_Ifbw.place(x=85, y=200, width=70, height=25)

        E_Dp=tk.Entry(frame_vna_settings)
        self.E_Dp = E_Dp
        E_Dp["borderwidth"] = "1px"
        E_Dp["fg"] = "#333333"
        E_Dp["justify"] = "center"
        E_Dp.place(x=435, y=200, width=70, height=25)

        L_Dp=tk.Label(frame_vna_settings, borderwidth='1px', relief='groove')
        L_Dp["justify"] = "center"
        L_Dp["bg"] = "#b9dcb9"
        L_Dp["text"] = "Datapoint"
        L_Dp.place(x=365, y=200, width=70, height=25)

        tkVNAset=tk.Button(frame_vna_settings)
        tkVNAset["text"] = "Enter Setting"
        tkVNAset.place(x=30, y=30, width=150, height=30)
        tkVNAset["command"] = self.start

        self.ddOptions = [
            "WR187 (3.95 - 5.85) GHz",
            "WR137 (5.85 - 8.20) GHz",
            "WR90 (8.20 - 12.40) GHz",
            "WR62 (12.40 - 18) GHz",
            "WR42 (18.00 - 26.50) GHz",
        ]
        self.ddValue = tk.StringVar()
        self.ddValue.set("")
        self.ddValue.trace_add('write', self.ddListener)
        ddMenu = tk.OptionMenu( frame_vna_settings , self.ddValue , *self.ddOptions )
        ddMenu.place(x=210, y=260)
    
    def now(self):
        if (self.ddValue.get() == ""):
            self.ddValue.set(self.ddOptions[2])

    def ddListener(self, *args):
        self.setCutoffAndBand(self.ddValue.get())

    def setCutoffAndBand(self, fullband):
        regex = re.compile(r"^(WR.+)\s\((?<=\()(.+)\s-\s(.+)(?=\))")
        result = re.search(regex, fullband)
        band = result[1]
        cutoff = '6.557e9'
        if (band == 'WR187'):
            cutoff = '3.153e9'
        elif (band == 'WR137'):
            cutoff = '4.301e9'
        elif (band == 'WR90'):
            cutoff = '6.557e9'
        elif (band == 'WR62'):
            cutoff = '9.488e9'
        elif (band == 'WR42'):
            cutoff = '14.051e9'
        print(">>>>>>>>>>>", band, result[2], result[3], cutoff)
        setCutOffFreq(cutoff)
        connection.send("SENS1:FREQ:STAR "+result[2]+"e9")
        connection.send("SENS1:FREQ:STOP "+result[3]+"e9")
    

    def start(self):
        self.log.text("Staring...")
        connection.send("SENS1:FREQ:STAR "+self.E_StartFr.get()+"E9")
        connection.send("SENS1:FREQ:STOP "+self.E_StopFr.get()+"E9")
        connection.send("SENS1:SWEep:POINt "+self.E_Dp.get())
        connection.send("SENS1:BWID "+self.E_Ifbw.get())
        connection.send("RTL")
        self.log.text("Done!")

vnasetting = VnaSetting()

'''
# Start Frequency
# display("Enter Start Frequency GHz)
# sf = takeInput()
sendData("SENS1:FREQ:STAR "+E_StartFr.get()+"E9")
# time.sleep(.2)
# sendData("SENS1:FREQ:STAR?")
# recvData()

#Stop Frequency
# display("Enter Stop Frequency GHz")
# sf1 = takeInput()
sendData("SENS1:FREQ:STOP "+E_StopFr.get()+"E9")
# time.sleep(.2)
# sendData("SENS1:FREQ:STOP?")
# recvData()

#Enter No. of Datapoint
# display("No of DataPoint")
# dp = takeInput()
sendData("SENS1:SWEep:POINt "+E_Dp.get())
# time.sleep(.2)
# sendData("SENS1:SWEep:POINt?")
# recvData()

#print("Enter IFBW-Default Hz")
# display("Enter IFBW")
# bw = takeInput()
sendData("SENS1:BWID "+E_Ifbw.get())
# time.sleep(.2)
# sendData("SENS1:BWID?")
sendData("RTL")
'''