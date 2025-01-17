import unittest
from datetime import datetime, timedelta
from tarefa import Tarefa

class TestConcluir(unittest.TestCase):
    
    def test_concluir_tarefa_altera_concluida_para_true(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)
    
    def test_concluir_tarefa_concluida_mantem_concluida_como_true(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)    
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)

class TestAdicionarDescricao(unittest.TestCase):
    
    def test_adicionar_descricao_altera_descricao(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.adicionar_descricao("Estudar fundamentos de Python")
        self.assertEqual(tarefa.descricao, "Estudar fundamentos de Python")
    
    def test_adicionar_descricao_vazia(self):
        tarefa = Tarefa("Estudar Python", "Estudar fundamentos de Python")
        tarefa.adicionar_descricao("")
        self.assertEqual(tarefa.descricao, "")

class TestAdiarNotificacao(unittest.TestCase):
    
    def test_adiar_notificacao(self):
        tarefa = Tarefa("Estudar Python", notificacao=datetime.now())
        original_time = tarefa.notificacao
        tarefa.adiar_notificacao(30)
        self.assertEqual(tarefa.notificacao, original_time + timedelta(minutes=30))
    
    def test_adiar_notificacao_com_notificacao_nula(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.adiar_notificacao(30)
        self.assertTrue(tarefa.notificacao > datetime.now())

class TestAtrasada(unittest.TestCase):
    
    def test_tarefa_atrasada(self):
        tarefa = Tarefa("Estudar Python", data=datetime.now() - timedelta(days=1))
        self.assertTrue(tarefa.atrasada())
    
    def test_tarefa_nao_atrasada(self):
        tarefa = Tarefa("Estudar Python", data=datetime.now() + timedelta(days=1))
        self.assertFalse(tarefa.atrasada())

if __name__ == '__main__':
    unittest.main()
