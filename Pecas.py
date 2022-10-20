from Modulos import *

class Peca():
    
    def var_pecas(self):
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
        self.codigo = self.codigo.upper()
        if self.codigo == '' or self.codigo == ' ':
            messagebox.showerror('Código','Campo Código não pode ser vazio')
            self.erro = 1
            self.ent_codigo.focus()
            return

    def limpa_pecas(self):
        self.ent_empresa.delete(0,END)
        self.ent_revenda.delete(0,END)
        self.ent_codigo.delete(0,END)
        self.ent_empresa.focus()

    def ClickDuplo_pecas(self, event):
        self.limpa_pecas()
        self.ckduplop = self.lista_pec.selection()
        for n in self.lista_pec.selection():
            empresa, revenda, codigo = self.lista_pec.item(n, 'values')
            self.ent_empresa.insert(END, empresa)
            self.ent_revenda.insert(END, revenda)
            self.ent_codigo.insert(END, codigo)

    def apaga_pecas(self):
        self.var_pecas()
        self.conecta_col()
        print(self.codigo)
        self.cursor_col.execute('''delete from pecas where cod_item=?''',(self.codigo))
        self.banco_col.commit()
        self.desconecta_col()
        messagebox.showinfo('Exclusão', 'Registro da peça excluido com sucesso')
        self.limpa_pecas()
        self.select_lista_pec()

    def altera_pecas(self):
        self.var_pecas()
        self.conecta_col()
        self.cursor_col.execute('''update pecas set EMPRESA=?, REVENDA=? where COD_ITEM= ?''',(self.empresa, self.revenda, self.codigo))
        self.banco_col.commit()
        self.desconecta_col()
        messagebox.showinfo('Alteração', 'Registro da peça alterado com sucesso')
        self.limpa_pecas()
        self.select_lista_pec()   

    def grava_pecas(self):
        self.var_pecas()
        if self.erro == 1:
            return
        self.conecta_col()
        self.cursor_col.execute("insert into pecas(empresa, revenda, cod_item) values (?, ?, ?)",(self.empresa, self.revenda, self.codigo))
        self.banco_col.commit()
        self.desconecta_col()
        messagebox.showinfo('Gravação', 'Registro de peças incluido com sucesso')
        self.limpa_pecas()
        self.select_lista_pec()

    def select_lista_pec(self):
        self.lista_pec.delete(*self.lista_pec.get_children())
        self.conecta_col()
        lista = self.cursor_col.execute('''SELECT empresa, revenda, cod_item FROM pecas''')
        for i in lista:
            self.lista_pec.insert("", END, values=i)
        self.desconecta_col()    
   
    def grade_pecas(self):
        self.lista_pec = ttk.Treeview(self.frame_grid, columns=('EMPRESA', 'REVENDA', 'COD_ITEM'), show='headings')
        self.lista_pec.heading('#1', text='Empresa')
        self.lista_pec.heading('#2', text='Revenda')
        self.lista_pec.heading('#3', text='Código da Peça')
        self.lista_pec.column('#1', width=1)
        self.lista_pec.column('#2', width=1)
        self.lista_pec.column('#3', width=300)
        self.lista_pec.place(relx = 0.16, rely = 0.05, relheight=0.90, relwidth=0.70)
        self.scr_lista_pec = Scrollbar(self.frame_grid, orient='vertical')
        self.lista_pec.configure(yscroll = self.scr_lista_pec)
        self.scr_lista_pec.place(relx = 0.86, rely = 0.05, relwidth = 0.03, relheight = 0.89)
        self.select_lista_pec()
        self.lista_pec.bind('<Double-1>', self.ClickDuplo_pecas)

    def entry_pecas(self):
        self.limpa_frame()
        self.lbl_titulo = Label(self.frame_dados, text = 'Cadastro de Peças', font=('verdana', 20, 'bold'))
        self.lbl_titulo.place(relx = 0.35, rely = 0.02)
        self.lbl_empresa = Label(self.frame_dados, text = 'Empresa',font=('verdana', 8, 'bold'))
        self.lbl_empresa.place(relx = 0.15, rely = 0.35)
        self.ent_empresa = Entry(self.frame_dados, width=2)
        self.ent_empresa.place(relx = 0.18, rely = 0.50)
        self.lbl_revenda = Label(self.frame_dados, text = 'Revenda',font=('verdana', 8, 'bold'))
        self.lbl_revenda.place(relx = 0.25, rely = 0.35)
        self.ent_revenda = Entry(self.frame_dados, width=2)
        self.ent_revenda.place(relx = 0.28, rely = 0.5)
        self.lbl_codigo = Label(self.frame_dados, text = 'Código da peça',font=('verdana', 8, 'bold'))
        self.lbl_codigo.place(relx = 0.45, rely = 0.35)
        self.ent_codigo = Entry(self.frame_dados, width=50)
        self.ent_codigo.place(relx = 0.45, rely = 0.5)
        self.btn_grava_c = Button(self.frame_dados, text='GRAVA', bg = '#D3D3D3', font=('verdana', 8,'bold'), height = 1, width = 10, command=self.grava_pecas)
        self.btn_grava_c.place(relx = 0.20, rely = 0.75)
        self.btn_altera_c = Button(self.frame_dados, text='ALTERA', bg = '#D3D3D3', font=('verdana', 8,'bold'), height = 1, width = 10, command=self.altera_pecas)
        self.btn_altera_c.place(relx = 0.45, rely = 0.75)
        self.btn_exclui_c = Button(self.frame_dados, text='EXCLUI', bg = '#D3D3D3', font=('verdana', 8,'bold'), height = 1, width = 10, command=self.apaga_pecas)
        self.btn_exclui_c.place(relx = 0.7, rely = 0.75)
        self.grade_pecas()