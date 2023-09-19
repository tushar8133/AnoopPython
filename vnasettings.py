import tkinter as tk
from window import frame_vna_settings
from connection import connection
from log import Log

class VnaSetting:

    def __init__(self):

        self.log = Log(frame_vna_settings, { 'x':40, 'y':260, 'w':470, 'h':150 })
        
        E_StartFr=tk.Entry(frame_vna_settings)
        self.E_StartFr = E_StartFr
        E_StartFr["borderwidth"] = "1px"
        E_StartFr["fg"] = "#333333"
        E_StartFr["justify"] = "center"
        E_StartFr.place(x=140,y=150,width=70,height=25)

        L_StartFr = tk.Label(frame_vna_settings)
        L_StartFr["justify"] = "center"
        L_StartFr["text"] = "Start Fr"
        L_StartFr.place(x=70, y=150, width=70, height=25)

        E_StopFr=tk.Entry(frame_vna_settings)
        self.E_StopFr = E_StopFr
        E_StopFr["borderwidth"] = "1px"
        E_StopFr["fg"] = "#333333"
        E_StopFr["justify"] = "center"
        E_StopFr.place(x=420,y=150,width=70,height=25)

        L_StopFr=tk.Label(frame_vna_settings)
        L_StopFr["justify"] = "center"
        L_StopFr["text"] = "Stop Fr"
        L_StopFr.place(x=350,y=150,width=70,height=25)

        E_Ifbw=tk.Entry(frame_vna_settings)
        self.E_Ifbw = E_Ifbw
        E_Ifbw["borderwidth"] = "1px"
        E_Ifbw["fg"] = "#333333"
        E_Ifbw["justify"] = "center"
        E_Ifbw.place(x=140,y=200,width=70,height=25)

        L_Ifbw=tk.Label(frame_vna_settings)
        L_Ifbw["justify"] = "center"
        L_Ifbw["text"] = "IFBW"
        L_Ifbw.place(x=70,y=200,width=70,height=25)

        E_Dp=tk.Entry(frame_vna_settings)
        self.E_Dp = E_Dp
        E_Dp["borderwidth"] = "1px"
        E_Dp["fg"] = "#333333"
        E_Dp["justify"] = "center"
        E_Dp.place(x=420,y=200,width=70,height=25)

        L_Dp=tk.Label(frame_vna_settings)
        L_Dp["justify"] = "center"
        L_Dp["text"] = "Datapoint"
        L_Dp.place(x=350,y=200,width=70,height=25)

        tkVNAset = tk.Button(frame_vna_settings)
        tkVNAset["text"] = "Enter Setting"
        tkVNAset.place(x=30, y=80, width=150, height=30)
        tkVNAset["command"] = self.start


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