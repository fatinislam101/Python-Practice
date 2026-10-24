def power(base,exponent=2):
    return base**exponent
print(power(3))
print(power(2,3))

def count_above(numbers,limit=0):
    counter=0
    for num in numbers:
        if num>limit:
            counter+=1
    return counter
print(count_above([1, 5, 8, 3], 4))   # expect 2
print(count_above([1, -2, 3]))        # expect 2

def most_common(text):
 
  words=text.split()
  count={}
  for word in words:
      if word in count:
         count[word]+=1
      else:
         count[word]=1
  return max(count,key=count.get)
print(most_common("to be or not to be to"))   # expect to




