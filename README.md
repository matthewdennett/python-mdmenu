![pylint](https://img.shields.io/badge/PyLint-9.62-yellow?logo=python&logoColor=white)
[![Lint, Test, Build](https://github.com/matthewdennett/python-mdmenu/actions/workflows/list-test-build.yml/badge.svg)](https://github.com/matthewdennett/python-mdmenu/actions/workflows/list-test-build.yml)
[![Codecov](https://codecov.io/gh/matthewdennett/python-mdmenu/branch/main/graph/badge.svg)](https://codecov.io/gh/matthewdennett/python-mdmenu)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mdmenu)](https://pypi.org/project/mdmenu/)
[![PyPI Publish](https://github.com/matthewdennett/python-mdmenu/actions/workflows/pypi-publish.yml/badge.svg)](https://github.com/matthewdennett/python-mdmenu/actions/workflows/pypi-publish.yml)

# mdmenu

A simple and customisable text based menu system.


## Installation
Install mdmenu using pip:

```console
pip install mdmenu
```

## Usage

A new MDMenu object can be instantiated by calling its empty constructor for a default menu or it can be called with any combination of the instance [parameters](#parameters). Menu items can be added and removed with [```.add_menu_item()```](examples/add_option.py) and [```.remove_menu_item()```](examples/remove_option.py) respectively.

The appearance of the menu is customisable by setting any of the menu instance [parameters](#parameters)


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


## Examples
Several working examples have been included and are listed in the table below

| Link | Description |
| --- | --- |
| [https://github.com/matthewdennett/python-mdmenu/tree/main/examples/examples/default_menu.py](examples/default_menu.py)| Create an empty menu with the default formatting and implied exit menu option|
| [https://github.com/matthewdennett/python-mdmenu/tree/main/examples/examples/examples/defined_options.py](examples/defined_options.py)| Create a menu with a predefined set of menu options |
| [https://github.com/matthewdennett/python-mdmenu/tree/main/examples/examples/examples/add_option.py](examples/add_option.py)| Add a menu option with a defined index key and with out and index key |
| [https://github.com/matthewdennett/python-mdmenu/tree/main/examples/examples/remove_option.py](examples/remove_option.py)| Remove a menu option from the menu |
| [https://github.com/matthewdennett/python-mdmenu/tree/main/examples/examples/custom_formatting.py](examples/custom_formatting.py)| Create menu with custom formatting |
| [https://github.com/matthewdennett/python-mdmenu/tree/main/examples/examples/call_function.py](examples/call_function.py)| Call a function selected from the menu |

