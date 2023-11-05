from window import window, notebook, setCurrentTabInstance
from connection import connection
from vnasettings import vnasetting
from calibration import calibration
from qmeasure import qmeasure
from calstatus import calstatus
from livetrace import livetrace

def tabClick(event):
    # notebook.index(notebook.select())
    tabName = event.widget.tab('current')['text']
    print(tabName)
    if tabName == 'Connection':
        setCurrentTabInstance(connection)
    elif tabName == 'VNA Setting':
        setCurrentTabInstance(vnasetting)
    elif tabName == 'Calibration':
        setCurrentTabInstance(calibration)
    elif tabName == 'Measurement':
        setCurrentTabInstance(qmeasure)
    elif tabName == 'GUI':
        setCurrentTabInstance(qmeasure)
    elif tabName == 'Live Trace':
        setCurrentTabInstance(livetrace)

notebook.bind('<<NotebookTabChanged>>', tabClick)

setCurrentTabInstance(connection)
calstatus.check()

window.mainloop()
