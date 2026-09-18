# Shopping List Manager

`list_warmup.py` — demonstrates creating a list, accessing items by index, using append and remove, and finding the list length with len.

`shopping_list.py` — provides an interactive shopping list manager for adding, removing, showing, and finishing a shopping list.

`list_report.py` — prints a numbered shopping list, counts item names longer than four characters, and finds the longest item using a loop.

Checking `in` before calling `.remove()` is safer because `.remove()` causes an error if the item does not exist in the list. Using `in` first allows the program to handle a missing item safely instead of crashing.
