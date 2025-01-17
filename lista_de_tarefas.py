from datetime import date

class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []
    
    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
    
    def get_tarefas(self, incluir_concluidas=False):
        if incluir_concluidas:
            return self.tarefas
        return [tarefa for tarefa in self.tarefas if not tarefa.concluida]
    
    def get_tarefas_atrasadas(self):
        hoje = date.today()
        return [tarefa for tarefa in self.tarefas if tarefa.data < hoje and not tarefa.concluida]
    
    def get_tarefas_para_hoje(self):
        hoje = date.today()
        return [tarefa for tarefa in self.tarefas if tarefa.data == hoje]
