import tkinter as tk   
import time
from window import frame_calibration
from connection import connection
from log import Log

class Calibration:
    def __init__(self):

        self.log = Log(frame_calibration, { 'x':40, 'y':260, 'w':470, 'h':150 })
        
        '''btnCalStatus = tk.Button(frame_calibration)
        self.btnCalStatus = btnCalStatus
        # btnCalStatus["bg"] = "#61e827"
        btnCalStatus.place(x=475, y=70, width=70, height=30)
        btnCalStatus["text"] = "CAL STATS"
        btnCalStatus["command"] = self.calstatus'''

        btnStartCal = tk.Button(frame_calibration)
        self.btnStartCal = btnStartCal
        btnStartCal["text"] = "Start Cal"
        btnStartCal.place(x=30, y=30, width=150, height=30)
        btnStartCal["command"] = self.calibration

        btnOpen1 = tk.Button(frame_calibration)
        self.btnOpen1 = btnOpen1
        btnOpen1["text"] = "Port 1: OPEN"
        btnOpen1.place(x=80, y=80, width=150, height=30)
        btnOpen1["command"] = self.open1

        btnShort1 = tk.Button(frame_calibration)
        self.btnShort1 = btnShort1
        btnShort1["text"] = "Port 1: SHORT"
        btnShort1.place(x=80, y=110, width=150, height=30)
        btnShort1["command"] = self.short1

        btnLoad1 = tk.Button(frame_calibration)
        self.btnLoad1 = btnLoad1
        btnLoad1["text"] = "Port 1: LOAD"
        btnLoad1.place(x=80, y=140, width=150, height=30)
        btnLoad1["command"] = self.load1

        btnOpen2 = tk.Button(frame_calibration)
        self.btnOpen2 = btnOpen2
        btnOpen2["text"] = "Port 2: OPEN"
        btnOpen2.place(x=360, y=80, width=150, height=30)
        btnOpen2["command"] = self.open2

        btnShort2 = tk.Button(frame_calibration)
        self.btnShort2 = btnShort2
        btnShort2["text"] = "Port 2: SHORT"
        btnShort2.place(x=360, y=110, width=150, height=30)
        btnShort2["command"] = self.short2

        btnLoad2 = tk.Button(frame_calibration)
        self.btnLoad2 = btnLoad2
        btnLoad2["text"] = "Port 2: LOAD"
        btnLoad2.place(x=360, y=140, width=150, height=30)
        btnLoad2["command"] = self.load2

        btnCalibration = tk.Button(frame_calibration)
        self.btnCalibration = btnCalibration
        btnCalibration["text"] = "Port 1-2: THRU"
        btnCalibration.place(x=220, y=190, width=150, height=30)
        btnCalibration["command"] = self.thru

        btnApplyCal = tk.Button(frame_calibration)
        self.btnApplyCal = btnApplyCal
        btnApplyCal["text"] = "APPLY CAL "
        btnApplyCal.place(x=220, y=220, width=150, height=30)
        btnApplyCal["command"] = lambda:(self.caldone())
        # btnApplyCal["command"] = lambda:(self.caldone(), calstatus())
        #self.calstatus()

    def calibration(self):
        connection.send("SENS1:CORR:COEF:FULL2")
        connection.send("SENS1:CORR:COEF:PORT12:FULL2")
        time.sleep(1.2)

    def open1(self):
        self.btnOpen1['bg'] = '#b8ffd7'
        self.log.text("Connect OPEN at Port1 ?")
        connection.send("SENS1:CORR:COLL:PORT1:OPEN")
        time.sleep(3)

    def short1(self):
        self.btnShort1['bg'] = '#b8ffd7'
        self.log.text("Connect SHORT at Port1 ?")
        connection.send("SENS1:CORR:COLL:PORT1:SHORT")
        time.sleep(3)

    def load1(self):
        self.btnLoad1['bg'] = '#b8ffd7'
        self.log.text("Connect LOAD at Port1 ?")
        connection.send("SENS1:CORR:COLL:PORT1:LOAD")
        time.sleep(3)

    def open2(self):
        self.btnOpen2['bg'] = '#b8ffd7'
        self.log.text("Connect OPEN at Port2 ?")
        connection.send("SENS1:CORR:COLL:PORT2:OPEN")
        time.sleep(3)

    def short2(self):
        self.btnShort2['bg'] = '#b8ffd7'
        self.log.text("Connect SHORT at Port2 ?")
        connection.send("SENS1:CORR:COLL:PORT2:SHORT")
        time.sleep(3)

    def load2(self):
        self.btnLoad2['bg'] = '#b8ffd7'
        self.log.text("Connect LOAD at Port2 ?")
        connection.send("SENS1:CORR:COLL:PORT2:LOAD")
        time.sleep(3)

    def thru(self):
        self.btnCalibration['bg'] = '#b8ffd7'
        self.log.text("Connect THRU Port 1-2 ?")
        connection.send("SENS1:CORR:COLL:PORT12:THRU")
        time.sleep(5)

    def caldone(self):
        connection.send("SENS1:CORR:COLL:SAVE")
        time.sleep(3)
        self.log.text("Calibration Done")
        connection.send("RTL")


calibration = Calibration()