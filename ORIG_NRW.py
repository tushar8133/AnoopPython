from skrf import Network, constants
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import skrf as rf
rf.stylely()
from window import frame_nrw_ori, window
from tkinter import Button
import tkinter as tk
from pathlib import Path
import math
from connection import connection
import os
import time
from common import defaultPauseTime, defaultWinUpdateTime

class NRW_ORI:
    def __init__(self):

        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.full_path = os.path.join(dir_path, 'NRW.s2p')

        self.counter = 0
        self.running = False

        self.frame1 = tk.LabelFrame(frame_nrw_ori)
        self.frame1.pack(side="top", fill="x", expand=False)
        self.frame2 = tk.LabelFrame(frame_nrw_ori)
        self.frame2.pack(side="top", fill="both", expand=True)

        #self.b1 = Button(frame_nrw_ori, text="Start", command=self.toggle)
        self.b1 = tk.Button(self.frame1, text="Start", padx=20, command=self.toggle)
        self.b1.pack(side="top")

        self.EO_L = tk.Entry(self.frame1, width=6)
        self.EO_L.pack(side="left")
        self.EO_L.delete(0, 'end')
        self.EO_L.insert(0, '0.002')
        self.b2 = tk.Button(self.frame1, text="T-(MUT)", padx=1, width=6)
        self.b2.pack(side="left", padx=5)

        self.EO_Ltotal = tk.Entry(self.frame1, width=6)
        self.EO_Ltotal.pack(side="left")
        self.EO_Ltotal.delete(0, 'end')
        self.EO_Ltotal.insert(0, '0.003')
        self.b2 = tk.Button(self.frame1, text="T-(SH)", padx=1, width=6)
        self.b2.pack(side="left", padx=5)

        self.graph_magnetic = []
        self.graph_electrical = []
        self.graph_loss = []
        self.graph_frequency = []


        # Matplotlib Figure
        # fig, ax = plt.subplots()
        figure = Figure(figsize=(150, 5.8), dpi=75)
        figure.clf()

        global axes1
        global axes2
        global axes3
        #global axes4

        axes1 = figure.add_subplot(221); axes1.grid()
        axes2 = figure.add_subplot(222); axes2.grid()
        axes3 = figure.add_subplot(223); axes3.grid()
        #axes4 = figure.add_subplot(224); axes4.grid()

        # Create Canvas
        global canvas
        canvas = FigureCanvasTkAgg(figure, master=frame_nrw_ori)
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
        # path = Path("C:/test.s2p")

        try:
            self.data = Network(self.full_path)
        except:
            print("Problem in reading file")
            time.sleep(defaultPauseTime)
            self.plot_graphs()

        self.totalPoints = int(self.data.s.size / 4)

        # data.s11.plot_s_smith(ax=axes1, show_legend=True, label="s11")
        # data.s12.plot_s_db(ax=axes2, show_legend=True, label="s12")
        # data.s21.plot_s_db(ax=axes3, show_legend=True, label="s21")
        # data.s22.plot_s_smith(ax=axes4, show_legend=True, label="s22")

        # self.graph_magnetic.plot(ax=axes1, show_legend=True, label="s11")
        axes1.clear()
        axes2.clear()
        axes3.clear()
        #axes4.clear()

        self.calculate_data()

        axes1.plot(self.graph_frequency, self.graph_magnetic, color = "green")
        #axes1.set_ylim(0, 5)
        axes1.set(xlabel="frequency", ylabel="Mu")

        axes2.plot(self.graph_frequency, self.graph_electrical, color = "blue")
        #axes2.set_ylim(4, 6)
        axes2.set(xlabel="frequency", ylabel="Epsl")

        axes3.plot(self.graph_frequency, self.graph_loss, color = 'red')
        #axes4.plot(self.graph_loss)

        canvas.draw()

    def calculate_data(self):
        self.graph_magnetic = []
        self.graph_electrical = []
        self.graph_loss = []
        self.graph_frequency = []
        for i in range(self.totalPoints):
            _fc = 6.557e9  # user input cutoff frequency #Ghz conversion???
            # print("_fc", _fc)
            L = float(self.EO_L.get())  # user input thickness of material
            # print("L", L)
            Ltotal = float(self.EO_Ltotal.get())  # user input waveguide total length
            # print("Ltotal", Ltotal)
            L1 = 0.00  # user input empty space
            # print("L1", L1)
            L2 = Ltotal - L - L1
            # print("L2", L2)
            _c = constants.c  # 3*10^8 # speed of light
            # print("_c", _c)
            _fq = self.data.f[i:(i + 1)]
            self.graph_frequency.append(_fq[0]/1000000000)
            # print("_fq", _fq)
            _lambda = _c / _fq
            # print("_lambda", _lambda)
            _lc = _c / _fc
            # print("_lc", _lc)
            _a = 1 / np.square(_lc)
            # print("_a", _a)
            yy = (1 / np.square(_lambda)) - _a
            # print("yy", yy)
            _gm0 = 2 * math.pi * 1j * np.sqrt(yy)
            # print("_gm0", _gm0)

            # Calculate plane transformation
            R1 = np.exp(-_gm0 * L1)
            # print("R1", R1)
            R2 = np.exp(-_gm0 * L2)
            # print("R2", R2)

            _complex_s11_NRW = self.data.s[i:(i + 1), 0, 0][0]
            _complex_s21_NRW = self.data.s[i:(i + 1), 0, 1][0]

            _complex_s11 = _complex_s11_NRW / (R1 ** 2)
            _complex_s21 = _complex_s21_NRW / (R1 * R2)

            _x = (((_complex_s11) ** 2) - ((_complex_s21) ** 2) + 1) / (2 * _complex_s11)
            # print('_x', _x)
            _gm1 = _x + (((_x ** 2) - 1) ** (1 / 2))
            # print('_gm1', _gm1)
            _gm2 = _x - (((_x ** 2) - 1) ** (1 / 2))
            # print('_gm2', _gm2)
            _ag1 = abs(_gm1)
            # print('_ag1', _ag1)
            _ag2 = abs(_gm2)
            # print('_ag2', _ag2)

            _gm3 = 0
            if _ag2 <= 1:
                _gm3 = _gm2
            elif _ag1 <= 1:
                _gm3 = _gm1
            # print(_gm3)

            t = (_complex_s11 + _complex_s21 - _gm3) / (1 - ((_complex_s11 + _complex_s21) * _gm3))
            # print("t", t)
            tx = np.log(1 / t)
            # print("tx", tx)
            txx = -((1 / (2 * math.pi * L)) * tx) ** 2
            # print("txx", txx)
            phase_fac = txx ** (1 / 2)
            # print("phase_fac", phase_fac)

            za = (1 + _gm3) / (1 - _gm3)
            # print("za", za)
            mur = (za * (phase_fac) * (1 / np.sqrt(yy)))  # magnetic
            # print("mur", mur)
            er = ((np.square(_lambda)) / mur) * (txx + _a)  # electric
            # print("er", er)
            tandel1 = (mur.real * er.real) - (mur.imag * er.imag)
            # print("tandel1", tandel1)
            tandel2 = (mur.real * er.imag) + (mur.imag * er.real)
            # print("tandel2", tandel2)
            loss = tandel2 / tandel1
            # print("loss", loss)

            self.graph_magnetic.append(mur[0].real)
            self.graph_electrical.append(er[0].real)
            self.graph_loss.append(loss[0])


nrw_ori = NRW_ORI()
