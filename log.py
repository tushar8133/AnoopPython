from tkinter import scrolledtext
from window import window

class Log:
    def __init__(self, container, pos):
        self.widget = scrolledtext.ScrolledText(container, wrap = "none")
        self.widget.place(x=pos['x'], y=pos['y'], width=pos['w'], height=pos['h'])
        self.widget['state'] = 'disabled'
    
    def text(self, x='', y=''):
        x = x.rstrip('\\n\n')
        y = y.rstrip('\\n\n')
        self.widget['state'] = 'normal'
        self.widget.yview_pickplace("end")
        all = str(x) + str(y) + '\n'
        self.widget.insert('end', all)
        self.widget['state'] = 'disabled'
        # window.update()
        # window.update_idletasks()
