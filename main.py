from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
NAVY = "#0C2B4E"
RED = "#e7305b"
GREEN = "#9bdeac"
GREY = "#F4F4F4"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_pomodoro():
    window.after_cancel(timer)
    global reps

    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    session_label.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_pomodoro():
    global reps
    reps += 1  # Count each session (work or break)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Every 8th rep -> long break
    if reps % 8 == 0:
        print("Long break 🌴")
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)

    # Every 2nd, 4th, 6th rep -> short break
    elif reps % 2 == 0:
        print("Short break ☕")
        title_label.config(text="Break", fg=GREY)
        count_down(short_break_sec)

    # Every odd rep (1st, 3rd, 5th, 7th) -> work session
    else:
        print("Work session 💻")
        print("Current reps:", reps)
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds == 0:
        count_seconds = "00"
    elif count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_pomodoro()
        complete_session = reps // 2
        mark = ""
        for _ in range(complete_session):
            mark += "✔"
            session_label.config(text=mark)
        # session_label.config(text=f"{"✔" * complete_session}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Technics 🍅")


canvas = Canvas(width=200, height=224, bg=NAVY, highlightthickness=0 )
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35,"bold"))
canvas.grid(row=1, column=1)


# Timer label
title_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=NAVY, fg=GREEN)
title_label.grid(row=0, column=1)

# START Button
start_button = Button(text="Start", command=start_pomodoro, bg=GREEN, font=(FONT_NAME, 12,"bold"))
start_button.grid(row=2, column=0)

# RESET Button
reset_button = Button(text="Reset", command=reset_pomodoro, bg=RED, fg=GREY, font=(FONT_NAME, 12,"bold"))
reset_button.grid(row=2, column=2)

# Session label
session_label = Label(text="", font=(FONT_NAME, 12, "bold"), bg=NAVY, fg=GREY)
session_label.grid(row=3, column=1)


window.mainloop()