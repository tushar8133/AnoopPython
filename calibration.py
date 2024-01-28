import tkinter as tk
import time
from window import frame_calibration
from connection import connection
from log import Log
from calstatus import calstatus

class Calibration:
    def __init__(self):
        self.log = Log(frame_calibration, {'x': 65, 'y': 330, 'w': 485, 'h': 100})

        L_PeakFr = tk.Label(frame_calibration, borderwidth='1px', relief='groove')
        L_PeakFr["justify"] = "center"
        L_PeakFr.place(x=72, y=80, width=165, height=130)

        L_PeakFr = tk.Label(frame_calibration, borderwidth='1px', relief='groove')
        L_PeakFr["justify"] = "center"
        L_PeakFr.place(x=352, y=80, width=165, height=130)

        L_PeakFr = tk.Label(frame_calibration, borderwidth='1px', relief='groove')
        L_PeakFr["justify"] = "center"
        L_PeakFr.place(x=72, y=225, width=445, height=40)

        btnStartCal = tk.Button(frame_calibration)
        self.btnStartCal = btnStartCal
        btnStartCal["text"] = "Start WG Cal"
        btnStartCal.place(x=30, y=30, width=150, height=30)
        btnStartCal["command"] = self.calibration

        btnOpen1 = tk.Button(frame_calibration)
        self.btnOpen1 = btnOpen1
        btnOpen1["text"] = "Port 1: 1/8 SHORT"
        btnOpen1.place(x=80, y=90, width=150, height=30)
        btnOpen1["command"] = self.P1short1_8

        btnShort1 = tk.Button(frame_calibration)
        self.btnShort1 = btnShort1
        btnShort1["text"] = "Port 1: 3/8 SHORT"
        btnShort1.place(x=80, y=130, width=150, height=30)
        btnShort1["command"] = self.P1short3_8

        btnLoad1 = tk.Button(frame_calibration)
        self.btnLoad1 = btnLoad1
        btnLoad1["text"] = "Port 1: LOAD"
        btnLoad1.place(x=80, y=170, width=150, height=30)
        btnLoad1["command"] = self.P1load

        btnOpen2 = tk.Button(frame_calibration)
        self.btnOpen2 = btnOpen2
        btnOpen2["text"] = "Port 2: 1/8 SHORT"
        btnOpen2.place(x=360, y=90, width=150, height=30)
        btnOpen2["command"] = self.P2short1_8

        btnShort2 = tk.Button(frame_calibration)
        self.btnShort2 = btnShort2
        btnShort2["text"] = "Port 2: 3/8 SHORT"
        btnShort2.place(x=360, y=130, width=150, height=30)
        btnShort2["command"] = self.P2short3_8

        btnLoad2 = tk.Button(frame_calibration)
        self.btnLoad2 = btnLoad2
        btnLoad2["text"] = "Port 2: LOAD"
        btnLoad2.place(x=360, y=170, width=150, height=30)
        btnLoad2["command"] = self.P2load

        btnCalibration = tk.Button(frame_calibration)
        self.btnCalibration = btnCalibration
        btnCalibration["text"] = "Port 1-2: THRU"
        btnCalibration.place(x=220, y=230, width=150, height=30)
        btnCalibration["command"] = self.thru

        btnApplyCal = tk.Button(frame_calibration)
        self.btnApplyCal = btnApplyCal
        btnApplyCal["text"] = "APPLY CAL "
        btnApplyCal.place(x=220, y=280, width=150, height=30)
        btnApplyCal["command"] = lambda: (self.caldone(), calstatus.check())

    def calibration(self):
        self.btnStartCal['bg'] = '#b8ffd7'
        connection.send("SENS1:CORR:COEF:FULL2")
        connection.send("SENS1:CORR:COEF:PORT12:FULL2")
        time.sleep(.2)
        connection.send("SENS1:CORR:COLL:METH SSLT")
        time.sleep(.2)
        connection.send("SENS1:CORR:COLL:LINE WAVE")
        self.log.text("Connect 1/8 waveguide SHORT at port 1 ?")
        time.sleep(1.2)

    def P1short1_8(self):
        self.btnOpen1['bg'] = '#b8ffd7'
        connection.send("SENS1:CORR:COLL:PORT1:SHORT1")
        self.log.text("Connect 3/8 waveguide SHORT at port 1 ?")
        time.sleep(3)

    def P1short3_8(self):
        self.btnShort1['bg'] = '#b8ffd7'
        connection.send("SENS1:CORR:COLL:PORT1:SHORT2")
        self.log.text("Connect waveguide LOAD at Port1 ?")
        time.sleep(3)

    def P1load(self):
        self.btnLoad1['bg'] = '#b8ffd7'
        connection.send("SENS1:CORR:COLL:PORT1:LOAD1")
        self.log.text("Connect 1/8 waveguide SHORT at port 2 ?")
        time.sleep(3)

    def P2short1_8(self):
        self.btnOpen2['bg'] = '#b8ffd7'
        connection.send("SENS1:CORR:COLL:PORT2:SHORT1")
        self.log.text("Connect 3/8 waveguide SHORT at port 2 ?")
        time.sleep(3)

    def P2short3_8(self):
        self.btnShort2['bg'] = '#b8ffd7'
        connection.send("SENS1:CORR:COLL:PORT2:SHORT2")
        self.log.text("Connect waveguide LOAD at Port2 ?")
        time.sleep(3)

    def P2load(self):
        self.btnLoad2['bg'] = '#b8ffd7'
        connection.send("SENS1:CORR:COLL:PORT2:LOAD")
        self.log.text("Connect THRU Port 1-2 ?")
        time.sleep(3)

    def thru(self):
        self.btnCalibration['bg'] = '#b8ffd7'
        self.log.text("Apply Cal")
        connection.send("SENS1:CORR:COLL:PORT12:THRU")
        time.sleep(5)

    def caldone(self):
        connection.send("SENS1:CORR:COLL:SAVE")
        time.sleep(3)
        connection.send("RTL")


calibration = Calibration()