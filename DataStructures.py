# Dictionary and Nested lists and tuple and sets learning 
'''
lists
'''
# Can map matrices using nested lists 
student_list = [ ['John', 68, False], 
                 ['Sarah', 75, True], 
                 ['Mary', 95, True] ]
print(student_list[0][1])# way to acces nested lists
# how to loop through each element of each sub list 
# for entry in student_list:
#     for subentry in entry:
#         print(subentry)

# List comprehension you can do something to the new elements for a range satisfying a condtion
xRange = [x+1 for x in range(10)]
xRange = [x+1 for x in range(5)]
y = [3*x*x+5 for x in xRange]
matrix = [[x, x**2, x**3] for x in xRange]
# for row in matrix:
#     print(row)
# print(y)# to get y list in debug mode you must have code after it 
t = [x/1000 for x in range(10)]# timing mil liseconds
evenNr = [x for x in range(10) if x % 2]# all even numbers using if condition
names = ['mia','zara','Tom']
caps = [x.upper() for x in names]
numbers = [3, 0, 2, 10, 7]
low = [x for x in numbers if x <= 5]

'''
tuples now
'''
# nested tuple 
Nested_Tuple = ((4, 'Hello'), (7,'OK'))
Nested_Tuple[0][1] #will give 'Hello' same way to access as nested lists
'''
sets now
no indexing to call individual elements
union(|)
intersection (&)
difference(-)
symmetric difference(^) - all elements - intersection
'''
first_set = {1,2,3,4,4,5}
second_set = {1,2,2,7,8}
# print(first_set^second_set)
'''
dictionary now 
keys must be unique and immutable
.keys gets keys
.values gets values 
.items gets key value pair
'''
states = {'Oregon': 'OR', 
          'Florida': 'FL',
          'California': 'CA',
          'New York': 'NY'
          }
states["Michigan"] = "MI" # create new element in dictionary
del states['New York']
# print(states.keys(), states.values(), sorted(states.keys()), 'Florida' in states, states.items())
for key, val in states.items():
    print(key,val)