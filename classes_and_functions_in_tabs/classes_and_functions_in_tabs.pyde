#Created by Jeppe Veirum Larsen 30/5/2019

#Classes and Functions in tabs

"""
Tabs does not work like in regular Processing. Normally when creating a tab in Processing
it is automaticcally imported and ready to use. This is not the case in Processing.py where
we have to import it manually. It is easy to do and this example will show a couple of methods.
"""
#------------------------------------------
#--------- HOW TO CREATE A NEW TAB --------
#------------------------------------------

#To create a new file press the 'down arrow' beside the last tab. 

# From the square.py file we import everything (* means everything)
from square import *

s = Square()


def setup():
    size(300,300)
    
def draw():
    background(255)
    s.update()
