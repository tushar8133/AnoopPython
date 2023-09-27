from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from skrf import Network, Frequency
from tkinter import filedialog as fd

root = Tk()
root.title("Test")
root.geometry("600x400")

frame1 = LabelFrame(root, text='Frame A', height=100)
frame1.pack(side='top', fill='x')

frame2 = LabelFrame(root, text='Frame B')
frame2.pack(side='top', expand=True, fill='both')

filename = 'test.s2p'

# Matplotlib Figure
# fig, ax = plt.subplots()
figure = Figure(figsize=(100, 5.8), dpi=50)
figure.clf()
axes = figure.add_subplot()

# Create Canvas
canvas = FigureCanvasTkAgg(figure, master=frame2)  
canvas.get_tk_widget().pack(side='top', fill='both')

# Create Toolbar
toolbar = NavigationToolbar2Tk(canvas, frame2, pack_toolbar=False)
toolbar.update()
toolbar.pack(anchor='w', fill='x')

def generate(str):
    # Plot data on Matplotlib Figure
    axes.clear()
    x = np.random.randint(0, 10, 10)
    y = np.random.randint(0, 10, 10)
    if str == 'plot':
        axes.plot(x, y)
    elif str == 'scatter':
        axes.scatter(x, y)
    else:
        ring_slot = Network(filename)
        ring_slot.plot_s_smith(ax=figure.gca())
    # figure.tight_layout()
    canvas.draw()

def openFile():
        global filename
        filetypes = (('Touchstone File', '*.s2p'),('All files', '*.*'))
        # f1 = fd.askopenfile(filetypes=filetypes)
        f1 = fd.askopenfilename(title='Select TouchStone File',initialdir='.',filetypes=filetypes)
        filename = f1


button1 = Button(frame1, text='plot', command=lambda: generate('plot'))
button1.pack(side='left', padx=5, pady=5)

button2 = Button(frame1, text='scatter', command=lambda: generate('scatter'))
button2.pack(side='left', padx=5, pady=5)

button3 = Button(frame1, text='smith', command=lambda: (openFile(), generate('')))
button3.pack(side='left', padx=5, pady=5)

root.mainloop()

'''
import skrf as rf
f = open("file.s2p", "r")
print(f.read())
ring_slot = rf.Network('file.s2p')
short = rf.data.wr2p2_short
line = rf.data.wr2p2_line
delayshort = line ** short
print(line.frequency)
print('ring_slot.s', ring_slot.s)
print('ring_slot.s_arcl', ring_slot.s_arcl)
print('ring_slot.s_im', ring_slot.s_im)
print('ring_slot.s11', ring_slot.s11)
print('ring_slot.s_arcl_unwrap', ring_slot.s_arcl_unwrap)
print('ring_slot.s_mag', ring_slot.s_mag)
'''

'''
# install these libraries...
# pip3 install scikit-rf
# pip3 install matplotlib

from skrf import Network, Frequency
import matplotlib.pyplot as plt
ring_slot = Network('file.s2p')
ring_slot.plot_s_smith(draw_labels=True)
plt.show()
'''


'''
send("DISP:WIND1:SPL R2C1")
# send('CALC1:ALT:TRAC:NAM "Material Measurement"')
send("DISP:WIND1:ACT")
send("MMEM:STOR 'C:/filename2.s2p'")
time.sleep(3)
send("DISP:COUN 2")
send("DISP:WIND2:ACT")
send("DISP:WIND2:SPL R2C1")
send("SENS2:HOLD:FUNC HOLD")
send("SENS2:MMEM:LOAD 'filename2.s2p")
'''


'''
tk._test()
tk.Tcl().eval('info patchlevel')
'''