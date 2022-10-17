from Modulos import *

class Tela():
       
    def tela_inicial(self): # Tela parâmetros da validação
        self.telaval.title('Coletor - v1.0')
        self.telaval.geometry('700x600+300+20')
        self.telaval.resizable(False, False)
        self.telaval.focus_force()
        self.telaval.grab_set()
        self.abas()
        self.botoes_cadastros()
        self.tab_control.select(tab_id=1)
        self.frame_revenda() # Monta lista de revendas para serem selecionadas
        self.dataini()
        self.datafim()  
            