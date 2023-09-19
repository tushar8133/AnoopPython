import tkinter as tk               
from tkinter import ttk

window = tk.Tk()
window.title("Anritsu Shockline VNA Automation")
width=600
height=500
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
window.geometry(alignstr)
window.resizable(width=False, height=False)

# TO ALIGN NOTEBOOK TABS ON LHS
# style = ttk.Style(window)
# style.configure('lefttab.TNotebook', tabposition='wn')
# notebook = ttk.Notebook(window, style='lefttab.TNotebook')

notebook = ttk.Notebook(window)
notebook.pack(fill='both', expand=True)

frame_connection = ttk.Frame(notebook)
frame_vna_settings = ttk.Frame(notebook)
frame_calibration = ttk.Frame(notebook)
frame_qmeasurement = ttk.Frame(notebook)
frame_commands = ttk.Frame(notebook)
frame_marker = ttk.Frame(notebook)

notebook.add(frame_connection, text ='Connection')
notebook.add(frame_vna_settings, text ='VNA Setting')
notebook.add(frame_calibration, text ='Calibration')
notebook.add(frame_qmeasurement, text ='Q Measurement')
# notebook.add(frame_marker, text ='Set Marker')
# notebook.add(frame_commands, text ='Commands')

def setCurrentTabInstance(x):
    global currentTabInstance
    currentTabInstance = x

def getCurrentTabInstance():
    return currentTabInstance
