import tkinter as tk   
import time
from window import window, getCurrentTabInstance
from connection import connection

class CalStatus:
    def __init__(self, container):
        
        btnCalStatus = tk.Button(container)
        self.btnCalStatus = btnCalStatus
        btnCalStatus["bg"] = "#61e827"
        btnCalStatus.place(x=510, y=55, width=60, height=25)
        btnCalStatus["text"] = "CAL STATS"
        btnCalStatus["command"] = self.check

        GButton_417 = tk.Button(container)
        GButton_417["justify"] = "center"
        GButton_417["bg"] = "#819df9"
        GButton_417["text"] = "PRESET"
        GButton_417.place(x=510, y=25, width=60, height=25)
        GButton_417["command"] = self.presetAndCheck

    def presetAndCheck(self):
        self.preset()
        self.check()
        
    def check(self):
        box = getCurrentTabInstance()
        connection.send("SENS1:CORR:STAT?")
        x = connection.receive()
        if x == "1":
            box.log.text('Status is 1')
            self.btnCalStatus["bg"] = "#48ff6c"
            self.btnCalStatus["text"] = "Cal ON"
        else:
            box.log.text('Status is NOT 1')
            self.btnCalStatus["bg"] = "#ff5353"
            self.btnCalStatus["text"] = "Cal OFF"
        connection.send("RTL")

    def preset(self):
        box = getCurrentTabInstance()
        box.log.text("Preset in progress. Please wait...")
        connection.send(":SYSTem:PRESet")
        time.sleep(3)
        box.log.text("Preset Complete!")
        connection.send("RTL")

calstatus = CalStatus(window)
# calstatus.check()
