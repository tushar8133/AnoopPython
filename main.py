from window import window, notebook, setCurrentTabInstance
from connection import connection
from vnasettings import vnasetting
from calibration import calibration
from qmeasure import qmeasure
from calstatus import calstatus
from livetrace import livetrace
from ORIG_NRW import nrw_ori
from NPL_NRW import nrw

def tabClick(event):
    # notebook.index(notebook.select())
    tabName = event.widget.tab('current')['text']
    print(tabName)
    if tabName == 'Connection':
        setCurrentTabInstance(connection)
    elif tabName == 'VNA Setting':
        setCurrentTabInstance(vnasetting)
        vnasetting.now()
    elif tabName == 'Calibration':
        setCurrentTabInstance(calibration)
    elif tabName == 'Live Trace':
        setCurrentTabInstance(livetrace)
    elif tabName == 'Q Measurement':
        setCurrentTabInstance(qmeasure)
    elif tabName == 'NRW-ORI':
        setCurrentTabInstance(nrw_ori)
    elif tabName == 'NRW-NPL':
        setCurrentTabInstance(nrw)

notebook.bind('<<NotebookTabChanged>>', tabClick)

setCurrentTabInstance(connection)
calstatus.check()

window.mainloop()
