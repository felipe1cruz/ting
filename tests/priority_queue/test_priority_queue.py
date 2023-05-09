from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    pq = PriorityQueue
    pq.enqueue({"nome": "arquivo_prioritario1.txt", "qtd_linhas": 2})
    pq.enqueue({"nome": "arquivo_nao_prioritario.txt", "qtd_linhas": 10})
    pq.enqueue({"nome": "arquivo_prioritario2.txt", "qtd_linhas": 1})
    
    qty_data_inserted = 3
    assert len(pq) == qty_data_inserted
    assert pq.search(0)["nome"] == "arquivo_prioritario1.txt"
    assert pq.search(1)["nome"] == "arquivo_prioritario2.txt"
    assert pq.search(2)["nome"] == "arquivo_nao_prioritario.txt"

    assert pq.dequeue()["nome"] == "arquivo_prioritario1.txt"
    assert pq.dequeue()["nome"] == "arquivo_prioritario2.txt"
    assert pq.dequeue()["nome"] == "arquivo_nao_prioritario.txt"

    number_out_of_len = 10
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        pq.search(number_out_of_len)
