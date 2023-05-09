from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    pq = PriorityQueue()
    pq.enqueue({"nome_do_arquivo": "arquivo_prioritario1.txt",
                "qtd_linhas": 2,
                "linhas_do_arquivo": [1, 2]})
    pq.enqueue({"nome_do_arquivo": "arquivo_nao_prioritario.txt",
                "qtd_linhas": 10,
                "linhas_do_arquivo": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    pq.enqueue({"nome_do_arquivo": "arquivo_prioritario2.txt",
                "qtd_linhas": 1,
                "linhas_do_arquivo": [1]})

    qty_data_inserted = 3
    assert len(pq) == qty_data_inserted
    assert pq.search(0)["nome_do_arquivo"] == "arquivo_prioritario1.txt"
    assert pq.search(1)["nome_do_arquivo"] == "arquivo_prioritario2.txt"
    assert pq.search(2)["nome_do_arquivo"] == "arquivo_nao_prioritario.txt"

    dequeue = pq.dequeue()
    assert dequeue is not None and dequeue["nome_do_arquivo"] == "arquivo_prioritario1.txt"

    number_out_of_len = 10
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        pq.search(number_out_of_len)
    # teste
