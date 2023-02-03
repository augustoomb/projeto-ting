from .file_management import txt_importer
import sys


def check_path_file_in_queue(path_file, instance):
    for index in range(len(instance)):
        path_file_in_queue = (instance.search(index)['nome_do_arquivo'])
        if path_file_in_queue == path_file:
            return True


def process(path_file, instance):
    if check_path_file_in_queue(path_file, instance):
        return None

    list_content = txt_importer(path_file)

    dict_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(list_content),
        "linhas_do_arquivo": list_content
    }

    instance.enqueue(dict_file)

    print(dict_file, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


# O check_path_file_in_queue verifica se o path_file passado já está na fila.
# Minha queue possui um método que recebe um index e retorna o valor presente
# na posição da queue.
# Usando este método, eu trago o valor presente em cada posição da Queue
# e comparo com o que foi passado por parâmetro.
