import tkinter
from tkinter import BOTH, StringVar, IntVar, DISABLED, NORMAL
import COVID19Py
from time import strftime
from PIL import Image, ImageTk


covid_window = tkinter.Tk()
covid_window.title("Covid-19 Tracker")
covid_window.geometry("400x450")
covid_window.resizable(0, 0)
covid_window.iconbitmap(corona.ico")

# Define colours and fonts
turquoise = "#72EFDD"
light_blue = "#56CFE1"
dark_blue = "#4EA8DE"
text_font = ("Rubrik", 12)
title_font = ("Consolas", 15)


# Set up Covid api
covid19 = COVID19Py.COVID19(data_source="jhu")


# Change the main window's background colour
covid_window.config(bg=dark_blue)


# Define layout
# Define frames
title_frame = tkinter.Frame(covid_window, bg=light_blue)
title_frame.pack(padx=5, pady=5, ipadx=100)
case_frame = tkinter.Frame(covid_window, bg=turquoise)
case_frame.pack(padx=5, pady=5)


# Define functions
def clock():
    """Create a simple clock that actively changes time."""
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, clock)


lbl = tkinter.Label(title_frame, font=title_font, background=turquoise, foreground="black")


def get_cases():
    """Get response from pyCovid tracker API."""
    confirmed_cases = covid19.getLatest()
    confirmed_label = tkinter.Label(case_frame, text="Confirmed Cases: " + str(confirmed_cases["confirmed"]), font=title_font, bg=dark_blue)
    confirmed_label.grid(row=0, column=0, padx=5, pady=5)

    latest_deaths = tkinter.Label(case_frame, text="Confirmed Deaths: " + str(confirmed_cases["deaths"]), font=title_font, bg=dark_blue)
    latest_deaths.grid(row=1, column=0, padx=5, pady=5)

    latest_recoveries = tkinter.Label(case_frame, text="Confirmed Recoveries: " + str(confirmed_cases["recovered"]), font=title_font, bg=dark_blue)
    latest_recoveries.grid(row=2, column=0, padx=5, pady=5)


def show_guide():
    """Show a covid safety help guide in a second window"""
    # Image 'help_image' needs to be a global variable to put on our window
    # Window 'guide' needs to be global to close in another function
    global help_image
    global guide

    # Create a second window relative to the covid_window window
    guide = tkinter.Toplevel()
    guide.title("Covid Safety Guide")
    guide.iconbitmap("corona.ico")
    guide.geometry("350x450+" + str(covid_window.winfo_x() + 400) + "+" + str(covid_window.winfo_y()))
    guide.config(bg=dark_blue)

    # Create the image, label
    help_image = ImageTk.PhotoImage(Image.open("covid safety sheet.png"))
    label = tkinter.Label(guide, image=help_image, bg=light_blue)
    label.pack(padx=10, pady=10, ipadx=5, ipady=5)

    # Create a close button
    close_button = tkinter.Button(guide, text="Close", font=text_font, bg=light_blue, command=hide_guide)
    close_button.pack(padx=10, ipadx=50)

    # Disable the guide button
    guide_button.config(state=DISABLED)


def hide_guide():
    """Hide the guide"""
    guide_button.config(state=NORMAL)
    guide.destroy()


lbl.grid(row=3, column=1, padx=5, pady=20)
clock()

# Define title layout
title_label = tkinter.Label(title_frame, text="Covid-19 Case Tracker", font=title_font, bg=turquoise, width=35)
title_label.grid(row=0, column=1)

# Create the get cases button
get_cases_button = tkinter.Button(title_frame, text="GET CASES", font=title_font, bg=turquoise, command=get_cases)
get_cases_button.grid(row=4, column=1, padx=30, pady=15, ipadx=50)

# Create help button
guide_button = tkinter.Button(title_frame, text="HELP", font=title_font, bg=turquoise, command=show_guide)
guide_button.grid(row=5, column=1, padx=30, pady=15, ipadx=78)

# Create quit button
quit_button = tkinter.Button(title_frame, text="QUIT", font=title_font, bg=turquoise, command=covid_window.destroy)
quit_button.grid(row=6, column=1, padx=30, pady=15, ipadx=78)


covid_window.mainloop()

