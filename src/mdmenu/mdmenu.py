
# TODO - Add menu item
# TODO - Remove menu item
# TODO - Footer
# TODO - Title
# TODO - Tests
# TODO - LINT

class Menu(object):
    menu_items = {}
    menu_name = "Menu"
    title = True
    title_border = True
    title_padding = " "
    footer = True
    menu_character = "#"
    menu_width = 80

    # def __init__(self, menu_items: dict[int, tuple] | None = {100,("Exit", exit_menu)}) -> None:
    def __init__(self, menu_items: dict[int, tuple] | None = None) -> None:
        if menu_items is None:
            self.menu_items = {1: ("Exit", exit)}
        else:
            self.menu_items = menu_items

    def __str__(self) -> str:
        output: str = ""

        if self.title:
            output += self.get_title()

        for key in sorted(self.menu_items.keys()):
            # TODO - Add Left and right padding to key
            # TODO - Add Left padding to item
            output += f"{key} : {self.menu_items[key][0]}\n"

        if self.footer:
            output += self.get_border()

        return output

    def get_title(self) -> str:
        output: str = ""
        if self.title_border:
            output += self.get_border()

        output += f"{self.menu_name:{self.title_padding}^{self.menu_width}}\n"

        if self.title_border:
            output += self.get_border()

        return output

    def get_border(self) -> str:
        return f"{self.menu_width * self.menu_character}\n"

    def add_menu_item(self, item: tuple, key: int = None,) -> None:
        # Get the exit menu item
        max_key = max(list(self.menu_items.keys()))
        last = self.menu_items.pop(max_key)

        if key is None:
            key = next((i for i in range(1,max(list(self.menu_items.keys()))) if i not in self.menu_items.keys()), max_key)


        if self.menu_items.get(key) is not None:
            raise ValueError

        self.menu_items[key] = item
        max_key = max(list(self.menu_items.keys()))
        self.menu_items[max_key + 1] = last


if __name__ == "__main__":
    print("Running")

    def hello():
        print("hello")

    my_menu = Menu()
    print(my_menu)
    my_menu.add_menu_item(("Hello", hello), 3)
    print("added")
    print(my_menu)
    my_menu.add_menu_item(("Hello 2nd", hello))
    print(my_menu)
    my_menu.add_menu_item(("Hello 3nd", hello))
    print(my_menu)
    my_menu.add_menu_item(("Hello 4nd", hello))
    print(my_menu)
    my_menu.add_menu_item(("Hello 5nd", hello))
    print(my_menu)
    my_menu.add_menu_item(("Hello", hello), 3)