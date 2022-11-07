#mutable means you change values of the elements and add or remove elements in place(lists are mutablbe where as tuples and strings are not)
Days = ['Mon', 'Tue', 'Wed']
Days.append('Thu')#append the new element to the end of the list
Days.insert(4, 'Fri')#insert an element at specific index
Days.remove('Tue')# removes first instance of Tue
del Days[1]# removes element at index 1
thursday = Days.pop(3)# removes the element and returns the elements value 
# print(Days)
Days.inedx('Wed')# find index of wednesday 
Days.count('Wed')# count the time the element appears in the list 
Days[0] = 'Tuesday'# assign new value for element 
 
'''
when looping through multiple iterable objects(lists)
'''
fruit = ['lemons', 'apples', 'pears']
colour = ['yellow', 'red', 'green']

for f,c in zip(fruit,colour):# zip joins to lists in a way that both elements can be called at the same time
    print(f, 'are', c)