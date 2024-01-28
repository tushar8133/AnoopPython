# Import module 
from tkinter import *

# Create object 
root = Tk() 

# Adjust size 
root.geometry( "200x200" ) 


# Dropdown menu options 
ddOptions = [
	'WR187 (3.95 - 5.85 GHz)',
	'WR137 (5.85 - 8.20 GHz)',
	'WR90 (8.20 - 12.40 GHz)',
	'WR62 (12.40 - 18 GHz)',
	'WR42 (18.00 - 26.50 GHz)'
]


# datatype of menu text 
ddValue = StringVar()

# initial menu text 
ddValue.set(ddOptions[2])

def ddListener(*args):
	band = ddValue.get().split(" (",1)[0]
	cutoff = 6.557e9
	if (band == 'WR187'):
		cutoff = 3.153e9
	elif (band == 'WR137'):
		cutoff = 4.301e9
	elif (band == 'WR90'):
		cutoff = 6.557e9
	elif (band == 'WR62'):
		cutoff = 9.488e9
	elif (band == 'WR42'):
		cutoff = 14.051e9
	print(cutoff)

ddValue.trace_add('write', ddListener)
ddMenu = OptionMenu( root , ddValue , *ddOptions )
ddMenu.pack()

# Execute tkinter 
root.mainloop() 
