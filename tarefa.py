from datetime import datetime, timedelta
from datetime import date

class Tarefa:
    def __init__(self, titulo, descricao="", data=date.today(), notificacao=None, concluida=False):
        self.titulo = titulo
        self.descricao = descricao
        self.data = data if data else datetime.now()
        self.notificacao = notificacao
        self.concluida = concluida

    def concluir(self):
        """Define essa tarefa como concluída"""
        self.concluida = True

    def adicionar_descricao(self, descricao):
        """Adiciona ou altera a descrição para a tarefa"""
        self.descricao = descricao

    def adiar_notificacao(self, minutos):
        """Adia a notificação por um número de minutos"""
        if self.notificacao:
            self.notificacao += timedelta(minutes=minutos)
        else:
            self.notificacao = datetime.now() + timedelta(minutes=minutos)

    def atrasada(self):
        """Verifica se a tarefa está atrasada (data < hoje)"""
        return self.data < datetime.now()
