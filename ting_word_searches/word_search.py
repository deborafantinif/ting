def search_word(word, file_info, repeat, content):
    structure = {
        'palavra': word,
        'arquivo': file_info["nome_do_arquivo"],
        'ocorrencias': []
    }
    for index, item in enumerate(file_info["linhas_do_arquivo"]):
        if word.lower() in item.lower():
            if content:
                structure['ocorrencias'].append({
                    "linha": index + 1,
                    "conteudo": item
                })
            else:
                structure['ocorrencias'].append({"linha": index + 1})
    if structure['ocorrencias'] != []:
        repeat.append(structure)
    return repeat


def structure_word(word, instance, content):
    verify = True
    index = 0
    repeat = []
    try:
        while verify:
            file_info = instance.search(index)
            repeat = search_word(word, file_info, repeat, content)
            index += 1
    except IndexError:
        if index == 0:
            return []
        verify = False
        return repeat


def exists_word(word, instance):
    return structure_word(word, instance, False)


def search_by_word(word, instance):
    return structure_word(word, instance, True)
