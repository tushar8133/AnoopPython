from window import window, notebook, setCurrentTabInstance
from connection import connection
from vnasettings import vnasetting
from calibration import calibration
from qmeasure import qmeasure
from calstatus import calstatus

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
    elif tabName == 'Q Measurement':
        setCurrentTabInstance(qmeasure)
    else:
        setCurrentTabInstance(False)

notebook.bind('<<NotebookTabChanged>>', tabClick)

window.mainloop()
