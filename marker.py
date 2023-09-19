import tkinter as tk
from window import frame_marker
from connection import connection

class Marker:

    def __init__(self):
        
        LabelFq=tk.Label(frame_marker)
        LabelFq["text"] = "Enter Frequency"
        LabelFq.place(x=40,y=30,width=155,height=30)

        EntryFq=tk.Entry(frame_marker)
        EntryFq.delete(0, 'end')
        EntryFq.insert(0, '2.2')
        EntryFq.place(x=210,y=30,width=94,height=30)
        self.EntryFq = EntryFq

        BtnFq=tk.Button(frame_marker)
        BtnFq["text"] = "SET MARKER"
        BtnFq.place(x=140,y=90,width=100,height=30)
        BtnFq["command"] = self.setMarker

    def setMarker(self):
        print("SET MARKER")
        connection.send("CALC1:PAR3:MARK2:ACT")
        connection.send("CALC1:PAR3:MARK2:X " + self.EntryFq.get() + "E9")
        connection.send("CALC1:PAR3:MARK2:X?")
        connection.receive()
        connection.send("RTL")

marker = Marker()