

def txt_to_list(txt_file):
    list_from_text = []
    with open(txt_file, 'r', encoding='utf8') as text:
        for l in text:
            list_from_text.append(l.lower().rstrip())
    list_from_text = set(list_from_text)
    return sorted(list(list_from_text))


print(txt_to_list('instructions.txt'))
print(txt_to_list('endroit.txt'))
print(txt_to_list('manières.txt'))
print(txt_to_list('étapes.txt'))


def classifie(elements):
    réceptif = []
    productif = []
    for el in elements:
        choice = input(el + ' to (r)éceptif ou (p)roductif?')
        if choice == 'r':
            réceptif.append((el))
        elif choice == 'p':
            productif.append(el)
        else:
            pass
    return réceptif, productif

