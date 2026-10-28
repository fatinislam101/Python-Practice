# axis tells NumPy which direction to work in.

# axis=0 goes down the rows, giving one result per column.
# axis=1 goes across the columns, giving one result per row.
import numpy as np
marks = np.array([[70, 80],
                  [65, 90],
                  [88, 75]])

print(marks.mean(axis=0))   # average per subject
print(marks.mean(axis=1))   # average per student

a = np.arange(1,13)
b = a.reshape(3,4)
print(b)
print(b.shape)   # the shape
marks = np.array([[70, 80],
                  [65, 90],
                  [88, 75]])
bonus = np.array([5, 10])

print(marks+bonus)