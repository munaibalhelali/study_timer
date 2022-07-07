#!/usr/bin/env python3 

# importing whole module
from tkinter import *
from tkinter.ttk import *
from timer import Timer 
from time import strftime

# creating tkinter windows
root = Tk()
root.title('Study Timer')
root.geometry('400x150+700+200')
# root.resizable(False, False)

display_window = Frame(root, width='300')
control_window = LabelFrame(root, width='100', text='Control', )
timer_display_window = LabelFrame(display_window, height='100', text='Timer')
time_date_display_window = LabelFrame(display_window, height='50', text='Date & Time')

timer = Timer()

f = ('Times', 20)
hour_string=StringVar()
min_string=StringVar()
last_value_sec = ""
last_value = "" 

# This function is used to
# display time on the label

def time():
  string = strftime('%D %H:%M:%S %p')
  wall_clock.config(text = string)
  wall_clock.after(1000, time)

def start_timer():
    timer.start()
    update_timer_lbl()
    if timer.started:
        start_btn.config(text= "Restart")
    else:
        start_btn.config(text="Start")

def update_timer_lbl():
    timer.update()
    str_duration = timer.get_formated_timer_duration()
    timer_lbl.config(text=str_duration)
    timer_lbl.after(1000, update_timer_lbl)

def toggle_pause_continue():
    if not timer.started:
        return
    if timer.paused:
        timer.continue_timer()
        pause_btn.config(text='Pause')
    else:
        timer.pause()
        pause_btn.config(text='Continue')

def stop_timer():
    start_btn.config(text="Start")
    timer.stop()

count_down = False 
hour_sb = Spinbox(
        timer_display_window,
        from_=0,
        to=99,
        wrap=True,
        textvariable=hour_string,
        width=2,
        font=f,
        justify=CENTER
        )
hour_sb.set(0)
min_sb = Spinbox(
    timer_display_window,
    from_=0,
    to=59,
    wrap=True,
    textvariable=min_string,
    font=f,
    width=2,
    justify=CENTER,
    
    )
min_sb.set(0)

sec_sb = Spinbox(
    timer_display_window,
    from_=0,
    to=59,
    wrap=True,
    textvariable=min_sb,
    width=2,
    font=f,
    justify=CENTER
    )
sec_sb.set(0)

def set_count_down(): 
    global count_down
    
    if not count_down:
        timer_lbl.grid_remove()
        hour_sb.grid(row=0, column=0, sticky="NSEW")
        min_sb.grid(row=0, column=1, sticky="NSEW")
        sec_sb.grid(row=0, column=2, sticky="NSEW")
        count_down = True
        set_count_down_btn.config(text='Confirm')
    else:
        initalize_count_down()
        hour_sb.grid_remove()
        min_sb.grid_remove()
        sec_sb.grid_remove()
        timer_lbl.grid()
        count_down = False
        set_count_down_btn.config(text='Set time')

def initalize_count_down():
    h = int(hour_sb.get()) 
    m = int(min_sb.get()) 
    s = int(sec_sb.get()) 
    t_sec = h*3600+m*60+s 
    timer.initalize_count_down(t_sec)
# Create a Button
start_btn = Button(control_window, text = 'Start', command = start_timer)
pause_btn = Button(control_window, text = 'Pause', command = toggle_pause_continue)
stop_btn = Button(control_window, text = 'Reset', command = stop_timer)
set_count_down_btn = Button(control_window, text='Set time', command= set_count_down)

# Styling the label widget so that clock
# will look more attractive
wall_clock = Label(time_date_display_window, font = ('calibri', 16, 'bold'),
      background = 'black',
      foreground = 'white')

timer_lbl = Label(timer_display_window, font = ('calibri', 40, 'bold'),
      background = 'black',
      foreground = 'gold')


# Placing clock at the centre
# of the tkinter window
display_window.grid(row=0,column=1, sticky="NSEW")
control_window.grid(row=0, column=0, sticky="NSEW")

timer_display_window.grid(row=0, column=0, sticky="NSEW")
time_date_display_window.grid(row=1, column=0, sticky="NSEW")

wall_clock.grid(row=0, column=0, sticky="NSEW")
timer_lbl.grid(row=0, column=0, sticky="NSEW")
start_btn.grid(row=0, column=0, sticky="NSEW")
pause_btn.grid(row=1, column=0, sticky="NSEW")
stop_btn.grid(row=2, column=0, sticky="NSEW")
set_count_down_btn.grid(row=3, column=0, sticky="NSEW")
time()
update_timer_lbl()
mainloop()

