
# Step1: Import required packages
import sys
import scipy
import joblib

import pandas as pd
from sklearn import svm
from sklearn.svm import SVC
from sklearn.svm import LinearSVC


from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import plot_confusion_matrix, accuracy_score, classification_report

# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

# Step2: Load dataset
Arabic_word = pd.read_csv(r'C:\Users\nizar.maarouf\Desktop\Final_Progect_Ruppin\APP_Files\DATA\Data.csv')

# input wrong value 
wrong_input = pd.read_csv(r'C:\Users\nizar.maarouf\Desktop\Final_Progect_Ruppin\APP_Files\DATA\wrong_input.csv')
wrong_input = wrong_input.values

# input real value 
real_input = pd.read_csv(r'C:\Users\nizar.maarouf\Desktop\Final_Progect_Ruppin\APP_Files\DATA\real_input.csv')
real_input = real_input.values


# Step 3: Split the data in training and testing subsets
x = Arabic_word.drop(columns = ['Outcome' , 'Word'])
x = x.values
y = Arabic_word['Outcome']
x_tr, x_ts, y_tr, y_ts = train_test_split(x,y,test_size=0.35 )

# Step 4: Classifier training using Support Vector Machine
model = svm.SVC(gamma="auto")
model.fit(x_tr,y_tr)
# joblib.dump(model, 'Arabic_word.joblib')

# Step 5: make predict on test data and see result
predict_vector = model.predict(x_ts)
# PREDICT THE REAL VALUE
predictions = model.predict(real_input)
# predictions = model.predict([[4,2,0,0,0,1,0,3]])
# PREDICT THE INPUT WRONG VALE
prediction_R = model.predict(wrong_input)

# if (predictions == 0):
#      predictions = [' Gtaa ']
# else:
#      predictions = [' Wasl ']
print('\n')
# Step 6: Check classifier accuracy on test data and see result
print("Accuracy: ",accuracy_score(y_ts, predict_vector))
print('\n')
print('The Outcome of the real input is : \n' ,predictions)

print('\n')

print('The Outcome of the wrong input is : \n' ,prediction_R)

# print('\n')
# Step 7: plot the Confusion matrix for our classifier
# matrix = plot_confusion_matrix(model, x_ts, y_ts,cmap=plt.cm.Reds,normalize='true')
# plt.title('Confusion matrix for our classifier')
# plt.show()

print('\n')