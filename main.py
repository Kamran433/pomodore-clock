import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#FBEEC1"
GREEN = "#659DBD"
YELLOW = "#DAAD86"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
S = 0
Timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(Timer)
    tick.config(text="",background=YELLOW)
    canvas.itemconfig(m, text="00:00")
    timer.config(text="Timer",fg=RED)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    countdown(S, WORK_MIN, SHORT_BREAK_MIN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(S, WORK_MIN,SHORT_BREAK_MIN):
     global Timer
     timer.config(text="Timer", fg=RED)
     global tick
     canvas.itemconfig(m, text=f"{str(WORK_MIN).zfill(2)}:{str(S).zfill(2)}")
     if (S>0 and WORK_MIN>=0):
         Timer = window.after(1000, countdown, S - 1,WORK_MIN,SHORT_BREAK_MIN)
     if(S==0):
         if(WORK_MIN>0):
             S = 60
             window.after(1000, countdown, S - 1,WORK_MIN-1,SHORT_BREAK_MIN)
     if(WORK_MIN==0 and S==0):
         tick.config(text="✔")
         tick.grid(row=2, column=1)
         Breaking(S, SHORT_BREAK_MIN)
def Breaking(S,SHORT_BREAK_MIN):
    global Timer
    timer.config(text="Break",fg=GREEN)
    canvas.itemconfig(m, text=f"{str(SHORT_BREAK_MIN).zfill(2)}:{str(S).zfill(2)}")
    if (S > 0 and SHORT_BREAK_MIN >= 0):
        Timer=window.after(1000, Breaking, S - 1, SHORT_BREAK_MIN)
    if (S == 0):
        if (SHORT_BREAK_MIN > 0):
            S = 60
            window.after(1000, Breaking, S - 1,SHORT_BREAK_MIN-1)
    if (SHORT_BREAK_MIN == 0 and S==0):
        secondshift(S,WORK_MIN)
        return
def secondshift(S,WORK_MIN):
    global Timer
    timer.config(text="Timer",fg=RED)
    canvas.itemconfig(m, text=f"{str(WORK_MIN).zfill(2)}:{str(S).zfill(2)}")
    if (S > 0 and WORK_MIN >= 0):
        Timer=window.after(1000, secondshift, S - 1, WORK_MIN)
    if (S == 0):
        if (WORK_MIN > 0):
            S = 60
            window.after(1000, secondshift, S - 1, WORK_MIN - 1)
    if (WORK_MIN == 0 and S == 0):
        tick.config(text="✔✔")
        tick.grid(row=2, column=1)
        Breaking2(S,SHORT_BREAK_MIN)
def Breaking2(S,SHORT_BREAK_MIN):
    global Timer
    timer.config(text="Break",fg=GREEN)
    canvas.itemconfig(m, text=f"{str(SHORT_BREAK_MIN).zfill(2)}:{str(S).zfill(2)}")
    if (S > 0 and SHORT_BREAK_MIN >= 0):
        Timer=window.after(1000, Breaking2, S - 1, SHORT_BREAK_MIN)
    if (S == 0):
        if (SHORT_BREAK_MIN > 0):
            S = 60
            window.after(1000, Breaking2, S - 1,SHORT_BREAK_MIN-1)
    if (SHORT_BREAK_MIN == 0 and S==0):
        thirdshift(S,WORK_MIN)
        return
def thirdshift(S, WORK_MIN):
    global Timer
    timer.config(text="Timer",fg=RED)
    canvas.itemconfig(m, text=f"{str(WORK_MIN).zfill(2)}:{str(S).zfill(2)}")
    if (S > 0 and WORK_MIN >= 0):
        Timer=window.after(1000, thirdshift, S - 1, WORK_MIN)
    if (S == 0):
        if (WORK_MIN > 0):
            S = 60
            window.after(1000, thirdshift, S - 1, WORK_MIN - 1)
    if (WORK_MIN == 0 and S == 0):
        tick.config(text="✔✔✔")
        tick.grid(row=2, column=1)
        Breaking3(S, LONG_BREAK_MIN)
def Breaking3(S,LONG_BREAK_MIN):
    global Timer
    timer.config(text="Break",fg=GREEN)
    canvas.itemconfig(m, text=f"{str(LONG_BREAK_MIN).zfill(2)}:{str(S).zfill(2)}")
    if (S > 0 and LONG_BREAK_MIN >= 0):
        Timer=window.after(1000, Breaking3, S - 1, LONG_BREAK_MIN)
    if (S == 0):
        if (LONG_BREAK_MIN > 0):
            S = 60
            window.after(1000, Breaking3, S - 1,LONG_BREAK_MIN-1)
    if (LONG_BREAK_MIN == 0 and S==0):
        tick.config(text="✔well-done✔",font=("Didot",12,"italic"))
        tick.grid(row=2, column=1)
        return
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
j= True
window.config(padx=50,pady=50,highlightthickness=0,bg=YELLOW)
window.minsize(width=200,height=200)
window.title("POMODORE")
imageshow = tkinter.PhotoImage(file = "clock.png")
canvas= tkinter.Canvas(width=210,height=210,bg=YELLOW,highlightbackground=YELLOW)
canvas.create_image(110,110,image=imageshow)
m=canvas.create_text(113,130,text="00:00",font=("Proxima Nova",30,"italic","bold"),fill="white")
canvas.grid(row=1,column = 1)
resetbutton = tkinter.Button(text="Reset",command=reset,highlightbackground=YELLOW)
resetbutton.grid(row=2,column=2)
startbutton = tkinter.Button(text="Start",command=start,highlightbackground=YELLOW)
startbutton.grid(row=2,column=0)
timer = tkinter.Label(text="Timer",font=("Courier",30,"bold"),fg="#D2042D",background=YELLOW)
timer.grid(row=0,column = 1)
tick = tkinter.Label(text="✔",fg="#7CFC00",background=YELLOW)
tkinter.mainloop()