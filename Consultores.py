from Modulos import *

class Consultor():

    def var_consultor(self):
        self.erro = 0
        self.empresa = self.ent_empresa.get()
        if self.empresa == '' or self.empresa == ' ':
            messagebox.showerror('Empresa','Campo empresa não pode ser vazio')
            self.erro = 1
            self.ent_empresa.focus()
            return
        self.revenda = self.ent_revenda.get()
        if self.revenda == '' or self.revenda == ' ':
            messagebox.showerror('Revenda','Campo Revenda não pode ser vazio')
            self.erro = 1
            self.ent_revenda.focus()
            return
        self.codigo = self.ent_codigo.get()
        if self.codigo == '' or self.codigo == ' ':
            messagebox.showerror('Código','Campo Código não pode ser vazio')
            self.erro = 1
            self.ent_codigo.focus()
            return
        self.nome = self.ent_nome.get()
        self.nome = self.nome.upper()
        if self.nome == '' or self.nome == ' ':
            messagebox.showerror('Nome','Campo Nome não pode ser vazio')
            self.erro = 1
            self.ent_nome.focus()
            return        

    def limpa_consultor(self):
        self.ent_empresa.delete(0,END)
        self.ent_revenda.delete(0,END)
        self.ent_codigo.delete(0,END)
        self.ent_nome.delete(0,END)
        self.ent_empresa.focus()

    def ClickDuplo(self, event):
        self.limpa_consultor()
        self.ckduplo = self.lista_con.selection()
        for n in self.lista_con.selection():
            empresa, revenda, codigo, nome = self.lista_con.item(n, 'values')
            self.ent_empresa.insert(END, empresa)
            self.ent_revenda.insert(END, revenda)
            self.ent_codigo.insert(END, codigo)
            self.ent_nome.insert(END, nome)    

    def apaga_consultor(self):
        self.var_consultor()
        self.conecta_col()
        self.cursor_col.execute("delete from consultores where cod_usuario="+self.codigo)
        self.banco_col.commit()
        self.desconecta_col()
        messagebox.showinfo('Exclusão', 'Registro Excluido com sucesso')
        self.limpa_consultor()
        self.select_lista_con()

    def altera_consultor(self):
        self.var_consultor()
        self.conecta_col()
        self.cursor_col.execute('''update consultores set EMPRESA=?, REVENDA=?, NOME_USUARIO=? where COD_USUARIO= ?''',(self.empresa, self.revenda, self.nome, self.codigo))
        self.banco_col.commit()
        self.desconecta_col()
        messagebox.showinfo('Alteração', 'Registro Alterado com sucesso')
        self.limpa_consultor()
        self.select_lista_con()   

    def grava_consultor(self):
        self.var_consultor()
        if self.erro == 1:
            return
        self.conecta_col()
        self.cursor_col.execute("insert into consultores(empresa, revenda, cod_usuario, nome_usuario) values (?, ?, ?, ?)",(self.empresa, self.revenda, self.codigo, self.nome))
        self.banco_col.commit()
        self.desconecta_col()
        messagebox.showinfo('Gravação', 'Registro incluido com sucesso')
        self.limpa_consultor()
        self.select_lista_con()

    def select_lista_con(self):
        self.lista_con.delete(*self.lista_con.get_children())
        self.conecta_col()
        lista = self.cursor_col.execute('''SELECT empresa, revenda, cod_usuario, nome_usuario FROM consultores''')
        for i in lista:
            self.lista_con.insert("", END, values=i)
        self.desconecta_col()    
   
    def grade_consultor(self):
        self.lista_con = ttk.Treeview(self.frame_grid, columns=('EMPRESA', 'REVENDA', 'COD_USUARIO', 'NOME_USUARIO'), show='headings')
        self.lista_con.heading('#1', text='Empresa')
        self.lista_con.heading('#2', text='Revenda')
        self.lista_con.heading('#3', text='Código')
        self.lista_con.heading('#4', text='Nome')
        self.lista_con.column('#1', minwidth = 0, width=60)
        self.lista_con.column('#2', minwidth = 0, width=60)
        self.lista_con.column('#3', minwidth = 0, width=50)
        self.lista_con.column('#4', minwidth = 0, width=480)
        self.lista_con.place(relx = 0.01, rely = 0.05, relheight=0.90, relwidth=0.95)
        self.scr_lista_con = Scrollbar(self.frame_grid, orient='vertical')
        self.lista_con.configure(yscroll = self.scr_lista_con)
        self.scr_lista_con.place(relx = 0.96, rely = 0.05, relwidth = 0.03, relheight = 0.89)
        self.select_lista_con()
        self.lista_con.bind('<Double-1>', self.ClickDuplo)

    def entry_consultor(self):
        self.limpa_frame()
        self.lbl_titulo = Label(self.frame_dados, text = 'Cadastro de consultores', font=('verdana', 20, 'bold'))
        self.lbl_titulo.place(relx = 0.25, rely = 0.02)
        self.lbl_empresa = Label(self.frame_dados, text = 'Empresa',font=('verdana', 8, 'bold'))
        self.lbl_empresa.place(relx = 0.05, rely = 0.35)
        self.ent_empresa = Entry(self.frame_dados, width=2)
        self.ent_empresa.place(relx = 0.08, rely = 0.50)
        self.lbl_revenda = Label(self.frame_dados, text = 'Revenda',font=('verdana', 8, 'bold'))
        self.lbl_revenda.place(relx = 0.15, rely = 0.35)
        self.ent_revenda = Entry(self.frame_dados, width=2)
        self.ent_revenda.place(relx = 0.18, rely = 0.5)
        self.lbl_codigo = Label(self.frame_dados, text = 'Código consultor',font=('verdana', 8, 'bold'))
        self.lbl_codigo.place(relx = 0.35, rely = 0.35)
        self.ent_codigo = Entry(self.frame_dados, width=10)
        self.ent_codigo.place(relx = 0.35, rely = 0.5)
        self.lbl_nome = Label(self.frame_dados, text = 'Nome do consultor',font=('verdana', 8, 'bold'))
        self.lbl_nome.place(relx = 0.55, rely = 0.35)
        self.ent_nome = Entry(self.frame_dados, width=40)
        self.ent_nome.place(relx = 0.55, rely = 0.5)
        self.btn_grava_c = Button(self.frame_dados, text='GRAVA', bg = '#D3D3D3', font=('verdana', 8,'bold'), height = 1, width = 10, command=self.grava_consultor)
        self.btn_grava_c.place(relx = 0.20, rely = 0.75)
        self.btn_altera_c = Button(self.frame_dados, text='ALTERA', bg = '#D3D3D3', font=('verdana', 8,'bold'), height = 1, width = 10, command=self.altera_consultor)
        self.btn_altera_c.place(relx = 0.45, rely = 0.75)
        self.btn_exclui_c = Button(self.frame_dados, text='EXCLUI', bg = '#D3D3D3', font=('verdana', 8,'bold'), height = 1, width = 10, command=self.apaga_consultor)
        self.btn_exclui_c.place(relx = 0.7, rely = 0.75)
        self.grade_consultor()


        