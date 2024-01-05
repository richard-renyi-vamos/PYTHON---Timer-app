import tkinter as tk
from tkinter import colorchooser
from datetime import timedelta

def update_time():
    global time_remaining
    label.config(text=str(time_remaining))
    if time_remaining > timedelta(seconds=0):
        time_remaining -= timedelta(seconds=1)
        label.after(1000, update_time)

def set_time():
    global time_remaining
    try:
        hours = int(entry_hours.get())
        minutes = int(entry_minutes.get())
        seconds = int(entry_seconds.get())
        time_remaining = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        update_time()
    except ValueError:
        label.config(text="Invalid time format!")

def change_text_color():
    color = colorchooser.askcolor(title="Choose text color")[1]
    label.config(fg=color)

def toggle_always_on_top():
    root.attributes("-topmost", not root.attributes("-topmost"))

time_remaining = timedelta()

root = tk.Tk()
root.title("Timer App")

# Entry widgets to set time
entry_hours = tk.Entry(root, width=5)
entry_hours.insert(tk.END, "0")
entry_hours.grid(row=0, column=0)
label_hours = tk.Label(root, text="hours")
label_hours.grid(row=0, column=1)

entry_minutes = tk.Entry(root, width=5)
entry_minutes.insert(tk.END, "0")
entry_minutes.grid(row=0, column=2)
label_minutes = tk.Label(root, text="minutes")
label_minutes.grid(row=0, column=3)

entry_seconds = tk.Entry(root, width=5)
entry_seconds.insert(tk.END, "0")
entry_seconds.grid(row=0, column=4)
label_seconds = tk.Label(root, text="seconds")
label_seconds.grid(row=0, column=5)

# Button to set time
set_button = tk.Button(root, text="Set Time", command=set_time)
set_button.grid(row=1, columnspan=6)

# Label to display timer
label = tk.Label(root, text="00:00:00", font=("Arial", 24), pady=10)
label.grid(row=2, columnspan=6)

# Button to change text color
color_button = tk.Button(root, text="Change Text Color", command=change_text_color)
color_button.grid(row=3, columnspan=6)

# Button to toggle always on top
always_on_top_button = tk.Button(root, text="Toggle Always on Top", command=toggle_always_on_top)
always_on_top_button.grid(row=4, columnspan=6)

root.mainloop()
