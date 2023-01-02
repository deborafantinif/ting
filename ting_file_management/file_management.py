from os import path
import sys


def txt_importer(path_file):
    if not path.exists(path_file):
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
        return None
    if not path_file.endswith('.txt'):
        sys.stderr.write('Formato inválido\n')
    with open(path_file, 'r') as text:
        return [line.rstrip() for line in text]
