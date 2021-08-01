

def txt_to_list(txt_file):
    list_from_text = []
    with open(txt_file, 'r', encoding='utf8') as text:
        for l in text:
            list_from_text.append(l.lower().rstrip())
    list_from_text = set(list_from_text)
    return sorted(list(list_from_text))
