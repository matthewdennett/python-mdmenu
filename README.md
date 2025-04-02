# mdmenu


[![Lint](https://github.com/matthewdennett/python-mdmenu/actions/workflows/lint.yml/badge.svg)](https://github.com/matthewdennett/python-mdmenu/actions/workflows/lint.yml)

![pylint](https://img.shields.io/badge/PyLint-8.16-yellow?logo=python&logoColor=white)


[![Build](https://github.com/matthewdennett/python-mdmenu/actions/workflows/build.yml/badge.svg)](https://github.com/matthewdennett/python-mdmenu/actions/workflows/build.yml)


[![codecov](https://codecov.io/gh/matthewdennett/python-mdmenu/branch/main/graph/badge.svg)](https://codecov.io/gh/matthewdennett/python-mdmenu)

[![PyPI version](https://badge.fury.io/py/python-mdmenu.svg)](https://badge.fury.io/py/python-mdmenu)


A simple and customisable text based menu system.


## Installation
Install mdmenu using pip:

```console
pip install mdmenu
```

## Usage

Create a default menu object
```python
# examples/default_menu.py
from mdmenu import MDMenu

my_menu = MDMenu()
print(my_menu)

"""
################################################################################
                                      Menu                                      
################################################################################
     1:   Exit
################################################################################
"""
```

Create a menu with a predefined set of menu options
```python
# examples/defined_options.py
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
```

Create a menu with customised size and formatting
```python
# examples/custom_formatting.py
from mdmenu import MDMenu

my_menu = MDMenu(
    footer_content="This is the footer_content",
    key_trailing_gap=1,
    key_width=3,
    menu_character="=",
    menu_name="My Custom Menu",
    menu_width=40,
    title_padding="-",
    title_preface="This is the title_preface",
                 )
print(my_menu)

"""
========================================
-------------My Custom Menu-------------
========================================
This is the title_preface
========================================
 1: Exit
========================================
This is the footer_content
========================================
"""
```

Add a new menu option
```python
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
```

Remove a menu option from a menu
```python
# examples/remove_options.py
from mdmenu import MDMenu

def hello_world():
    print("Hello World!")

my_options = {
    1: ("Item 1", hello_world),
    2: ("Item 2", hello_world),
    10: ("Item x", hello_world)
}

my_menu = MDMenu(menu_items=my_options)
my_menu.remove_menu_item(key=2)
print(my_menu)

"""
################################################################################
                                      Menu                                      
################################################################################
     1:   Item 1
    10:   Item x
################################################################################
"""
```

Call menu option function
```python


```


## Parameters

The following table list the parameters of the Menu which can be altered to customise the look and
formatting of the table. 

| Parameter | Description |
| :--- | :--- |
| **footer_content** <br>Type: str <br>Default: None | A text body to be displayed in the footer of the menu, after the main body of the menu. |
| **footer** <br>Type: bool <br>Default: True        | Enabled by default, this boolean attribute indicates if the menu will be displayed with footer. | 
| **key_trailing_gap**<br>Type:int <br>Default: 3    | The number of white space to be added after the menu item key and before the items name when displaying the menu. <br>eg.     5:<key_trailing_gap>Hello World |
| **key_width** <br>Type: int <br>Default: 7         | The number of characters to pad the menu item key to when displayed.<br>eg.<key_width>:     Hello World |
| **menu_character** <br>Type: str <br>Default: '#'  | The character used to create borders of 'self.menu_width' for the menu |
| **menu_hold_last** <br>Type: bool <br>Default: True | When true, the last item in the 'self.menu_items" dict is maintained as the item with the highest/last key value. As the default and most likely first item added is the exit, this provides a easy mechanism to keep it as the last last menu item even when key values are automatically assigned. |
| **menu_items** <br>Type: dict[int, tuple] <br>Default: {1: ("Exit", exit)} | The dict of menu items in the system. Each item has a int key and a tuple with the items title and associated function. |
| **menu_name** <br>Type: str <br>Default: True      | The name of the menu as a string. The name is displayed when the attribute 'title' is true. |
| **menu_width** <br>Type: int <br>Default: 80       | The width of the menu system |
| **title_border** <br>Type: bool <br>Default: True  | Enabled by default, this boolean attribute indicates if the menus title should be surrounded by a border of 'self.menu_character'. |
| **title_padding** <br>Type: str <br>Default: " "   | The character to use to pad the left and right of 'self.menu_name' when displayed in the menu title.  |
| **title_preface** <br>Type: str <br>Default: None  | A text body to be displayed between the menu title and the main body of the menu. |
| **title** <br>Type: bool <br>Default: True         | Enabled by default, this boolean attribute indicates if the menus title should be displayed.  |

