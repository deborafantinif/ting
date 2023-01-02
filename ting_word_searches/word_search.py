def search_word(word, file_info, repeat):
    structure = {
        'palavra': word,
        'arquivo': file_info["nome_do_arquivo"],
        'ocorrencias': []
    }
    for index, item in enumerate(file_info["linhas_do_arquivo"]):
        if word.lower() in item.lower():
            structure['ocorrencias'].append({"linha": index + 1})
    if structure['ocorrencias'] != []:
        repeat.append(structure)
    return repeat


def exists_word(word, instance):
    verify = True
    index = 0
    repeat = []
    try:
        while verify:
            file_info = instance.search(index)
            repeat = search_word(word, file_info, repeat)
            index += 1
    except IndexError:
        if index == 0:
            return []
        verify = False
        return repeat


def search_by_word(word, instance):
    return []
