# examples/custom_formatting.py
# pylint: disable=W0105, C0114, C0116
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
