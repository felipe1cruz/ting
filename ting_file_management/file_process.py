from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    lines = txt_importer(path_file)
    insert = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }
    if insert in instance.data:
        print(f"Arquivo {path_file} já foi processado anteriormente")
        return
    instance.enqueue(insert)
    print(insert, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
        return
    remove = instance.dequeue()
    print(f"Arquivo {remove['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
