# examples/defined_options.py
# pylint: disable=W0105,C0114,C0116
from mdmenu import MDMenu


def hello_world():
    print("Hello World!")


my_options = {
    1: ("Item 1", hello_world),
    2: ("Item 2", hello_world),
    10: ("Item x", hello_world)
}

my_menu = MDMenu(menu_items=my_options)
print(my_menu)

"""
################################################################################
                                      Menu
################################################################################
     1:   Item 1
     2:   Item 2
    10:   Item x
################################################################################
"""
