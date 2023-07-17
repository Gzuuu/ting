import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    try:
        if not path_file.endswith('.txt'):
            sys.stderr.write('Formato inválido')
        with open(path_file, 'r') as arquivo:
            conteudo = arquivo.read()
        quebra_de_linha = conteudo.splitlines()
        return quebra_de_linha
    except FileNotFoundError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
