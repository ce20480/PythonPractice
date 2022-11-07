'''
learning about classes
'''
import math
class MyFraction():
    '''Constructor is the init'''
    def __init__(self, num, den):# the init function will automatically be called when the class is called
        '''Class attributes'''
        self.num = num
        self.den = den
        self.normalize() # so you can either put it into the init and force it to happen or allow the user to use the function outside the class on their own

    def normalize(self):
        gcd = math.gcd(self.num, self.den)
        self.num = int(self.num / gcd)
        self.den = int(self.den / gcd)
    
    def eval(self):# you can redefine a built in function for a class and then use the built-in function on data not belonging to the class
        return (self.num/self.den)

    def __float__(self):# redefined float for class
        return (self.num/self.den)
    
    def __str__(self):# redefined string for our class and we can use print normally
        return (" " + str(self.num) + "\n---\n" + " " + str(self.den) + "\n")

    def __add__(self, other):
        cd = self.den * other.den
        cn = (self.num * other.den) + (other.num *self.den)
        return (MyFraction(cn,cd))
    
    def __sub__(self, other):
        cd = self.den * other.den
        cn = (self.num * other.den) - (other.num *self.den)
        return (MyFraction(cn,cd))
    
    def __truediv__(self, other):# to get divide you have to use truediv 
        den = self.den * other.num
        num = self.num * other.den
        return (MyFraction(num,den))
    
    def __mul__(self,other):
        den = self.den * other.den
        num = self.num * other.num
        return (MyFraction(num,den))

fraction = MyFraction(2,4)
fraction2 = MyFraction(3,4)
print(fraction / fraction2) # now can output a nice print because of def __str__

x = 1
print(eval('x+1'))# normal use of eval is to evaluate a string not as a string




