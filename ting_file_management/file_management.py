import sys


def txt_importer(path_file: str):
    try:
        if not path_file.endswith(".txt"):
            sys.stderr.write("Formato inválido\n")
        with open(path_file) as file:
            return file.read().splitlines()

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        return []
