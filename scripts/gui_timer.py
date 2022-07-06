#!/usr/bin/env python3 

# importing whole module
from tkinter import *
from tkinter.ttk import *
from timer import Timer 

# importing strftime function to
# retrieve system's time
from time import strftime

# creating tkinter window
root = Tk()
root.title('Clock')
timer = Timer()
# This function is used to
# display time on the label
def time():
  string = strftime('%H:%M:%S %p')
  wall_clock.config(text = string)
  wall_clock.after(1000, time)

def update_timer_lbl():
    str_duration = timer.get_formated_timer_duration()
    timer_lbl.config(text=str_duration)
    timer_lbl.after(1000, update_timer_lbl)

# Create a Button
start_btn = Button(root, text = 'Start', command = update_timer_lbl)
pause_btn = Button(root, text = 'Pause', command = timer.start)
stop_btn = Button(root, text = 'Stop', command = timer.start)

# Styling the label widget so that clock
# will look more attractive
wall_clock = Label(root, font = ('calibri', 40, 'bold'),
      background = 'purple',
      foreground = 'white')
timer_lbl = Label(root, font = ('calibri', 40, 'bold'),
      background = 'purple',
      foreground = 'white')


# Placing clock at the centre
# of the tkinter window
wall_clock.pack(anchor = 'center')
timer_lbl.pack(anchor='center')
start_btn.pack(anchor='s')
pause_btn.pack(anchor='s')
stop_btn.pack(anchor='s')
time()
mainloop()

