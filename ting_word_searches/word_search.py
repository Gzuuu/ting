def exists_word(word, instance):
    """Aqui irá sua implementação"""
    archives = []
    for index, file in enumerate(instance._data):
        archive_info = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for line, line_content in enumerate(
            file["linhas_do_arquivo"], start=1
        ):
            if word.lower() in line_content.lower():
                archive_info["ocorrencias"].append({"linha": line})
        if archive_info["ocorrencias"]:
            archives.append(archive_info)

    return archives


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    archives = []
    for index, file in enumerate(instance._data):
        archive_info = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for line, line_content in enumerate(
            file["linhas_do_arquivo"], start=1
        ):
            if word.lower() in line_content.lower():
                archive_info["ocorrencias"].append(
                    {
                        "linha": line,
                        "conteudo": line_content
                    })
        if archive_info["ocorrencias"]:
            archives.append(archive_info)

    return archives
