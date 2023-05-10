def exists_word(word, instance):
    results = []

    for archive in instance.data:
        ocurrences = []
        for i, lines in enumerate(archive["linhas_do_arquivo"]):
            if word.lower() in lines.lower():
                ocurrences.append({"linha": i + 1})
        if ocurrences:
            results.append({
                "palavra": word,
                "arquivo": archive["nome_do_arquivo"],
                "ocorrencias": ocurrences
            })

    return results


def search_by_word(word, instance):
    results = []

    for archive in instance.data:
        ocurrences = []
        for i, lines in enumerate(archive["linhas_do_arquivo"]):
            if word.lower() in lines.lower():
                ocurrences.append({"linha": i + 1,
                                   "conteudo": lines.strip()
                                   })
        if ocurrences:
            results.append({
                "palavra": word,
                "arquivo": archive["nome_do_arquivo"],
                "ocorrencias": ocurrences
            })

    return results
