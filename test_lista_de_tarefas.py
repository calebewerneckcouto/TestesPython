import unittest
from datetime import date, timedelta
from tarefa import Tarefa
from lista_de_tarefas import ListaDeTarefas

class TestAdicionarTarefa(unittest.TestCase):
    def test_adiciona_tarefa_a_lista_de_tarefa(self):
        tarefa = Tarefa("Tarefa teste")
        lista = ListaDeTarefas()
        lista.adicionar_tarefa(tarefa)
        self.assertEqual(lista.get_tarefas()[0], tarefa)

class TestGetTarefas(unittest.TestCase):
    def test_retorna_lista_de_tarefas_adicionadas(self):
        tarefa_um = Tarefa("Tarefa teste 1")
        tarefa_dois = Tarefa("Tarefa teste 2")
        lista = ListaDeTarefas()
        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)
        
        self.assertEqual(lista.get_tarefas(), [tarefa_um, tarefa_dois])

class TestGetTarefasAtrasadas(unittest.TestCase):
    def test_retorna_apenas_tarefas_atrasadas(self):
        hoje = date.today()
        tarefa_atrasada = Tarefa("Tarefa atrasada", data=hoje - timedelta(days=1))
        tarefa_hoje = Tarefa("Tarefa de hoje", data=hoje)
        lista = ListaDeTarefas()
        lista.adicionar_tarefa(tarefa_atrasada)
        lista.adicionar_tarefa(tarefa_hoje)

        tarefas_atrasadas = lista.get_tarefas_atrasadas()
        self.assertEqual(tarefas_atrasadas, [tarefa_atrasada])

class TestGetTarefasParaHoje(unittest.TestCase):
    def test_retorna_apenas_tarefas_para_hoje(self):
        hoje = date.today()
        tarefa_hoje = Tarefa("Tarefa de hoje", data=hoje)
        tarefa_futura = Tarefa("Tarefa futura", data=hoje + timedelta(days=1))
        lista = ListaDeTarefas()
        lista.adicionar_tarefa(tarefa_hoje)
        lista.adicionar_tarefa(tarefa_futura)

        tarefas_para_hoje = lista.get_tarefas_para_hoje()
        self.assertEqual(tarefas_para_hoje, [tarefa_hoje])

if __name__ == "__main__":
    unittest.main()
