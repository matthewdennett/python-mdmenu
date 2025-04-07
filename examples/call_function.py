# examples/call_function.py
# pylint: disable=W0105, C0114, C0116
from mdmenu import MDMenu
from mdmenu import invalid


def hello_world(arg=None):
    print("Hello World!")
    print(f'arg: {arg}')


my_options = {
    1: ("Item 1", hello_world),
    2: ("Item 2", hello_world)
}

# Create and display a menu
my_menu = MDMenu(menu_items=my_options)
print(my_menu)

# Get user input
ans = input("Make A Choice: ")

# Get the selected option name and function. Return a the included "invalid" when option does not exist
function_name, function_called = my_menu.menu_items.get(int(ans), [None, invalid])
function_called("Arg passed in")

"""
################################################################################
                                      Menu
################################################################################
     1:   Item 1
     2:   Item 2
################################################################################

Make A Choice: 1
Hello World!
arg: Arg passed in
"""
