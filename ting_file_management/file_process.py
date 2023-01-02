import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    list_text = txt_importer(path_file)
    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(list_text),
        "linhas_do_arquivo": list_text
    }
    repeat = [1 for x in instance.queue if x["nome_do_arquivo"] == path_file]
    if len(repeat) > 0:
        return None
    instance.enqueue(new_dict)
    sys.stdout.write(str(new_dict))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
