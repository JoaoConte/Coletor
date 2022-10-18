from Modulos import *
from Funcoes import *
from Conecta_banco import *
from Prepara_dados import *
from Telas import *
from Consultores import *
from Pecas import *
from Servicos import *

telaval = Tk() # Estanciando a intergace grafica

class Application(Funcs, Conexao, Pre_Dados, Tela, Consultor, Peca, Servico): # Declarando uso das classes
# Inicialização em tempo de carga
    def __init__(self):
        self.telaval = telaval  # Estância tela inicial
        self.le_conexao()       # Efetua leitura do conexão.dat
        self.tela_inicial()     # Carrega tela inicial do sistema
        self.telaval.mainloop() # Engine do TKINTER
Application()


