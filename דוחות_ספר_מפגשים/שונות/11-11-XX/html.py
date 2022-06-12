# import pandas as pd

# # create dataframe
# df_marks = pd.DataFrame({'name': ['nmm', 'ghj', 'sdf', 'tee'],
#      'physics': [68, 74, 77, 78],
#      'chemistry': [84, 56, 73, 69],
#      'algebra': [78, 88, 82, 87]})

# # render dataframe as html
# html = df_marks.to_html()
# print(html)# Write your code here :-)

# import pandas as pd

# #create dataframe
# df_marks = pd.DataFrame({'name': ['Somu', 'Kiku', 'Amol', 'Lini'],
#      'physics': [68, 74, 77, 78],
#      'chemistry': [84, 56, 73, 69],
#      'algebra': [78, 88, 82, 87]})

# #render dataframe as html
# html = df_marks.to_html()

# #write html to file
# text_file = open("index.html", "w")
# text_file.write(html)
# text_file.close()



# Python code to find Euclidean distance
# using linalg.norm()

# Import NumPy Library
import numpy as np

# initializing points in
# numpy arrays
point1 = np.array((2, 2, 1))
point2 = np.array((1, 1, 1))

# calculate Euclidean distance
# using linalg.norm() method
dist = np.linalg.norm(point1 - point2)

# printing Euclidean distance
print(dist)# Write your code here :-)