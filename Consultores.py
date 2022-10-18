from Modulos import *

class Consultor():
    def limpa_consultor(self):
        pass


    def grade_consultor(self):
        pass



    def entry_consultor(self):
        self.lbl_titulo = Label(self.frame_dados, text = 'Cadastro de consultores', font=('verdana', 20, 'bold'))
        self.lbl_titulo.place(relx = 0.25, rely = 0.05)
        self.lbl_empresa = Label(self.frame_dados, text = 'Empresa',font=('verdana', 8, 'bold'))
        self.lbl_empresa.place(relx = 0.05, rely = 0.30)
        self.ent_empresa = Entry(self.frame_dados, width=2)
        self.ent_empresa.place(relx = 0.08, rely = 0.45)
        self.lbl_revenda = Label(self.frame_dados, text = 'Revenda',font=('verdana', 8, 'bold'))
        self.lbl_revenda.place(relx = 0.15, rely = 0.30)
        self.ent_revenda = Entry(self.frame_dados, width=2)
        self.ent_revenda.place(relx = 0.18, rely = 0.45)
        self.lbl_codigo = Label(self.frame_dados, text = 'Código consultor',font=('verdana', 8, 'bold'))
        self.lbl_codigo.place(relx = 0.35, rely = 0.30)
        self.ent_codigo = Entry(self.frame_dados, width=10)
        self.ent_codigo.place(relx = 0.35, rely = 0.45)
        self.lbl_nome = Label(self.frame_dados, text = 'Nome do consultor',font=('verdana', 8, 'bold'))
        self.lbl_nome.place(relx = 0.55, rely = 0.30)
        self.ent_nome = Entry(self.frame_dados, width=40)
        self.ent_nome.place(relx = 0.55, rely = 0.45)

        self.btn_grava_c = Button(self.frame_dados, text='GRAVA', bg = '#D3D3D3', font=('verdana', 8,'bold'), height = 1, width = 10)
        self.btn_grava_c.place(relx = 0.20, rely = 0.75)
        self.btn_altera_c = Button(self.frame_dados, text='ALTERA', bg = '#D3D3D3', font=('verdana', 8,'bold'), height = 1, width = 10)
        self.btn_altera_c.place(relx = 0.45, rely = 0.75)
        self.btn_exclui_c = Button(self.frame_dados, text='EXCLUI', bg = '#D3D3D3', font=('verdana', 8,'bold'), height = 1, width = 10)
        self.btn_exclui_c.place(relx = 0.7, rely = 0.75)