from Modulos import *

class Servico():
    def var_servicos(self):
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
            messagebox.showerror('Código','Campo Código Serviço não pode ser vazio')
            self.erro = 1
            self.ent_codigo.focus()
            return

    def limpa_servicos(self):
        self.ent_empresa.delete(0,END)
        self.ent_revenda.delete(0,END)
        self.ent_codigo.delete(0,END)
        self.ent_empresa.focus()

    def ClickDuplo_servicos(self, event):
        self.limpa_servicos()
        self.ckduplos = self.lista_ser.selection()
        for n in self.lista_ser.selection():
            empresa, revenda, codigo = self.lista_ser.item(n, 'values')
            self.ent_empresa.insert(END, empresa)
            self.ent_revenda.insert(END, revenda)
            self.ent_codigo.insert(END, codigo)

    def apaga_servicos(self):
        self.var_servicos()
        self.conecta_col()
        self.cursor_col.execute('''delete from servicos where cod_servico=?''',(self.codigo))
        self.banco_col.commit()
        self.desconecta_col()
        messagebox.showinfo('Exclusão', 'Registro do serviço excluido com sucesso')
        self.limpa_servicos()
        self.select_lista_ser()

    def altera_servicos(self):
        self.var_servicos()
        self.conecta_col()
        self.cursor_col.execute('''update servicos set EMPRESA=?, REVENDA=? where COD_SERVICO= ?''',(self.empresa, self.revenda, self.codigo))
        self.banco_col.commit()
        self.desconecta_col()
        messagebox.showinfo('Alteração', 'Registro do serviço alterado com sucesso')
        self.limpa_servicos()
        self.select_lista_ser()   

    def grava_servicos(self):
        self.var_servicos()
        if self.erro == 1:
            return
        self.conecta_col()
        self.cursor_col.execute("insert into servicos(empresa, revenda, cod_servico) values (?, ?, ?)",(self.empresa, self.revenda, self.codigo))
        self.banco_col.commit()
        self.desconecta_col()
        messagebox.showinfo('Gravação', 'Registro ds servico incluido com sucesso')
        self.limpa_servicos()
        self.select_lista_ser()

    def select_lista_ser(self):
        self.lista_ser.delete(*self.lista_ser.get_children())
        self.conecta_col()
        lista = self.cursor_col.execute('''SELECT empresa, revenda, cod_servico FROM servicos''')
        for i in lista:
            self.lista_ser.insert("", END, values=i)
        self.desconecta_col()    
   
    def grade_servicos(self):
        self.lista_ser = ttk.Treeview(self.frame_grid, columns=('EMPRESA', 'REVENDA', 'COD_SERVICO'), show='headings')
        self.lista_ser.heading('#1', text='Empresa')
        self.lista_ser.heading('#2', text='Revenda')
        self.lista_ser.heading('#3', text='Código do Serviço')
        self.lista_ser.column('#1', width=1)
        self.lista_ser.column('#2', width=1)
        self.lista_ser.column('#3', width=300)
        self.lista_ser.place(relx = 0.16, rely = 0.05, relheight=0.90, relwidth=0.70)
        self.scr_lista_ser = Scrollbar(self.frame_grid, orient='vertical')
        self.lista_ser.configure(yscroll = self.scr_lista_ser)
        self.scr_lista_ser.place(relx = 0.86, rely = 0.05, relwidth = 0.03, relheight = 0.89)
        self.select_lista_ser()
        self.lista_ser.bind('<Double-1>', self.ClickDuplo_servicos)

    def entry_servicos(self):
        self.limpa_frame()
        self.lbl_titulo = Label(self.frame_dados, text = 'Cadastro de Serviços', font=('verdana', 20, 'bold'))
        self.lbl_titulo.place(relx = 0.30, rely = 0.02)
        self.lbl_empresa = Label(self.frame_dados, text = 'Empresa',font=('verdana', 8, 'bold'))
        self.lbl_empresa.place(relx = 0.15, rely = 0.35)
        self.ent_empresa = Entry(self.frame_dados, width=2)
        self.ent_empresa.place(relx = 0.18, rely = 0.50)
        self.lbl_revenda = Label(self.frame_dados, text = 'Revenda',font=('verdana', 8, 'bold'))
        self.lbl_revenda.place(relx = 0.25, rely = 0.35)
        self.ent_revenda = Entry(self.frame_dados, width=2)
        self.ent_revenda.place(relx = 0.28, rely = 0.50)
        self.lbl_codigo = Label(self.frame_dados, text = 'Código do serviço',font=('verdana', 8, 'bold'))
        self.lbl_codigo.place(relx = 0.45, rely = 0.35)
        self.ent_codigo = Entry(self.frame_dados, width=50)
        self.ent_codigo.place(relx = 0.45, rely = 0.5)
        self.btn_grava_s = Button(self.frame_dados, text='GRAVA', bg = '#D3D3D3', font=('verdana', 8,'bold'), height = 1, width = 10, command=self.grava_servicos)
        self.btn_grava_s.place(relx = 0.20, rely = 0.75)
        self.btn_altera_s = Button(self.frame_dados, text='ALTERA', bg = '#D3D3D3', font=('verdana', 8,'bold'), height = 1, width = 10, command=self.altera_servicos)
        self.btn_altera_s.place(relx = 0.45, rely = 0.75)
        self.btn_exclui_s = Button(self.frame_dados, text='EXCLUI', bg = '#D3D3D3', font=('verdana', 8,'bold'), height = 1, width = 10, command=self.apaga_servicos)
        self.btn_exclui_s.place(relx = 0.7, rely = 0.75)
        self.grade_servicos()