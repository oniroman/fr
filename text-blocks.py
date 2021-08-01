mots_interrog = ["qui", "que", "qu'", "quoi", "quel", "quels", "quelle",
                 "quelles", "où", "est-ce-que", "pourquoi", "combien",
                 "combien de", "combien d'", "comment", "quand",
                 "à qui", "à quoi", "à quelle heure", "à combien de",
                 "avec qui", "avec quoi", "avec quel", "pour qui", "pour combien",
                 "de qui", "de quoi", "de quel"]
def txt_file_to_list(file_string):
    my_list = []
    with open(file_string, 'r', encoding='utf8') as f:
        my_list = [t.lower().rstrip() for t in f]
        my_list = sorted(my_list)
    return my_list

def prettier(list_of_things):
    lines = ""
    if len(list_of_things) > 20:
        for i, x in enumerate(list_of_things):
            if i < 9:
                temp = ' ' + str(i + 1) + '. ' + x
            else:
                temp = str(i + 1) + '. ' + x
            if len(temp) < 15:
                temp = temp + (15 - len(temp)) * ' '
            lines = lines + temp
            if (i + 1) % 10 == 0:
                lines = lines + '\n'
    else:
        for i, x in enumerate(list_of_things):
            lines = lines + '\n' + str(i) + ' ' + x
    return lines


print(prettier(txt_file_to_list('instructions.txt')))
print(prettier(txt_file_to_list('manières.txt')))
print(prettier(txt_file_to_list('étapes.txt')))
print(prettier(txt_file_to_list('endroit.txt')))
