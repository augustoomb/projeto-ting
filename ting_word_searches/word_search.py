# from ting_file_management.queue import Queue
# from ting_file_management.file_process import process


def list_contains(list, word):
    list_content = []
    for index in range(len(list)):
        if word.lower() in list[index].lower():
            list_content.append(
                {"linha": index + 1}
            )

    return list_content


def exists_word(word, instance):
    occurrence_list = []
    for index in range(len(instance)):
        item_in_queue = instance.search(index)
        list_content = list_contains(item_in_queue['linhas_do_arquivo'], word)
        if len(list_content) > 0:
            occurrence_list.append({
                "palavra": word,
                "arquivo": item_in_queue['nome_do_arquivo'],
                "ocorrencias": list_content
            })

    return occurrence_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""

# if __name__ == "__main__":
#     queue1 = Queue()
#     process("statics/nome_pedro.txt", queue1)
#     print('Resposta abaixo:')
#     print(exists_word("pedro", queue1))
