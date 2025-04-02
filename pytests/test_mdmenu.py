import pytest

from mdmenu import MDMenu
from mdmenu import invalid

# pylint: disable=W0212:protected-access


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


def test_create_footer():
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
    Test the formatting of menu items is functional. Ensure wrapping of long items is occurring
    """
    assert False


def test_create_title():
    assert False


def test_create_border():
    assert False


def test_add_with_index():
    # Add a menu item with index
    assert False


def test_add_with_no_index():
    # Add menu item without index
    assert False


def test_add_with_index_no_hold_last():
    # Add a menu item with index
    assert False


def test_add_with_no_index_no_hold_last():
    # Add menu item without index
    assert False


def test_remove():
    # Remove menu item

    # with pytest.raises(IpDoesNotExistsError):
    #     net_a.delete_ip(IPv4Address("10.0.0.129"))

    assert False


def test_invalid():
    assert invalid() == "INVALID CHOICE!"
