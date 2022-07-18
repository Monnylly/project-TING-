from ting_file_management.file_management import txt_importer
import sys
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return

    file = txt_importer(path_file)
    process = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    instance.enqueue(process)
    return sys.stdout.write(str(process))


def remove(instance: Queue) -> None:
    if not len(instance):
        return sys.stdout.write("Não há elementos\n")
    else:
        result_remove = instance
        ["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {result_remove} removido com sucesso\n")


def file_metadata(instance: Queue, position: int):
    try:
        result_file = instance.search(position)
        sys.stdout.write(str(result_file))
    except IndexError:
        return sys.stderr.write("Posição inválida\n")
