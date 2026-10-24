#Day 2: Reading Error Messages and Debugging
prices = {"tea": 20, "coffee": 35}
print(prices.get("juice","Juice is not available"))     # ask for "juice" safely, with a default of "not available"
def total(values):
    result = 0
    for v in values:
        result += v
    return result

print(total([1, 2, 3]))

#ages = [20, "22", "abc", "22.5", None]

def safe_gate(d,key):
    return d.get(key,"not found")

prices = {"tea": 20, "coffee": 35}
print(safe_gate(prices, "tea"))      # 20
print(safe_gate(prices, "juice"))    # not found
