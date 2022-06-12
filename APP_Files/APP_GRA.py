# ==============================
# WHAT IS THE WORD 
# GTAA OR WASL
# ==============================
# 41000202
# 26000203
# 78000201
# 56000111
# 66000111
# 56000402
# ==============================
# Gtaa Or Wasl Desktop App
# With Tkinter
# ==============================

import csv
from array import *
from tkinter import *
from tkinter import messagebox

# Create The Main App Window
GtaaOrWasl_app = Tk()

# Change App Text
GtaaOrWasl_app.title("Nizar GtaaOrWasl_app App")

# Set Dimensions
GtaaOrWasl_app.geometry("400x180")

# Write Age Label
the_text = Label(GtaaOrWasl_app, text="Enter a vector 8 digits", height=2, font=("Arial", 20))
the_text.pack()  # Place The Text Into The Main Window

# Age Variables
vector = StringVar()

# Set Default Value For Age
vector.set("")

# Create The Input For Age
vector_input = Entry(GtaaOrWasl_app, width=8, font=("Arial", 30), textvariable=vector)
vector_input.pack()  # Place The Input Into The Main Window


referencePath = (r'C:\Users\nizar.maarouf\Desktop\Final_Progect_Ruppin\PROGRAMING\TKINTER\Data.csv')
# function in click
def IsCorrectVector(givenVector):
    File = open(referencePath,'r',encoding="utf8")
    Reader = csv.reader(File)
    Data = list(Reader)
    returnValue = []
    for data  in Data:
        if((data) != ['', '', '', '', '', '', '', '', '', '']):
            if(data[1:len(data)- 1] == givenVector):
                returnValue = data
                break

    File.close()  

    return returnValue
    
def main(): 
  
    givenVector = vector.get() 
       
    full_vector=IsCorrectVector(list(givenVector))

    outcome = []

    if(full_vector != [] ):
        word = full_vector[0]
        outcome = full_vector[len(full_vector) - 1]
        if(outcome == '1'):
            outcome = 'هذه الكلمة تبدأ بهمزة الوصل'
        else:
            outcome = 'هذه الكلمة تبدأ بهمزة القطع'  
        # newVector = full_vector[1:len(full_vector)- 1]
        line_one = f"Found - {word}"
        line_two = f"outcome - {outcome}"

        all_lines = [line_one, line_two]

        messagebox.showinfo("Your Word is : ", "\n".join(all_lines))

    else:

        line_three = f"Wrong input {givenVector}"

        all_lines2 = [line_three]

        messagebox.showinfo("Your Word is : ", "\n".join(all_lines2))

    print('\n')

# Create The Grammer_App Button
btn = Button(GtaaOrWasl_app, text="GO", width=20,
height=2, bg="#e91e63", fg="white", borderwidth=0, command=main)
btn.pack()  # Place Button in The Main Window


# Run App Infinitely
GtaaOrWasl_app.mainloop()



