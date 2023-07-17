import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    conteudo = txt_importer(path_file)
    conteudo_para_fila = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(conteudo),
        "linhas_do_arquivo": conteudo,
    }
    instance.enqueue(conteudo_para_fila)
    sys.stdout.write(f"{conteudo_para_fila}\n")
    return conteudo_para_fila


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
        return None

    removed = instance.dequeue()
    sys.stdout.write(
        f"Arquivo {removed['nome_do_arquivo']} removido com sucesso\n")
    return removed


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        conteudo = instance.search(position)
        sys.stdout.write(f"{conteudo}\n")
        return conteudo
    except IndexError:
        sys.stderr.write('Posição inválida')
