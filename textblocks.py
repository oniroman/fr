

def to_list(file_string):
    my_list = []
    with open(file_string, 'r', encoding='utf8') as f:
        my_list = [t.rstrip() for t in f]
        my_list = sorted(my_list)
    return my_list

questions = to_list(r'txt\interrogatifs.txt')
constructions = to_list(r'txt\constructions.txt')
places = to_list(r'txt\endroit.txt')
instructions = to_list(r'txt\instructions.txt')
ways = to_list(r'txt\manières.txt')
words = to_list(r'txt\mots.txt')
textparts = to_list(r'txt\parties_de_texte.txt')
sentenceparts = to_list(r'txt\parties_phrase.txt')
verbals = to_list(r'txt\verbaux.txt')
steps = to_list(r'txt\étapes.txt')

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
    print(lines)



