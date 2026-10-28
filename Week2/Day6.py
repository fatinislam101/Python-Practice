class Player:
    def __init__(self,name,goals):
        self.name=name
        self.goals=goals
    def score(self):
        self.goals+=1
p=Player("Rafi",3)
p.score()
print(p.name,p.goals)

class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
r = Rectangle(3, 4)
print(r.area())   # expect 12

class counter:
    def __init__(self):
        self.count=0
    def add(self):
       self.count+=1
    def get(self):
        return self.count
c = counter()
c.add()
c.add()
c.add()
print(c.get())   # expect 3
class Cart:
    def __init__(self):
        self.prices=[]
    def add(self,price):
        self.prices.append(price)
    def total(self):
        return sum(self.prices)
cart = Cart()
cart.add(50)
cart.add(30)
cart.add(20)
print(cart.total())   

#Output:100