class Account:
    def __init__(self):
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount
       
        return self.balance
    def withdraw(self,amount):
        if amount>self.balance:
            return False
        else:
            self.balance-=amount
            return True
a = Account()
a.deposit(100)
print(a.withdraw(30))    # expect True
print(a.withdraw(100))   # expect False
print(a.balance)         # expect 70

from math import pi
def circle_area(radius):
    x=pi*radius*radius
    
    return round(x,2)
print(circle_area(2))    # expect 12.57
print(circle_area(1))    # expect 3.14
import numpy as np
def normalize(numbers):
    arr=np.array(numbers)
    return arr/np.max(numbers)

print(normalize([2, 5, 10]))   # expect [0.2 0.5 1. ]
print(normalize([50, 25]))     # expect [1.  0.5]
   
import numpy as np

marks = np.array([[60, 70, 80],
                  [90, 85, 95],
                  [40, 50, 60]])

averages = marks.mean(axis=1)
print(averages)
print(len(averages[averages>70]))   # how many averages are above 70 

import numpy as np

a = np.arange(1, 13)
b = a.reshape(3, 4)
print(b.sum(axis=1))