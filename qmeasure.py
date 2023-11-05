import math
import time
import tkinter as tk
from window import frame_qmeasurement
from connection import connection
from log import Log
from tkinter import ttk

class QMeasure:

    def __init__(self):
        
        #self.log = Log(frame_qmeasurement, { 'x':40, 'y':260, 'w':470, 'h':150 })

        L_PeakFr = tk.Label(frame_qmeasurement, borderwidth='1px', relief='groove')
        L_PeakFr["justify"] = "center"
        L_PeakFr["text"] = "Tx Measurement"
        L_PeakFr.place(x=65, y=90, width=470, height=155)

        L_PeakFr1 = tk.Label(frame_qmeasurement, borderwidth='1px', relief='groove')
        L_PeakFr1["justify"] = "center"
        L_PeakFr1["text"] = "Full 2-Port Measurement"
        L_PeakFr1.place(x=65, y=275, width=470, height=155)

        # ffff = ttk.Frame(frame_qmeasurement)
        # ffff.pack(fill='both', expand=True)
        # frame_qmeasurement.add(ffff, text='Connection')

        GButton_150=tk.Button(frame_qmeasurement)
        GButton_150["text"] = "Measure Q"
        GButton_150.place(x=30,y=30,width=150,height=30)
        GButton_150["command"] = self.start

        G_PeakFr = tk.Entry(frame_qmeasurement)
        self.G_PeakFr = G_PeakFr
        G_PeakFr["borderwidth"] = "1px"
        G_PeakFr["fg"] = "#333333"
        G_PeakFr["justify"] = "center"
        G_PeakFr.place(x=155, y=125, width=70, height=25)

        L_PeakFr = tk.Label(frame_qmeasurement, borderwidth='1px', relief='groove')
        self.L_PeakFr = L_PeakFr
        L_PeakFr["justify"] = "center"
        L_PeakFr["bg"] = "#b9dcb9"
        L_PeakFr["text"] = "Peak Freq"
        L_PeakFr.place(x=85, y=125, width=70, height=25)

        E_CoupleLoss = tk.Entry(frame_qmeasurement)
        self.E_CoupleLoss = E_CoupleLoss
        E_CoupleLoss["borderwidth"] = "1px"
        E_CoupleLoss["fg"] = "#333333"
        E_CoupleLoss["justify"] = "center"
        E_CoupleLoss.place(x=435, y=125, width=70, height=25)

        L_CoupleLoss = tk.Label(frame_qmeasurement,  borderwidth='1px', relief='groove')
        self.L_CoupleLoss = L_CoupleLoss
        L_CoupleLoss["justify"] = "center"
        L_CoupleLoss["bg"] = "#b9dcb9"
        L_CoupleLoss["text"] = "Couple Loss"
        L_CoupleLoss.place(x=365, y=125, width=70, height=25)

        E_QLoaded = tk.Entry(frame_qmeasurement)
        self.E_QLoaded = E_QLoaded
        E_QLoaded["borderwidth"] = "1px"
        E_QLoaded["fg"] = "#333333"
        E_QLoaded["justify"] = "center"
        E_QLoaded.place(x=155, y=200, width=70, height=25)

        L_QLoaded = tk.Label(frame_qmeasurement,  borderwidth='1px', relief='groove')
        L_QLoaded["justify"] = "center"
        L_QLoaded["bg"] = "#b9dcb9"
        L_QLoaded["text"] = "QLoaded"
        L_QLoaded.place(x=85, y=200, width=70, height=25)

        E_QunLoaded = tk.Entry(frame_qmeasurement)
        self.E_QunLoaded = E_QunLoaded
        E_QunLoaded["borderwidth"] = "1px"
        E_QunLoaded["fg"] = "#333333"
        E_QunLoaded["justify"] = "center"
        E_QunLoaded.place(x=435, y=200, width=70, height=25)

        L_QunLoaded = tk.Label(frame_qmeasurement,  borderwidth='1px', relief='groove')
        L_QunLoaded["justify"] = "center"
        L_QunLoaded["bg"] = "#b9dcb9"
        L_QunLoaded["text"] = "Qunloaded"
        L_QunLoaded.place(x=365, y=200, width=70, height=25)

        G_PeakFr2 = tk.Entry(frame_qmeasurement)
        self.G_PeakFr2 = G_PeakFr2
        G_PeakFr2["borderwidth"] = "1px"
        G_PeakFr2["fg"] = "#333333"
        G_PeakFr2["justify"] = "center"
        G_PeakFr2.place(x=155, y=310, width=70, height=25)

        L_PeakFr2 = tk.Label(frame_qmeasurement, borderwidth='1px', relief='groove')
        self.L_PeakFr2 = L_PeakFr2
        L_PeakFr2["justify"] = "center"
        L_PeakFr2["bg"] = "#b9dcb9"
        L_PeakFr2["text"] = "Peak Freq"
        L_PeakFr2.place(x=85, y=310, width=70, height=25)

        E_CoupleLoss2 = tk.Entry(frame_qmeasurement)
        self.E_CoupleLoss2 = E_CoupleLoss2
        E_CoupleLoss2["borderwidth"] = "1px"
        E_CoupleLoss2["fg"] = "#333333"
        E_CoupleLoss2["justify"] = "center"
        E_CoupleLoss2.place(x=435, y=310, width=70, height=25)

        L_CoupleLoss2 = tk.Label(frame_qmeasurement,  borderwidth='1px', relief='groove')
        self.L_CoupleLoss2 = L_CoupleLoss2
        L_CoupleLoss2["justify"] = "center"
        L_CoupleLoss2["bg"] = "#b9dcb9"
        L_CoupleLoss2["text"] = "Couple Loss"
        L_CoupleLoss2.place(x=365, y=310, width=70, height=25)

        E_QLoaded2 = tk.Entry(frame_qmeasurement)
        self.E_QLoaded2 = E_QLoaded2
        E_QLoaded2["borderwidth"] = "1px"
        E_QLoaded2["fg"] = "#333333"
        E_QLoaded2["justify"] = "center"
        E_QLoaded2.place(x=155, y=385, width=70, height=25)

        L_QLoaded2 = tk.Label(frame_qmeasurement,  borderwidth='1px', relief='groove')
        L_QLoaded2["justify"] = "center"
        L_QLoaded2["bg"] = "#b9dcb9"
        L_QLoaded2["text"] = "QLoaded"
        L_QLoaded2.place(x=85, y=385, width=70, height=25)

        E_QunLoaded2 = tk.Entry(frame_qmeasurement)
        self.E_QunLoaded2 = E_QunLoaded2
        E_QunLoaded2["borderwidth"] = "1px"
        E_QunLoaded2["fg"] = "#333333"
        E_QunLoaded2["justify"] = "center"
        E_QunLoaded2.place(x=435, y=385, width=70, height=25)

        L_QunLoaded2 = tk.Label(frame_qmeasurement,  borderwidth='1px', relief='groove')
        L_QunLoaded2["justify"] = "center"
        L_QunLoaded2["bg"] = "#b9dcb9"
        L_QunLoaded2["text"] = "Qunloaded"
        L_QunLoaded2.place(x=365, y=385, width=70, height=25)
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
        peakFrequency = self.calculatePeakFq(frequency)
        connection.send("CALC1:MARK:SEA:BAND:DATA?")
        combinedData = connection.receive(False) or "3.09327738688E+009,7.72990113024E+009,2.498936E+000,-5.778590E+000,1.00000000000E+006"
        separatedData = combinedData.split(',')
        loadedQFactor = float(separatedData[2])
        couplingS21 = separatedData[3]  # CALC1:PAR1:MARK1:Y?
        power = float(couplingS21) / 20
        unloadedQ = loadedQFactor * (1 / (1 - math.pow(10, power)))

        summary = f'''
        Peak Frequency: {peakFrequency}
        Loaded Q Factor: {loadedQFactor}
        Coupling S21: {couplingS21}
        Unloaded Q: {unloadedQ}'''
        #Self.log.text(summary)

        self.E_QunLoaded.delete(0, 'end')
        self.E_QLoaded.delete(0, 'end')
        self.E_CoupleLoss.delete(0, 'end')
        self.G_PeakFr.delete(0, 'end')

        self.E_QunLoaded.insert(0, unloadedQ)
        self.E_QLoaded.insert(0, loadedQFactor)
        self.E_CoupleLoss.insert(0, couplingS21)
        self.G_PeakFr.insert(0, peakFrequency)

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