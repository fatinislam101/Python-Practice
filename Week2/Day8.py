import numpy as np
arr=np.array([10,20,30,40])
print(arr*3)
print(arr.sum())
print(arr.mean())

scores = np.array([45, 80, 62, 30, 91, 50])

print(scores[scores>50])   # the scores above 50
print(len(scores[scores>50]))   # how many there are


marks = np.array([[70, 80],
                  [65, 90],
                  [88, 75]])

print(marks.shape)   # the shape
print(marks[1])   # the marks of the second student (whole row)
print(marks[0,1])   # the first student's mark in the second subject
