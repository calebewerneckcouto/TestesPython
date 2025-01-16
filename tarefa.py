#Test Driven Development:escrever os teste antes da nossa logica
class Tarefa:
    def __init__(self,titulo,descricao="",data=None,notificacao=None,concluida=False):
        self.titulo = titulo
        self.descricao =descricao
        self.data = data
        self.notificacao = notificacao
        self.concluida=concluida
        
        
    
    def concluir(self):
        """
        Define essa tarefa como concluida
        """    
        self.concluida=True
        
    
    def adicionar_descricao(self):
        """
        Adiciona uma descricao para a Tarefa
        """    
        pass
    
    
    def adiar_notificacao(self):
        """
        Adia a notificacao em um certa quantidade de minutos
        """    
        pass
    
    def atrasada(self):
        """
        Diz se a tarefa esta atrasada.Ou seja, data<hoje
        """    
        pass