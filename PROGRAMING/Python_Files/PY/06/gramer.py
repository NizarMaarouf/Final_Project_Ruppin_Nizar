# ==============================
# WHAT IS THE WORD 
# GTAA OR WASL
# ==============================
# 26000203   قطع
# 32000102   وصل 
# 40100201   قطع
# 20010101   قطع
# 76000111   وصل
# 76000113   وصل
# 66000111   وصل
# 86000503   قطع
# ==============================
# Gtaa Or Wasl Desktop App
# With Tkinter
# ==============================

from array import *
from tkinter import *
from tkinter import messagebox
from sklearn import svm    # linear algebra
import pandas as pd   # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split

# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

# Create The Main App Window
GtaaOrWasl_app = Tk()

# Change App Text
GtaaOrWasl_app.title("Nizar GtaaOrWasl_App")

# Set Dimensions
GtaaOrWasl_app.geometry("400x250")

# Write Victor Label
the_text = Label(GtaaOrWasl_app, text="Enter a vector 8 digits", height=2, font=("Arial", 20))
the_text.pack()  # Place The Text Into The Main Window

# Vector Variables
vector = StringVar()

# Set Default Value For Vector
vector.set("")

# Create The Input For Vector_input
vector_input = Entry(GtaaOrWasl_app, width=8, font=("Arial", 30), textvariable=vector)
vector_input.pack()  # Place The Input Into The Main Window

# function in click
def main():

    givenVector = vector.get() 
    givenVector = [int(x) for x in str(givenVector)]

    data = pd.read_csv (r'C:\Users\nizar.maarouf\Desktop\Final_Progect_Ruppin\DATA\CSV_Files\Data.csv').head(426)
    data.drop('Word', inplace = True, axis=1)
    y = data['Outcome']
    x = data.drop(["Outcome"], axis = 1)
    x = x.values
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state =0)
    # Trainning the data input by vsm algorithim 
    vsm_model = svm.SVC(gamma="auto")
    vsm_model.fit(x_train, y_train)
    # Predict the result of trainning the data
    Input_Vector = [givenVector]
    # prediction = vsm_model.predict(x_test)
    predictions = vsm_model.predict(Input_Vector)
        
    if(predictions  == 0):
        result = 'هذه الكلمة تبدأ بهمزة القطع' 
        line_one = f"outcome - {result}" 
        messagebox.showinfo("Your Word is : \n",line_one)
    else:
        result = 'هذه الكلمة تبدأ بهمزة الوصل'   
        line_two = f"outcome - {result}"
        messagebox.showinfo("Your Word is :\n ", line_two)

    print('\n')

# Create The Grammer_App Button
btn = Button(GtaaOrWasl_app, text="GO", width=15,
height=3, bg="#e91e63", fg="white", borderwidth=0, command=main)
btn.pack(pady=10)  # Place Button in The Main Window

Name = Label(GtaaOrWasl_app, text="Performed by Nazar Maruf",width=25, border=2,borderwidth=0 , bg ='#e91e63', height=2, font=("Arial", 15))
Name.pack()  # Place The Text Into The Main Window
# Run App Infinitely
GtaaOrWasl_app.mainloop()

