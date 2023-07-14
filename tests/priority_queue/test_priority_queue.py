import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing(capsys):
    """Aqui irá sua implementação"""
    arquivo_qualquer = {
        "nome_do_arquivo": "",
        "qtd_linhas": 20,
        "linhas_do_arquivo": [],
    }

    arquivo_com_prioridade = {
        "nome_do_arquivo": "",
        "qtd_linhas": 2,
        "linhas_do_arquivo": [],
    }
    priorityQueue = PriorityQueue()

    priorityQueue.enqueue(arquivo_qualquer)
    priorityQueue.enqueue(arquivo_com_prioridade)

    assert priorityQueue.is_priority(arquivo_com_prioridade) is True
    assert len(priorityQueue.high_priority) == 1
    assert len(priorityQueue.regular_priority) == 1
    assert priorityQueue.search(0) == arquivo_com_prioridade
    assert priorityQueue.dequeue() == arquivo_com_prioridade

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priorityQueue.search(5)
