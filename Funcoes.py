from Modulos import *

class Funcs():
    def limpa_frame(self):
        try:
            self.lbl_titulo.destroy()
            self.lbl_empresa.destroy()
            self.ent_empresa.destroy()
            self.lbl_revenda.destroy()
            self.ent_revenda.destroy()
            self.lbl_codigo.destroy()
            self.ent_codigo.destroy()
            self.lbl_nome.destroy()
            self.ent_nome.destroy()
            self.btn_grava_c.destroy()
            self.btn_altera_c.destroy()
            self.btn_exclui_c.destroy()
        except:
            pass
        
    def botoes_cadastros(self):
        self.btn_consultor = Button(self.cadastro, text='Consultores', bg = '#D3D3D3', font=('verdana', 10,'bold'), height = 2, width = 15, command=self.entry_consultor)
        self.btn_consultor.place(relx = 0.15, rely = 0.1)
        self.btn_pecas = Button(self.cadastro, text='Peças', bg = '#D3D3D3', font=('verdana', 10,'bold'), height = 2, width = 15, command=self.limpa_frame)
        self.btn_pecas.place(relx = 0.4, rely = 0.1)
        self.btn_servicos = Button(self.cadastro, text='Serviços', bg = '#D3D3D3', font=('verdana', 10,'bold'), height = 2, width = 15)
        self.btn_servicos.place(relx = 0.65, rely = 0.1)

        self.frame_grid = Frame(self.cadastro, height=300, width=700)
        self.frame_grid.pack(side = BOTTOM)
        self.frame_dados = Frame(self.cadastro, height=150, width=700)
        self.frame_dados.pack(side = BOTTOM)


    def abas(self):
        self.tab_control = ttk.Notebook(self.telaval)             # Estanciando o controle de abas
        self.cadastro = Frame(self.tab_control)                   # Estanciando aba Filtro
        self.filtro = Frame(self.tab_control)                     # Estanciando aba de Inconsistencias
        self.resultado = Frame(self.tab_control)                  # Estanciando aba Validada 
        self.tab_control.add(self.cadastro, text=' Cadastros ')     # Definindo aba Filtro
        self.tab_control.add(self.filtro, text=' Filtros ')    # Definindo aba Inconsistencias
        self.tab_control.add(self.resultado, text = ' Resultado ') # Definindo aba itens validados
        self.tab_control.pack(expand=1, fill='both') 

    def dataini(self): # Carrega Data inicial
        self.lbl_ini = Label(self.filtro, text = 'Data inicial', font = ('verdana', 8, 'bold'))
        self.lbl_ini.place(relx = 0.25, rely = 0.42)
        self.ent_ini = DateEntry(self.filtro, locale='pt_br')
        self.data_ini = self.ent_ini.get()
        self.ent_ini.delete(0,END)
        self.ent_ini.place(relx=0.25, rely=0.45)

    def datafim(self): # Carrega Data final
        self.lbl_fim = Label(self.filtro, text = 'Data final', font = ('verdana', 8, 'bold'))
        self.lbl_fim.place(relx = 0.60, rely = 0.42)
        self.ent_fim = DateEntry(self.filtro, locale='pt_br')
        self.data_fim = self.ent_fim.get()
        self.ent_fim.delete(0,END)
        self.ent_fim.place(relx=0.60, rely=0.45)        

    def seleciona_revenda(self):
        try:
            self.listbox_res.destroy()
            self.scroll_res.destroy()
            self.listbox_val.destroy()
            self.scroll_val.destroy()
        except:
            pass    
        self.cria_listbox()
        empresa = []
        revenda = []
        combo_p1 = []
        cnpj = []
        for i in self.listbox.curselection():
            empresa.append(str(self.listbox.get(i)[0]))
            revenda.append(str(self.listbox.get(i)[2]))
            combo_p1.append(str(self.listbox.get(i)[0]) + '.'+str(self.listbox.get(i)[2]) + ' - ' + str(self.listbox.get(i)[6:]))
            cnpj.append(str(self.listbox.get(i)[3]))
        self.empresa = ', '.join(empresa)
        self.revenda = ', '.join(revenda)
        self.combo_p = ', '.join(combo_p1)
        self.cnpj = ', '.join(cnpj)
        self.leitura_banco()   #### Validacao.py
        
    def frame_revenda(self):
        self.lbl_titulo = Label(self.filtro, text = 'Extrator de dados para comissão', font=('verdana', 18, 'bold'))
        self.lbl_titulo.place(relx = 0.18, rely=0.05)
        self.lbl_emprev = Label(self.filtro, text = 'Empresa/Revenda', font=('verdana', 8, 'bold'))
        self.lbl_emprev.place(relx = 0.23, rely=0.14)
        self.conecta_DB()
        self.cursor.execute("SELECT empresa, revenda,razao_social, cnpj FROM GER_REVENDA")
        self.listbox = Listbox(self.filtro, width=63, height=7)
        self.listbox.place(relx=0.23, rely=0.175)
        a = 0
        for linha in self.cursor.fetchall():
            a = a + 1
            self.combo = str(linha[0]) + '.' + str(linha[1]) + ' - ' + linha[2] + ' - CNPJ: ' + linha[3][0:2]+ '.'+ linha[3][2:5] + '.'+ linha[3][5:8]+ '/'+ linha[3][8:12] + '-'+ linha[3][12:14]
            self.listbox.insert(a, self.combo)
       
        btn_validar = Button(self.filtro, text='BUSCAR', font=('verdana', 13, 'bold'), bg = '#D3D3D3', height = 3, 
          width = 10)#, command=self.seleciona_revenda)
        btn_validar.place(relx=0.40, rely=0.85)
        self.desconecta_DB()