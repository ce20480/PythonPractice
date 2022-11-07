'''
learning about classes
'''
import math
import random
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

'''
Class inheritance - child classes which inherits the init function from the parents(the attributes)
'''

class NamedFraction(MyFraction):

    def __init__(self, num, den, name=False):
        '''
        Attributes specific to child class and can only be done by using super() fucntion
        '''
        super().__init__(num,den)#initialise super class( which is the one that you have derived your new class from) this allows you to create more attributes in this child class
        self.name = name

    def sig_fig(self, n):
        return round(super().eval(), n) #this is another way to do it ( this always gives you the inherited version of eval)
        #return round(self.eval(), n) # if you do not change the function that you use from the parent in the child you can do it this way
    
    # def eval(self):
    #     inv = 1 - round(super().eval(),0)
    #     ran = random.normalvariate(1,0)
    #     num = ran * round(super().eval(),0)
    #     den = ran * inv
    #     return MyFraction(num,den)
    
    def __str__(self):
        return 'This is: ' + self.name + '\n' + \
               '{:^5}'.format(self.num) + '\n' + \
               '----' + '\n' + \
               '{:^5}'.format(self.den)

nfrac = NamedFraction(2,6, 'Third')
print(nfrac)


