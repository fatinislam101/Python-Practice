import math
print(math.sqrt(16))
print(math.pi)
from math import sqrt
import math as m
print(sqrt(16))

import statistics
def describe(numbers):
    return{
        "mean":statistics.mean(numbers),
        "median":statistics.median(numbers),
        "max":max(numbers)
    }
print(describe([1, 2, 3, 4, 10]))   # expect mean 4, median 3, max 10
import helpers
print(helpers.double(21))