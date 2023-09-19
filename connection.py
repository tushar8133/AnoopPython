import socket
import tkinter as tk
from window import frame_connection
from log import Log

class Connection:
    def __init__(self):

        self.vna = False

        self.log = Log(frame_connection, { 'x':40, 'y':260, 'w':470, 'h':150 })

        GLabel_133=tk.Label(frame_connection)
        GLabel_133["text"] = "IP ADDRESS"
        GLabel_133.place(x=40,y=40,width=100,height=25)

        GLabel_735=tk.Label(frame_connection)
        GLabel_735["text"] = "PORT"
        GLabel_735.place(x=40,y=90,width=100,height=25)

        EntryIP=tk.Entry(frame_connection)
        EntryIP.delete(0, 'end')
        EntryIP.insert(0, '127.0.0.1')
        EntryIP.place(x=160,y=40,width=231,height=30)
        self.EntryIP = EntryIP

        EntryPort=tk.Entry(frame_connection)
        EntryPort.delete(0, 'end')
        EntryPort.insert(0, '5001')
        EntryPort.place(x=160,y=90,width=100,height=30)
        self.EntryPort = EntryPort

        GButton_7=tk.Button(frame_connection)
        GButton_7["text"] = "Connect"
        GButton_7.place(x=40,y=150,width=99,height=30)
        GButton_7["command"] = self.connect

        GButton_956=tk.Button(frame_connection)
        GButton_956["text"] = "Test"
        GButton_956.place(x=40,y=200,width=100,height=30)
        GButton_956["command"] = self.test

        # GMessage_968=tk.Message(frame_connection)
        # GMessage_968["text"] = "Message"
        # GMessage_968.place(x=40,y=260,width=509,height=212)
    def test(self):
        self.log.text("Testing *IDN? ...")
        self.send('*IDN?')

    def connect(self):
        try:
            self.vna = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ip = self.EntryIP.get()
            port = int(self.EntryPort.get())
            self.vna.connect((ip, port))
            self.log.text("SOCKET CONNECTED AT, " + ip + ", " + str(port))
        except:
            self.log.text("Connection Problem")

    def send(self, raw):
        try:
            cmd = raw.rstrip('\\n\n') + '\n'
            print(">>>>", cmd)
            self.vna.send(cmd.encode())
        except:
            self.log.text("Data could not be sent!")

    def receive(self, x = True):
        print("<<<<", output)
        try:
            self.vna.settimeout(2)
            output = self.vna.recv(2056).decode().rstrip('\n')
            if x == True:
                self.log.text(output)
            return output
        except:
            print("Nothing received!")
            self.log.text("Nothing received!")

connection = Connection()
connection.connect()