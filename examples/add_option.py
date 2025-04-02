# examples/add_option.py
from mdmenu import MDMenu

def hello_world():
    print("Hello World!")

my_menu = MDMenu()

# Add option with a index key
# by default the last item is moved to the next highest index to remain at the end in the menu
# unless menu_hold_last is set to False.
my_menu.add_menu_item(item=("New Item 1", hello_world), key=4)

# Add option without index key
# The lowest available index is automatically assigned
my_menu.add_menu_item(item=("New Item 2", hello_world))
print(my_menu)

"""
################################################################################
                                      Menu                                      
################################################################################
     1:   New Item 2
     4:   New Item 1
     5:   Exit
################################################################################
"""