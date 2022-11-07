import user_lib as ul
import sys
from user_lib import * # importing all can create conflicts because it imports gloabl variables as well
print_a_number()
ul.type_data(2)
# print(sys.path)# shows all paths where python will search for imports sys.path.append() can let you add a new path and sys.path.insert() takes 2 arguments position of location and location itself
#sys.path.remove() can remove a directory you no longer want in you import paths
sys.path.append('../')
print(sys.path[-1])
sys.path.remove('../')
print(sys.path[-1])
A = ul.number


