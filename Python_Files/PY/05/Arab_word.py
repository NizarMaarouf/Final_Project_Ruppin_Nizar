
# Step1: Import required packages
import sys
import scipy
import joblib
import matplotlib
import pandas as pd
from sklearn import svm
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from matplotlib import pyplot as plt
from mlxtend.plotting import plot_decision_regions
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import plot_confusion_matrix, accuracy_score, classification_report

# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

# Step2: Load dataset
Arabic_word = pd.read_csv(r'C:\Users\nizar.maarouf\Desktop\NIZAR\Arabic_Words.csv')

# input rong value 
wrong_input = pd.read_csv(r'C:\Users\nizar.maarouf\Desktop\NIZAR\wrong_input.csv')
wrong_input = wrong_input.values

# Step 3: Split the data in training and testing subsets

real_input = Arabic_word.drop(columns = ['Outcome' , 'Word'])
real_input = real_input.values
y = Arabic_word['Outcome']
x_tr, x_ts, y_tr, y_ts = train_test_split(real_input,y,test_size=0.1994 , random_state = 301 )

# Step 4: Classifier training using Support Vector Machine
model = svm.SVC(gamma="auto")
model.fit(x_tr,y_tr)
# joblib.dump(model, 'Arabic_word.joblib')

# Step 5: make predict on test data and see result
predict_vector = model.predict(x_ts)
# PREDICT THE REAL VALUE
predictions = model.predict(real_input)

# PREDET THE INPUT WRONG VALE
prediction_R = model.predict(wrong_input)

# if (predictions == 0):
#     predictions = [' Gtaa ']
# else:
#     predictions = [' Wasl ']
print('\n')
# Step 6: Check classifier accuracy on test data and see result
print("Accuracy: ",accuracy_score(y_ts, predict_vector))
print('The Outcome of the real input is : \n' ,predictions)

print('\n')

print('The Outcome of the wrong input is : \n' ,prediction_R)

print('\n')
# Step 7: plot the Confusion matrix for our classifier
# matrix = plot_confusion_matrix(model, x_ts, y_ts,cmap=plt.cm.Reds,normalize='true')
# plt.title('Confusion matrix for our classifier')
# plt.show()

print('\n')