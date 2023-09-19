import tkinter as tk
from window import frame_commands
from connection import connection

class Command:

    def __init__(self):

        GButton_429=tk.Button(frame_commands)
        GButton_429["justify"] = "center"
        GButton_429["text"] = "*IDN?"
        GButton_429.place(x=20,y=20,width=70,height=25)
        GButton_429["command"] = self.test


    def test(self):
        print('IDN')
        connection.send('*IDN?')
        connection.receive()

command = Command()