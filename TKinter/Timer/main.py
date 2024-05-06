from tkinter import *
import math


# ---------------------- CONSTANTS ---------------------- #
PINK = '#e2979c'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT_NAME = 'Courier'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

#---------------------- TIMER RESET ---------------------- #

def reset():
  win.after_cancel(timer)
  canvas.itemconfig(timer_text, text='00:00')
  timer_label.config(text='Timer', font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
  check_label.config(text='', font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
  global reps
  reps = 0

#---------------------- TIMER MECHANISM ------------------ #


def start_timer():
  global reps
  reps +=1
  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN * 60
  if reps == 8:
  # 8th
    count_down(long_break_sec)
    timer_label.config(text='Break', fg=RED)
  elif reps % 2 == 0:
    # 2nd/4th/6th
    count_down(short_break_sec)
    timer_label.config(text='Break', fg=PINK)
  else:
    # 1st/3rd/5th/7th
    count_down(work_sec)
    timer_label.config(text='Work', fg=GREEN)
#---------------------- COUNTDOWN MECHANISM -------------- #
def count_down(count):
  count_min = math.floor(count / 60)
  count_sec = count % 60
  if count_sec <= 9:
    count_sec = f"0{count_sec}"

  if count_sec == 0:
    count_sec = "00"


  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count > 0:
    global timer
    timer = win.after(1000, count_down, count - 1)
  else:
    start_timer()
    check = ""
    mark = math.floor(reps / 2)
    for i in range(mark):
      check += "✔"
    check_label.config(text=check)

#---------------------- UI SETUP ------------------------- #
win = Tk()
win.title('Pomodoro')
win.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW)
img = PhotoImage(file='Pomodoro.png')
canvas.create_image(100, 112, image=img)
canvas.grid(row=1, column=1)
timer_text = canvas.create_text(100, 170, text='00:00', fill='white', font=(FONT_NAME, 20, 'bold'))



start_button = Button(text='Start', highlightthickness=0, bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', highlightthickness=0, bg=YELLOW, command=reset)
reset_button.grid(column=2, row=2)

timer_label = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_label = Label( font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)





win.mainloop()

