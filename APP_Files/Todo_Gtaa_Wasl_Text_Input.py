import csv
from array import *
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from turtle import color, left
from numpy import pad
# from matplotlib.ft2font import BOLD
from sklearn import svm    # linear algebra
import pandas as pd   # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split

# import warnings filter
from warnings import simplefilter

# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

# Create The Main App Window
GtaaOrWasl_app = Tk()
GtaaOrWasl_app.configure(bg='#F7AA00')
# Change App Text
GtaaOrWasl_app.title("Nizar GtaaOrWasl_App")

# Set Dimensions
GtaaOrWasl_app.geometry('1290x950+50+50')

# Write Victor Label
the_text = Label(GtaaOrWasl_app, bg='#F7AA00' ,text="Enter text", height=1, font=('Helvetica', 20, 'bold'),fg='#235784')
the_text.place(x = 20,
        y = 15,
        width=125,
        height=20)
# Create The Input For Given text
givenText_input = Text(GtaaOrWasl_app,bg='#BCDBDF',font=('Tohama', 18, 'bold'),fg='#132238', width=1250,height=15,padx=5)
givenText_input.tag_config('tag-right', justify='right')
givenText_input.insert('end', '  ', 'tag-right')
givenText_input.pack(padx=20 , pady=50)
#Functions

referencePath = (r'C:\Users\nizar.maarouf\Desktop\Final_Progect_Ruppin\APP_Files\DATA\Data.csv')

def WordToVector(givenWord):
    File = open(referencePath,'r',encoding="utf8")
    Reader = csv.reader(File)
    Data = list(Reader)
    returnValue = []
    for data  in Data:
        if((data) != ['', '', '', '', '', '', '', '', '', '']):
            if(data[0] == givenWord):
                returnValue = data
                break
         

    File.close()  
    
    return returnValue
    
def GoClickEvent():
    output_text.delete("1.0","end")
    givenParagraph = givenText_input.get("1.0", "end-1c") 

    givenParagraph = givenParagraph.replace('\n',' ')

    for word in givenParagraph.split(' '):
        givenWord = word.strip()
        
        if(givenWord == '' or givenWord == ' '):
            continue

        full_vector=WordToVector(givenWord)

        if(full_vector == []):
            continue

        givenVector = full_vector[1:len(full_vector)- 1]
        # Read the file data and make variable to trainning 
        data = pd.read_csv (r'C:\Users\nizar.maarouf\Desktop\Final_Progect_Ruppin\APP_Files\DATA\Data.csv').head(426)
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

        result = '' 

        if(predictions  == 0):
        #    result =  givenWord , '        Is start with HAMZAT GTAA '
            result = '  \t     هذه الكلمة تبدأ بهمزة القطع' 
        else:
            # result = givenWord , '        Is start with HAMZAT WASL '
            result = '  \t     هذه الكلمة تبدأ بهمزة الوصل'   
        
        output_text.insert(END, givenWord , 'tag-right')
        output_text.insert(END, '\t\t')
        output_text.insert(END, result , '\t')
        output_text.insert(END, '\n')


        # outcome = []
        # if(full_vector != [] ):
        #     #exist
        #     #Filter vector
        #     outcome = full_vector[len(full_vector) -1]
        #     newVector = full_vector[1:len(full_vector)- 1]
        #     output_text.insert(END, 'Found - '+givenWord)
        #     output_text.insert(END, '\t')
        #     output_text.insert(END, newVector)
        #     output_text.insert(END, '\t')
        #     output_text.insert(END, 'outcome - ' + outcome)
        #     output_text.insert(END, '\n\n')
            
        # else:
        #     # not exist
        #     output_text.insert(END, 'Wrong input - '+ givenWord)
        #     output_text.insert(END, '\n\n')



 

def ClearClickEvent():
    givenText_input.delete("1.0","end")

#End Functions


# Create The Grammer_App Button

btn = Button(GtaaOrWasl_app ,text='CLICK ME \n TO GET RESULT', font=('Helvetica', 30, 'bold') ,fg='#FEF9A7',bg='#235784',command=GoClickEvent)
btn.place(x = 800,
        y = 500,
        width=460,
        height=150)

clearBtn = Button(GtaaOrWasl_app ,text='Clear', font=('Helvetica', 30, 'bold') ,fg='#FEF9A7',bg='#235784',command=ClearClickEvent)
clearBtn.place(x = 800,
        y = 750,
        width=460,
        height=150)

Name = Label(GtaaOrWasl_app, text="Results",fg='#235784',width=25, bg='#F7AA00', height=1, font=('Helvetica', 20, 'bold'))
Name.place(x = 20,
        y = 460,
        width=100,
        height=40)


output_text = Text(GtaaOrWasl_app,height=10, font=('Tohama', 18, 'bold'),bg='#BCDBDF',fg='#132238',padx=20,pady=5)
output_text.tag_config('tag-right', justify='right')
output_text.place(x = 20,
        y = 500,
        width=750,
        height=400)


Name = Label(GtaaOrWasl_app, text="Performed by Nazar Marouf",fg='#235784',width=25, border=2,borderwidth=0 ,
 bg ='#F7AA00', height=2, font=('Helvetica', 20, 'bold'))
Name.place(x = 20,
        y = 905,
        width=360,
        height=40)



      
# Run App Infinitely
 
GtaaOrWasl_app.mainloop()
 







