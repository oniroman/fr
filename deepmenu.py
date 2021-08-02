from textblocks import *


def select_from(some_list):
    prettier(some_list)
    i = input('Choose ? ')
    selection = some_list[int(i) - 1]
    print(selection)

