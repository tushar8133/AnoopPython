from skrf import Network, constants
import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import skrf as rf
rf.stylely()
from window import frame_nrw, window, enableTabs
import tkinter as tk
from pathlib import Path
import math
from connection import connection
import os
import time
from common import defaultPauseTime, defaultWinUpdateTime, getCutOffFreq

class NRW:
    def __init__(self):

        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.full_path = os.path.join(dir_path, 'NPL.s2p')

        self.counter = 0
        self.running = False

        self.frame1 = tk.LabelFrame(frame_nrw)
        self.frame1.pack(side="top", fill="x", expand=False)
        self.frame2 = tk.LabelFrame(frame_nrw)
        self.frame2.pack(side="top", fill="both", expand=True)

        self.b1 = tk.Button(self.frame1, text="Start", padx=20, command=self.toggle)
        self.b1.pack(side="top")

        self.E_Thickness = tk.Entry(self.frame1, width=10)
        self.E_Thickness.pack(side="left")
        self.E_Thickness.delete(0, 'end')
        self.E_Thickness.insert(0, '0.002')
        self.b2 = tk.Button(self.frame1, text="Thickness", padx=1)
        self.b2.pack(side="left", padx=5)
        # self.L_StartFr = tk.Label(self.frame1, borderwidth='1px', relief='groove', text="Start Fr").pack(side="left")

        self.graph_magnetic = []
        self.graph_electrical = []
        self.graph_loss = []
        self.graph_frequency = []
        # self.data = Network(self.full_path)

        #self.minFq = self.data.f_scaled.min()
        #self.maxFq = self.data.f_scaled.max()



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
        canvas = FigureCanvasTkAgg(figure, master=self.frame2)
        canvas.get_tk_widget().pack(side='left', fill='both')
        canvas.mpl_connect('draw_event', self.drawing_done)

    def toggle2(self):
        pass

    def toggle(self):
        if self.running:
            self.running = False
            self.b1['text'] = 'Start'
            enableTabs(True)
        else:
            enableTabs([4])
            self.counter = 0
            self.running = True
            self.b1['text'] = 'Stop'
            self.store_file()

    def drawing_done(self, x):
        print("drawing done...")
        if self.running:
            self.counter = self.counter + 1
            window.after(defaultWinUpdateTime, self.store_file)

    def store_file(self):
        if os.path.isfile(self.full_path):
            os.remove(self.full_path)
        connection.send("MMEM:STOR '" + self.full_path + "'")
        while not os.path.exists(self.full_path):
            time.sleep(defaultPauseTime)
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
            time.sleep(defaultPauseTime)
            self.plot_graphs()

        self.totalPoints = int(self.data.s.size / 4)
        # path = Path(self.full_path)


        # data.s11.plot_s_smith(ax=axes1, show_legend=True, label="s11")
        # data.s12.plot_s_db(ax=axes2, show_legend=True, label="s12")
        # data.s21.plot_s_db(ax=axes3, show_legend=True, label="s21")
        # data.s22.plot_s_smith(ax=axes4, show_legend=True, label="s22")

        # self.graph_magnetic.plot(ax=axes1, show_legend=True, label="s11")
        axes1.clear()
        axes2.clear()
        axes3.clear()
        axes4.clear()
        self.calculate_data()
        axes1.plot(self.graph_frequency, self.graph_magnetic, color = "green")
        axes2.plot(self.graph_frequency, self.graph_electrical)
        #axes2.set_ylim(2, 8)
        axes2.set(xlabel="frequency", ylabel="Epsl")

        #axes3.plot(self.graph_loss, color = "red")
        #axes4.plot(self.graph_loss)

        #axes4.set_xlim(self.minFq, self.maxFq)


        # print(">>>", self.graph_electrical)
        canvas.draw()

    def calculate_data(self):
        self.graph_magnetic = []
        self.graph_electrical = []
        self.graph_loss = []
        self.graph_frequency = []
        _fc = float(getCutOffFreq())  # '6.557e9' user input cutoff frequency #Ghz conversion???

        for i in range(self.totalPoints):
            _complex_s11 = self.data.s[i:(i+1),0,0][0]
            _complex_s21 = self.data.s[i:(i+1),0,1][0]
            _x = ((   (_complex_s11)**2 ) - ((_complex_s21)**2) + 1) / (2 * _complex_s11)
            _gm1 = _x + (( (_x**2) - 1 )**(1/2))
            _gm2 = _x - (( (_x**2) - 1 )**(1/2))
            _ag1 = abs(_gm1)
            _ag2 = abs(_gm2)

            _gm3 = 0
            if _ag2 <= 1:
                _gm3 = _gm2
            elif _ag1 <= 1:
                _gm3 = _gm1

            L = float(self.E_Thickness.get()) #user input thickness of material
            t = (_complex_s11+ _complex_s21 - _gm3)/(1-((_complex_s11 + _complex_s21) * _gm3))
            tx = np.log(1/t)
            txx = -((1/(2 * math.pi * L)) * tx)**2
            phase_fac = txx**(1/2)

            _c = constants.c # 3*10^8 # speed of light
            _fq = self.data.f[i:(i+1)]
            self.graph_frequency.append(_fq[0]/1000000000)
            _lambda = _c / _fq
            _lc = _c/_fc
            _a = 1/np.square(_lc)

            za = (1+_gm3)/(1-_gm3)
            yy = (1/np.square(_lambda)) - _a
            mur = (za * (phase_fac) * (1/np.sqrt(yy))) #magnetic
            er = ((np.square(_lambda))/mur) * (txx + _a) # electric
            tandel1 = (mur.real * er.real) - (mur.imag * er.imag)
            tandel2 = (mur.real * er.imag) + (mur.imag * er.real)
            loss = tandel2/tandel1

            self.graph_magnetic.append(mur[0].real)
            self.graph_electrical.append(er[0].real)
            self.graph_loss.append(loss[0])


nrw = NRW()
