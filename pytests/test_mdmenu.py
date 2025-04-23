# pylint: disable=W0212
# flake8: noqa:W291
"""
Testing for mdmenu
"""
import pytest
from mdmenu import MDMenu
from mdmenu import invalid


def test_main():
    """
    Test to validate test files is detected
    """
    assert True


def test_default_menu_item():
    """
    Test to validate a default menu item is create when a new menu is created
    """
    my_menu = MDMenu()
    assert my_menu.menu_items == {1: ("Exit", exit)}


def test_menu_item():
    """
    Test to validate a menu items can be passed in as a menu is created
    """
    test_item1 = ("test-1", exit)
    test_item5 = ("test-5", exit)
    my_menu = MDMenu(menu_items={1: test_item1, 5: test_item5})

    assert len(my_menu.menu_items) == 2
    assert my_menu.menu_items.get(1) == test_item1
    assert my_menu.menu_items.get(5) == test_item5


def test_str():
    """
    Test that the expected string representation is returned when in a default state
    """
    result = '''\
################################################################################
                                      Menu                                      
################################################################################
     1:   Exit
################################################################################
'''
    my_menu = MDMenu()
    assert str(my_menu) == result

    my_menu.title = False
    result = '''\
     1:   Exit
################################################################################
'''
    assert str(my_menu) == result

    my_menu.footer = False
    result = '''\
     1:   Exit
'''
    assert str(my_menu) == result


def test_create_footer():
    """
    Test that the expected footer string and content is created
    """
    result = '''################################################################################\n'''
    result_with_content = '''\
################################################################################
This is some test content
################################################################################
'''
    my_menu = MDMenu()

    assert my_menu._create_footer() == result
    my_menu.footer_content = "This is some test content"
    assert my_menu._create_footer() == result_with_content


def test_format_content():
    """
    Test that a long string is formatted to the configured width of the menu
    """
    result = '''\
This is a test string. This is a test string. This is a test string. This is a
test string. This is a test string. This is a test string. This is a test
string. This is a test string. This is a test string. This is a test string.
'''
    my_menu = MDMenu()
    assert my_menu._format_content("This is a test string. " * 10) == result


def test_format_menu_item():
    """
    Test the formatting of menu items is functional. Ensure wrapping of long items is occurring with
    correct indentation is being added for additional lines.
    """

    result = "This is a single line item."
    result_multiline = '''\
This is a multi line item.This is a multi line item.This is a multi
          line item.This is a multi line item.This is a multi line item.This is
          a multi line item.This is a multi line item.'''

    my_menu = MDMenu()
    assert my_menu._format_menu_item("This is a single line item.") == result
    assert my_menu._format_menu_item("This is a multi line item." * 7) == result_multiline


def test_create_title():
    """
    Test that a title is correctly constructed and can be customised to have a boarder or not
    """
    result = '''\
################################################################################
                                      Menu                                      
################################################################################
'''
    my_menu = MDMenu()
    assert my_menu._create_title() == result

    result = "                                      Menu                                      \n"
    my_menu.title_border = False
    assert my_menu._create_title() == result

    result = '''\
################################################################################
                                      Menu                                      
################################################################################
This is the preface string that is long enough to force wrappingThis is the
preface string that is long enough to force wrapping
################################################################################
'''
    my_menu.title_border = True
    my_menu.title_preface = "This is the preface string that is long enough to force wrapping" *2
    assert my_menu._create_title() == result

def test_create_border():
    """
    Test the creation of a boarder with default width and character is created
    """
    result = "################################################################################\n"
    my_menu = MDMenu()
    assert result == my_menu._create_border()


def test_add_with_index():
    """
    Test that a menu item can be added with a specified index and duplicate index raises a value
    error
    """
    # Add a menu item with index
    my_menu = MDMenu()
    test_item1 = ("test-1", exit)
    test_item5 = ("test-5", exit)
    test_item10 = ("test-10", exit)
    my_menu.add_menu_item(item=test_item1, key=1)
    my_menu.add_menu_item(item=test_item5, key=5)
    my_menu.add_menu_item(item=test_item10, key=10)

    assert len(my_menu.menu_items) == 4
    assert my_menu.menu_items.get(1) == test_item1
    assert my_menu.menu_items.get(5) == test_item5
    assert my_menu.menu_items.get(10) == test_item10
    assert my_menu.menu_items.get(11) == ("Exit", exit)

    with pytest.raises(ValueError):
        my_menu.add_menu_item(item=("duplicate", exit), key=5)


def test_add_with_no_index():
    """
    Test that entries can be added when a index is not specified and the lowest free index is
    allocated
    """
    my_menu = MDMenu()
    no_key1 = ("NoKey-1", exit)
    no_key2 = ("NoKey-2", exit)
    my_menu.add_menu_item(item=("test-1", exit), key=1)
    my_menu.add_menu_item(item=("test-3", exit), key=3)

    # First available index is 2
    my_menu.add_menu_item(item=no_key1)

    # No gap in index number, allocate the last
    my_menu.add_menu_item(item=no_key2)

    assert len(my_menu.menu_items) == 5
    assert my_menu.menu_items.get(2) == no_key1
    assert my_menu.menu_items.get(4) == no_key2


def test_add_with_index_no_hold_last():
    """
    Test that a menu item can be added with a specified index when the no_hold_last function is
    disabled
    """
    my_menu = MDMenu()
    my_menu.menu_hold_last = False
    test_item5 = ("test-5", exit)

    # The menu is initialised with a default item at index 1
    with pytest.raises(ValueError):
        my_menu.add_menu_item(item=("duplicate", exit), key=1)

    my_menu.add_menu_item(item=test_item5, key=5)

    assert len(my_menu.menu_items) == 2
    assert my_menu.menu_items.get(1) == ("Exit", exit)
    assert my_menu.menu_items.get(5) == test_item5


def test_add_with_no_index_no_hold_last():
    """
    Test that a menu item can be added with no index when the no_hold_last function is disabled
    """
    my_menu = MDMenu()
    my_menu.menu_hold_last = False
    test_item5 = ("test-5", exit)

    my_menu.add_menu_item(item=test_item5)

    assert len(my_menu.menu_items) == 2
    assert my_menu.menu_items.get(1) == ("Exit", exit)
    assert my_menu.menu_items.get(2) == test_item5


def test_remove():
    """
    Test that an item can be removed from the menu
    """

    my_menu = MDMenu()
    test_item1 = ("test-1", exit)
    test_item5 = ("test-5", exit)
    my_menu.add_menu_item(item=test_item1, key=1)
    my_menu.add_menu_item(item=test_item5, key=5)

    assert len(my_menu.menu_items) == 3

    # remove a key that never existed
    with pytest.raises(KeyError):
        my_menu.remove_menu_item(10)

    assert len(my_menu.menu_items) == 3
    assert my_menu.remove_menu_item(1) == test_item1
    assert len(my_menu.menu_items) == 2

    # remove a key that has just been removed
    with pytest.raises(KeyError):
        my_menu.remove_menu_item(1)

    assert len(my_menu.menu_items) == 2


def test_invalid():
    """
    Test the default function for invalid entries works
    """
    assert invalid() is None
