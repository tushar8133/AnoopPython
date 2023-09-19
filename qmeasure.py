import time
import tkinter as tk
from window import frame_qmeasurement
from connection import connection
from log import Log

class QMeasure:

    def __init__(self):
        
        self.log = Log(frame_qmeasurement, { 'x':40, 'y':260, 'w':470, 'h':150 })
        
        GButton_150=tk.Button(frame_qmeasurement)
        GButton_150["text"] = "Start"
        GButton_150.place(x=20,y=20,width=81,height=30)
        GButton_150["command"] = self.start


        # messageBox=tk.Label(frame_qmeasurement)
        # messageBox["text"] = ""
        # messageBox["font"] = tkFont.Font(size=23)
        # messageBox["justify"] = "left"
        # messageBox.place(x=20,y=70,width=600,height=396)
        # self.messageBox = messageBox

    
    def start(self):
        print("Q Measurement Started")
        connection.send("CALC1:PAR1:DEF S21")
        time.sleep(.5)
        connection.send("CALC1:ALT:TRAC:NAM:STAT ON")
        connection.send(':CALC1:ALT:TRAC:NAMe "QMeasurement"')
        time.sleep(.25)
        connection.send("CALC1:PAR1:MARK1:ACT")
        connection.send("CALC1:MARK:SEA:TRACK ON")
        connection.send("CALC1:MARK:SEA MAX")
        connection.send("CALC1:PAR1:MARK1:Y?")
        print('S21',connection.receive())
        connection.send("CALC1:MARK:SEA:BAND ON")
        connection.send("CALC1:MARK:SEA:BAND:DEF 3.0")
        connection.send("DISP:WIND1:TRAC1:SIZ MAX")
        connection.send("CALC1:MARK:X?")
        frequency = connection.receive(False) or 0.0
        print('Frequency:', frequency)
        frequencyMHz = float(frequency) / 1000000000
        print('Frequency In MHz:', frequencyMHz)
        connection.send("CALC1:MARK:SEA:BAND:DATA?")
        combinedData = connection.receive(False) or '0,0,0,0'
        separatedData = combinedData.split(',')
        loadedQFactor = float(separatedData[2])
        couplingS21 = separatedData[3]  # CALC1:PAR1:MARK1:Y?
        unloadedQ = loadedQFactor * (1 + frequencyMHz / 100)
        peakFrequency = self.calculatePeakFq(frequency)
        

        # self.messageBox['text'] = ''
        summary = f'''
Loaded Q Factor: {loadedQFactor}
Coupling S21: {couplingS21}
Unloaded Q: {unloadedQ}
Peak Frequency: {peakFrequency}'''
        self.log.text(summary)

        time.sleep(2)
        #connection.send("DISP:WIND1:TRAC1:SIZ NORM")
        connection.send("CALC1:PAR1:DEF S11")
        connection.send("CALC1:MARK:SEA:BAND OFF")
        #("CALC1:MARK:OFF")
        connection.send("CALC1:ALT:TRAC:NAM:STAT OFF")
        time.sleep(.25)
        connection.send("DISP:WIND1:TRAC1:SIZ NORM")
        connection.send("RTL")


    def calculatePeakFq(self, frequency):
        frequency = float(frequency)
        fq = 0
        unit = ''
        digits = len("{:.0f}".format(frequency))
        if digits >= 0 and digits <= 3:
            fq = frequency
            unit = 'Hz'
        elif digits >= 4 and digits <= 6:
            fq = frequency / 1000
            unit = 'KHz'
        elif digits >= 7 and digits <= 9:
            fq = frequency / 1000000
            unit = 'MHz'
        elif digits >= 10:
            fq = frequency / 1000000000
            unit = 'GHz'
        return str(fq) + " " + unit


qmeasure = QMeasure()