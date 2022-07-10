# ==============================
# Calculate Your Age Desktop App
# With Tkinter
# ==============================

from tkinter import *
from tkinter import messagebox

# Create The Main App Window
age_app = Tk()

# Change App Text
age_app.title("Elzero Calculate Age App")

# Set Dimensions
age_app.geometry("400x200")

# Write Age Label
the_text = Label(age_app, text="Write Your Age", height=2, font=("Arial", 20))
the_text.pack()  # Place The Text Into The Main Window

# Age Variables
age = StringVar()

# Set Default Value For Age
age.set("00")

# Create The Input For Age
age_input = Entry(age_app, width=2, font=("Arial", 30), textvariable=age)
age_input.pack()  # Place The Input Into The Main Window

def calc():

  # Get Age In Years
  the_age_value = age.get()

  # Get Time Units
  months = int(the_age_value) * 12
  weeks = months * 4
  days = int(the_age_value) * 365

  line_one = f"Your Age In Months Is: {months}"
  line_two = f"Your Age In Weeks Is: {weeks}"
  line_three = f"Your Age In Days Is: {days}"

  # List Contain All Lines
  all_lines = [line_one, line_two, line_three]

  # Message Box To Show All Lines
  messagebox.showinfo("Your Age In All Time Units", "\n".join(all_lines))

# Create The Calculate Button
btn = Button(age_app, text="Calculate Age", width=20,
height=2, bg="#e91e63", fg="white", borderwidth=0, command=calc)
btn.pack()  # Place Button in The Main Window

# Run App Infinitely
age_app.mainloop()