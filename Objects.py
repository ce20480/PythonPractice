class PartyAnimal:
    x = 0# each obhect made from the class will have data 
    name = ""
    def __init__(self, name) -> str: # constructor is optional used for setting up variables
        self.name = name
        print(self.name, 'is constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name, 'so far party count', self.x)
    # def __del__(self) -> str: # destructor rarely used
    #     print('I am destructed', self.x) problem is that if you dont use object later on it deletes it

# an = PartyAnimal() # Constructing an instance/object of the class
# print('Type: ', type(an))
# print('Dir: ', dir(an))
# an.party() # Same as writing PartyAnimal.party(an)
# an.party()
# an.party()
# an = 42 # this is when our previous will be destroyed and replaced with 42 so the del function will run and now is an integer
# print('an contains, ', an)

'''
making 2 instances of the same class
'''
s = PartyAnimal('Sally')
s.party()
j = PartyAnimal('Jelly')
j.party()
s.party()

# x = list()
# type(x) # returns type of x which is a list object
# dir(x) # tells you about capabilities of list class all __something__ are predefined functions but others are functions which we can use
'''
inheritance
'''
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

j = FootballFan('Jim')
j.party()
j.touchdown()