from tkinter import *
from playsound import playsound
import math
# ---------------------------- CONSTANTS ------------------------------- #
BLUE = "#dae9fc"
CYAN = "#89d9e5"
GREEN = "#7da1ae"
PURPLE = "#9091e5"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=CYAN)
    elif reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=PURPLE)
    else:
        count_down(work_sec)
        timer_label.config(text="Work")


# ---------------------------- PLAY SOUND ------------------------------- #
def play():
    playsound('blue_hour.mp3')


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        play()
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✓"
        checkmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BLUE)

# Image
canvas = Canvas(width=400, height=400, bg=BLUE, highlightthickness=0)
txt_img = PhotoImage(file="txtclock.png")
canvas.create_image(200, 200, image=txt_img)
timer_text = canvas.create_text(200, 200, text="00:00", fill=GREEN, font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Labels
timer_label = Label(text="Timer", bg=BLUE, fg=GREEN, font=(FONT_NAME, 50))
timer_label.grid(row=0, column=1)

checkmark_label = Label(bg=BLUE, fg=GREEN)
checkmark_label.grid(row=3, column=1)

# Buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

# Keep window on screen
window.mainloop()

