def only_positive(numbers):
    result=[]
    for n in numbers:
        if n>0:
            result.append(n)
    return result

print(only_positive([3, -1, 0, 7, -5]))   # expect [3, 7]
def running_total(numbers):
    result=[]
    total=0
    for n in numbers:
        total+=n
        result.append(total)
    return result
print(running_total([1, 2, 3, 4]))   # expect [1, 3, 6, 10]

def top_three(numbers):
    ordered=sorted(numbers,reverse=True)
    return ordered[:3]

print(top_three([4, 9, 2, 7, 9, 1]))   # expect [9, 9, 7]
    