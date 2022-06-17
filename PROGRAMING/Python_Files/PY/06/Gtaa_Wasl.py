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

# import csv
from array import *
from tkinter import *
from tkinter import messagebox
from sklearn import svm
import numpy as np    # linear algebra
import pandas as pd   # data processing, CSV file I/O (e.g. pd.read_csv)
# import sys
# import scipy
# import matplotlib
# import joblib
# from mlxtend.plotting import plot_decision_regions
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import plot_confusion_matrix, accuracy_score, classification_report
# from matplotlib import pyplot as plt

# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)
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

# function in click
def main():
    givenVector = vector.get() 
    givenVector = [int(x) for x in str(givenVector)]
    df = pd.read_csv (r'C:\Users\nizar.maarouf\Desktop\Final_Progect_Ruppin\APP_Files\Data.csv').head(426)
    data = df
    data.drop('Word', inplace = True, axis=1)
    y = data['Outcome']
    x = data.drop(["Outcome"], axis = 1)
    x = x.values
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state =0)
    vsm_model = svm.SVC(gamma="auto")
    vsm_model.fit(x_train, y_train)
    Input_Vector = [givenVector]
    predictions = vsm_model.predict(Input_Vector)
        
    if(predictions  == 0):
        result = 'هذه الكلمة تبدأ بهمزة القطع'
        
        line_one = f" {result}"
        # all_lines = [line_one]
        messagebox.showinfo("Your Word is : \n",line_one)

    else:
        result = 'هذه الكلمة تبدأ بهمزة الوصل' 
         
        line_two = f"{result}"
        # all_lines1 = [line_two]
        messagebox.showinfo("Your Word is :\n ", line_two)

    print('\n')

# Create The Grammer_App Button
btn = Button(GtaaOrWasl_app, text="GO", width=20,
height=2, bg="#e91e63", fg="white", borderwidth=0, command=main)
btn.pack()  # Place Button in The Main Window


# Run App Infinitely
GtaaOrWasl_app.mainloop()
 # if(outcome == [] ):
# if (predictions == 0):
    #       predictions = ' قطع '
    # elif(predictions == 1):
    #      predictions = ' وصل '
    # else:
    #      predictions = ' هذه الكتمة لا تبدأ بهمزة وصل أو قطع '  

    # print(' هذه الكتمة تبدأ بهمز  : ' , predictions)
# newVector = full_vector[1:len(full_vector)- 1]
