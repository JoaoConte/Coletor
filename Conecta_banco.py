from Modulos import *

class Conexao():
    def le_conexao(self):  # Lê ..\conexao.dat
        self.caminho = os.path.abspath(os.path.dirname('.')) # Pega diretorio atual
        try:
            with open(self.caminho + '\conexao.dat', 'r') as conecta:
                for self.leitura in conecta:
                    if self.leitura[0:12] == '[BANCODADOS]':
                        self.bancodados = self.leitura[13:]
                        self.bancodados = self.bancodados.strip("\n")
                        if self.bancodados == 'SQLSERVER':
                            self.drive = "SQL Server"
                    if self.leitura[0:10] == '[DATABASE]':
                        if self.bancodados == 'SQLSERVER':
                            self.posp = self.leitura.find(':')
                            self.servidor = self.leitura[11:self.posp]
                            self.banco1 = self.leitura[self.posp + 1:]
                            self.banco = self.banco1.strip("\n")
                        elif self.bancodados == 'ORACLE':
                            #self.ler_valida()
                            with open(self.caminho + '\conexao_par.dat', 'r') as con_valida:
                                for self.le_valida in con_valida:
                                    if self.le_valida[0:9] == '[USUARIO]':
                                        self.usu_conex1 = self.le_valida[10:]
                                        self.usuario = self.usu_conex1.strip("\n")
                                        #print(self.usuario)
                                    if self.le_valida[0:7] == '[SENHA]':
                                        self.sen_conex1 = self.le_valida[8:]
                                        self.senha = self.sen_conex1.strip('\n')
                                        #print(self.senha)
                                    if self.le_valida[0:6] == '[HOST]':
                                        self.host_conex1 = self.le_valida[7:]
                                        self.host = self.host_conex1.strip('\n')
                                        #print(self.host)
                                    if self.le_valida[0:14] == '[SERVICE_NAME]':
                                        self.serv_conex1 = self.le_valida[15:]
                                        self.service = self.serv_conex1.strip('\n')
                                        #print(self.service)
        except OSError:
            messagebox.showerror('Falha na conexão com o Banco de dados', 'arquivo CONEXÃO.DAT não encontrado!\n'
                                                                          'Verifique se o programa executável está na\n'
                                                                          'pasta do sistema ou se os dados informados\n '
                                                                          'estão corretos')
    def conecta_DB(self):
        if self.bancodados != 'SQLSERVER':
            try:
                self.cbd_ora = cx_Oracle.connect(self.usuario+'/'+self.senha+'@'+self.host+'/'+self.service)
                self.cursor = self.cbd_ora.cursor()
            except:
                messagebox.showerror('Dados Inválidos','Usuário e/ou senha do banco de dados inválidos\n'
                                                       'verifique se os dados informados no arquivo\n'
                                                       'conexao_par estão corretos ou está na mesma pasta\n'
                                                       'onde está o conexão.dat.')
                return
        else:
            try:
                self.cbd_sql = pyodbc.connect(
                    "Driver=" + self.drive + "; Server=" + self.servidor + "; Database=" + self.banco + "; TrustedConnection=yes")
                self.cursor = self.cbd_sql.cursor()
            except:
                messagebox.showerror('Falha na conexão', 'A conexão com o banco de dados falhou, verifique se\nesta aplicação está na mesma pasta do conexao.dat')
                exit()

    def desconecta_DB(self):
        if self.bancodados != 'SQLSERVER':
            self.cbd_ora.close()
        else:
            self.cbd_sql.close()

    def conecta_col(self):
        caminho = os.path.abspath(os.path.dirname('.'))
        self.banco_col = sqlite3.connect(caminho+"\Coletor_DB.db")
        self.cursor_col = self.banco_col.cursor()

    def desconecta_col(self):
        self.banco_col.close()
