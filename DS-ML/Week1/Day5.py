def discount(price,percent=10):
    discounted_price=price*percent/100
    new_price=price-discounted_price
    return new_price
print(discount(200))       # expect 180.0
print(discount(200, 50))   # expect 100.0

def word_lengths(words):
    return[len(word) for word in words]
print(word_lengths(["data", "science", "is", "fun"]))   # expect [4, 7, 2, 3]

def count_letters(words):
    count={}
    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    return count


print(count_letters("banana"))   # expect {'b': 1, 'a': 3, 'n': 2}

def to_number(text):
    try:
        return int(text)
    except ValueError:
        return None
print(to_number("42"))     # expect 42
print(to_number("abc"))    # expect None

def average_positive(numbers):
    total = 0
    count = 0
    for n in numbers:
        if n > 0:
            total += n
            count += 1
    if count==0:
        return None
    return total / count

print(average_positive([4, -2, 6]))
print(average_positive([-1, -2]))
print(average_positive([4, -2, 6]))   # 5.0
print(average_positive([-1, -2]))     # None
print(average_positive([-1, 5]))      # 5.0