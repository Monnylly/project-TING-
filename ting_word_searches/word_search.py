def exists_word(word, instance):
    result = []
    data_res = []

    for item in range(len(instance)):
        search = instance.search(item)
        file = search['nome_do_arquivo']
        file_line = search['linhas_do_arquivo']

        for line in file_line:
            if word.lower() in line.lower():
                result.append({"linha": file_line.index(line) + 1})

    if len(result) > 0:
        data_res.append({
            'palavra': word,
            'arquivo': file,
            'ocorrencias': result,
            })

    return data_res


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
