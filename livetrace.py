import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from skrf import Network, Frequency
import skrf as rf
rf.stylely()
from window import frame_livetrace, window
from connection import connection


class LiveTrace:
    def __init__(self):
        
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
        self.store_file()

    def drawing_done(self, x):
        print("drawing done...")
        window.after(2000, self.store_file)

    def store_file(self):
        connection.send("MMEM:STOR 'test.s2p'")
        print(">>>> file saved ")
        self.plot_graphs()

    def plot_graphs(self):

        axes1.clear()
        axes2.clear()
        axes3.clear()
        axes4.clear()

        data = Network("Port 4.s2p")
        #data.s11.plot_s_db_time(ax=axes1, window='hamming', label="HTG")
        data.s12.plot_s_db(ax=axes2, show_legend=True)
        data.s21.plot_s_db(ax=axes3, show_legend=True)
        data.s22.plot_s_db(ax=axes4, show_legend=True)

        s11 = data.s11
        s11_w = data.windowed()
        s11_gated = data.s11.time_gate(center=0, span=4, t_unit='ns')

        # s11.plot_s_db_time()
        s11_gated.plot_s_db_time(ax=axes1, window='rectangular', label="RTG")
        s11_gated.plot_s_db_time(ax=axes1, window='hamming', label="HTG")
        s11_gated.plot_s_db_time(ax=axes1, label="TG")
        canvas.draw()


livetrace = LiveTrace()
