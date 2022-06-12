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
# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

GtaaOrWasl_app = Tk()
GtaaOrWasl_app.title('Does the word start with the HAMZET "Wasl or Gtaa"?')
GtaaOrWasl_app.geometry('500x300')

# create clear function 
def Clear():
    input_text.delete(1.0 , END)

# grap the text from text box
def Get_text():
    output_text.config(text = input_text.get(1.0 , END))

input_text = Text(GtaaOrWasl_app , width=8 , height=1 , font=('helvetica' , 20))
input_text.pack(pady=20)



button_frame = Frame(GtaaOrWasl_app)
button_frame.pack()

clear_button = Button(button_frame , text='Clear Input' ,bg='red',font=( 'helvetica',13),width=10,height=1, command=Clear)   
clear_button.grid(row=0 , column=0)  

get_text_button = Button(button_frame , text='SEARCH',bg='green',font=( 'helvetica',13),width=10,height=1, command=Get_text)
get_text_button.grid(row=0 , column=1 , padx=20)

output_text = Label(GtaaOrWasl_app , background='white',fg='red', width=20 , height=3, text='',font=('helvetica' , 15))
output_text.pack(pady=20)


GtaaOrWasl_app.mainloop()