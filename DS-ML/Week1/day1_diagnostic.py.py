#1.Fundamentals: Given nums = [4, 9, 2, 7, 9, 4, 1], print the sum, the maximum, and the list of unique values in sorted order.
nums=[4,9,2,7,9,4,1]
print(sum(nums))
print(max(nums))
print(sorted(set(nums)))
#2.Functions: Write average(values) that returns the mean of a list. It should return None for an empty list instead of crashing.
def average(values):
    if len(values)==0:
        return None
    return sum(values)/len(values)
print(average([2, 4, 6]))   # expect 4.0
print(average([]))          # expect None
print(average([10]))        # expect 10.0

#3.Dictionaries: Given text = "to be or not to be", build a dictionary counting each word, then print the most frequent word.

given="to be or not to be"
words=given.split()
print(words)
counts={}
for items in words:
   if items in counts:
       counts[items]+=1
   else:
       counts[items]=1

print(counts)
print(max(counts, key=counts.get))

#4.Next up: Problem 4. The comprehension concepts are in my earlier message. Using only the concepts from there:

#From range(1, 21), build a list of the squares of the even numbers only, in one list comprehension.
#Expected result: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400], which is 10 numbers.

squares=[n*n for n in range(1,21) if n%2==0]
print(squares)

#5.Strings and logic: Write is_palindrome(s) that ignores case and spaces, so "Never odd or even" returns True.

def is_palindrome(s):
    clean=s.lower().replace(" ","")
    return clean[::-1]==clean
print(is_palindrome("Never odd or even"))
print(is_palindrome("Hello"))      
#Files and errors: Write a function that reads a text file and returns its line count. If the file doesn’t exist, it should print a friendly message and return 0.

def line_count(filename):
    try:
        with open (filename) as f:
         lines=f.readlines()
         return len(lines)
            
    except FileNotFoundError:
        print("File does not exist,SORRY")
        return 0
print(line_count("notes.txt"))
print(line_count("missing.txt"))