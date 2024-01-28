import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from skrf import Network, Frequency
import skrf as rf
rf.stylely()
from window import frame_livetrace, window
from connection import connection
from tkinter import Button
from pathlib import Path
import os
import time


class LiveTrace:
    def __init__(self):

        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.full_path = os.path.join(dir_path, 'livetrace.s2p')

        self.counter = 0
        self.running = False

        self.b1 = Button(frame_livetrace, text="Start", command=self.toggle)

        self.b1.pack()

        # Matplotlib Figure
        # fig, ax = plt.subplots()
        figure = Figure(figsize=(150, 5.8), dpi=75)
        figure.clf()

        global axes1
        global axes2
        global axes3
        global axes4

        axes1 = figure.add_subplot(221); axes1.grid()
        axes2 = figure.add_subplot(222); axes2.grid()
        axes3 = figure.add_subplot(223); axes3.grid()
        axes4 = figure.add_subplot(224); axes4.grid()

        # Create Canvas
        global canvas
        canvas = FigureCanvasTkAgg(figure, master=frame_livetrace)
        canvas.get_tk_widget().pack(side='top', fill='both')
        canvas.mpl_connect('draw_event', self.drawing_done)

    def toggle(self):
        if self.running:
            self.running = False
            self.b1['text'] = 'Start'
        else:
            self.counter = 0
            self.running = True
            self.b1['text'] = 'Stop'
            self.store_file()

    def drawing_done(self, x):
        print("drawing done...")
        if self.running:
            self.counter = self.counter + 1
            window.after(10, self.store_file)
            # window.update()
            # self.store_file()

    def store_file(self):
        if os.path.isfile(self.full_path):
            os.remove(self.full_path)
        connection.send("MMEM:STOR '" + self.full_path + "'")
        while not os.path.exists(self.full_path):
            time.sleep(0.01)
        if os.path.isfile(self.full_path):
            print(">>>> file saved ")
            self.plot_graphs()
        else:
            print(">>> couldnt find file to proceed and plot graph")

    def plot_graphs(self):

        print('counter >>', self.counter)

        try:
            self.data = Network(self.full_path)
        except:
            print("Problem in reading file")
            time.sleep(0.01)
            self.plot_graphs()

        axes1.clear()
        axes2.clear()
        axes3.clear()
        axes4.clear()

        # path = Path(self.full_path)
        #data.s11.plot_s_db_time(ax=axes1, window='hamming', label="HTG")
        self.data.s11.plot_s_db(ax=axes1, show_legend=True, label="s11")
        #self.data.s12.plot_s_db(ax=axes2, show_legend=True, label="s12")
        self.data.s21.plot_s_db(ax=axes3, show_legend=True, label="s21")
        self.data.s22.plot_s_db(ax=axes4, show_legend=True, label="s22")


        '''s11 = data.s11
        s11_w = data.windowed()
        s11_gated = data.s11.time_gate(center=2, span=4, t_unit='ns')

        # s11.plot_s_db_time()
        #s11_gated.plot_s_db_time(ax=axes1, window='rectangular', label="RTG")
        #s11_gated.plot_s_db_time(ax=axes1, window='hamming', label="HTG")
        s11_gated.plot_s_db_time(ax=axes1, label="TG")'''

        canvas.draw()

livetrace = LiveTrace()
