from Modulos import *

salvar = datetime.today().strftime('%d-%m-%Y_%H-%M')
corpodata1 = datetime.today().strftime('-%m-%Y')
corpodata2 = datetime.today().strftime('%d-%m-%Y')

class Adict():

    def pega_dados(self, caminho, aba, coluna):
        self.df_var = pd.read_excel(caminho, sheet_name= aba, usecols = coluna)
        self.tam = len(self.df_var)
        self.var1 = '#'
        for a in range(self.tam):
            if aba == 'Consultores':
                self.var1 = self.var1 + self.df_var.loc[a].astype(str) + ', '
            else:
                self.var1 = self.var1 + self.df_var.loc[a].astype(str) + '", "'    
        self.var2 = self.var1.to_frame()
        self.var = self.var2.to_string()
        self.pos = self.var.find('#')
        if self.aba == 'Consultores':
            self.var_fin = self.var[self.pos+1:-2]
        else:
            self.var_fin = '"' + self.var[self.pos+1:-3] 
        return self.var_fin

    def cria_banco(self):  # Verifica e se nao existir, cria o diretorio
        self.banco_bi = sqlite3.connect(self.caminho+'\Coletor_DB.db')
        self.c = self.banco_bi.cursor()
        
        self.c.execute("CREATE TABLE notas "
                  "(EMPRESA integer, "
                  "REVENDA integer, "
                  "NUMERO_NOTA_FISCAL integer, "
                  "SERIE_NOTA_FISCAL text, "
                  "TIPO_TRANSACAO text, "
                  "SERVICO real, "
                  "PECA real, "
                  "USUARIO integer, "
                  "NOME text, "
                  "DTA_ENTRADA_SAIDA date)")

        self.c.execute("CREATE TABLE pecas "
                  "(EMPRESA integer, "
                  "REVENDA integer, "
                  "NUMERO_NOTA_FISCAL integer, "
                  "SERIE_NOTA_FISCAL text, "
                  "ITEM_ESTOQUE_PUB text, "
                  "DES_ITEM_ESTOQUE text, "
                  "QUANTIDADE real, "
                  "VAL_UNITARIO real, "
                  "VAL_CUSTO_MEDIO real, "
                  "VAL_DEVERIA real, "
                  "VAL_DESCONTO real, "
                  "TOTAL_LIQUIDO real, "
                  "DTA_ENTRADA_SAIDA date)")

        self.c.execute("CREATE TABLE servicos "
                  "(EMPRESA integer, "
                  "REVENDA integer, "
                  "NUMERO_NOTA_FISCAL integer, "
                  "SERIE_NOTA_FISCAL text, "
                  "SERVICO integer, "
                  "MAODEOBRA text, "
                  "DESCRICAO text, "
                  "QUANTIDADE real, "
                  "VAL_UNITARIO real, "
                  "VAL_DESCONTO real, "
                  "TOTAL_LIQUIDO real, "
                  "DTA_ENTRADA_SAIDA date)")

#--------------- Lê planilha com informacao de vendedores, pecas e serviços

        self.caminho = 'c:\Coletor\parametros.xlsx'
        self.baseprog = self.pega_dados('base1.xlsx', 'Planilha1')
        self.baseprog = self.baseprog[1:-1]
        self.vendedorx = self.pega_dados('base2.xlsx', 'Planilha1')
        self.vendedor = str(self.vendedorx) 
        self.peca = self.pega_dados(self.caminho, 'Pecas', 'A')
        self.pecas = str(self.peca)
        self.servico = self.pega_dados(self.caminho, 'Servicos', 'A')
        self.servicos = str(self.servico)

#--------------------------------------------------------------------------
        self.diretorio = Path(r"c:\Coletor") # Verifica, se nao existe o diretorio, cria
        if self.diretorio.is_dir():
            print("")
        else:
            os.makedirs(r"c:\Coletor")
#------------------------
        self.arquivo = Path(r"c:\Coletor\Coletor_DB.db") # Verifica, se existe apaga e recria, senao somente cria.
        if self.arquivo.is_file():
            os.remove(r"c:\Coletor\Coletor_DB.db")
            self.cria_banco()
        else:
            self.cria_banco()

############################# Le e grava CAPA de notas
        self.conecta_DB()
        cursor.execute("SELECT fmc.EMPRESA, fmc.REVENDA, fmc.NUMERO_NOTA_FISCAL, fmc.SERIE_NOTA_FISCAL, fmc.TIPO_TRANSACAO, fmc.TOT_SERVICOS-fmc.VALDESCONTO_MO AS SERVICOS, fmc.TOT_MERCADORIA-fmc.VALDESCONTO AS PECAS, fmc.USUARIO, fv.NOME, fmc.DTA_ENTRADA_SAIDA FROM FAT_MOVIMENTO_CAPA fmc left join FAT_TIPO_TRANSACAO ftt on ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO left join FAT_VENDEDOR fv ON fv.VENDEDOR = fmc.USUARIO and fv.EMPRESA = fmc.EMPRESA and fv.REVENDA = fmc.REVENDA where fmc.STATUS = 'F' and fmc.modalidade = 'V' and ftt.tipo = 'S'and ftt.SUBTIPO_TRANSACAO = 'N' and fmc.EMPRESA = " + xempresa + " and fmc.REVENDA = " + xrevenda + " AND fmc.DTA_ENTRADA_SAIDA BETWEEN '"+ xdataini + "' AND '" + xdatafin + "'")

        for linha in cursor.fetchall():# A variavel linha é uma tupla
            empresa = int(linha[0])
            revenda = int(linha[1])
            nota = int(linha[2])
            serie = linha[3]
            transacao = linha[4]
            servico = float(linha[5])
            peca = float(linha[6])
            usuario = int(linha[7])
            nome = linha[8]
            data = datetime.date(linha[9])
            cp.execute("INSERT INTO notas(EMPRESA, REVENDA, NUMERO_NOTA_FISCAL, SERIE_NOTA_FISCAL, TIPO_TRANSACAO, SERVICO, PECA, USUARIO, NOME, DTA_ENTRADA_SAIDA) VALUES(? ,? ,? ,? ,? ,? ,? ,? ,?, ?)", (empresa,revenda,nota,serie,transacao,servico,peca,usuario,nome,data))
        banco_bip.commit()
        desconecta_DB()
############################# Le e grava PECAS das notas
        cursor.execute("SELECT fmi.EMPRESA, fmi.REVENDA, fmi.NUMERO_NOTA_FISCAL, fmi.SERIE_NOTA_FISCAL, pie.ITEM_ESTOQUE_PUB, pie.DES_ITEM_ESTOQUE, fmi.QUANTIDADE, fmi.VAL_UNITARIO_ITEM_4CASAS, fmi.VAL_CUSTO_MEDIO, fmi.VAL_DEVERIA, fmi.VAL_DESCONTO, fmi.QUANTIDADE * fmi.VAL_UNITARIO_ITEM_4CASAS - fmi.VAL_DESCONTO AS Total_liquido, fmc.DTA_ENTRADA_SAIDA FROM FAT_MOVIMENTO_ITEM fmi LEFT JOIN FAT_MOVIMENTO_CAPA fmc ON fmc.EMPRESA = fmi.EMPRESA AND fmc.REVENDA = fmi.REVENDA AND fmc.NUMERO_NOTA_FISCAL = fmi.NUMERO_NOTA_FISCAL AND fmc.SERIE_NOTA_FISCAL = fmi.SERIE_NOTA_FISCAL AND fmc.TIPO_TRANSACAO = fmi.TIPO_TRANSACAO LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmi.TIPO_TRANSACAO left JOIN PEC_ITEM_ESTOQUE pie ON pie.EMPRESA = fmi.EMPRESA AND pie.ITEM_ESTOQUE = fmi.ITEM_ESTOQUE where fmc.STATUS = 'F' and fmc.modalidade = 'V' and ftt.tipo = 'S' and ftt.SUBTIPO_TRANSACAO = 'N' and fmc.EMPRESA = " + xempresa + " and fmc.REVENDA = " + xrevenda + " AND fmc.DTA_ENTRADA_SAIDA BETWEEN '" + xdataini +"' AND '" + xdatafin +"'")

        for linha in cursor.fetchall():
            empresa = int(linha[0])
            revenda = int(linha[1])
            nota = int(linha[2])
            serie = linha[3]
            item_pub = linha[4]
            des_item = linha[5]
            quantidade = float(linha[6])
            unitario = float(linha[7])
            customedio = float(linha[8]) 
            deveria = float(linha[9])
            desconto = float(linha[10])
            liquido = float(linha[11])
            data = datetime.date(linha[12])
            cp.execute("INSERT INTO pecas(EMPRESA, REVENDA, NUMERO_NOTA_FISCAL, SERIE_NOTA_FISCAL, ITEM_ESTOQUE_PUB, DES_ITEM_ESTOQUE, QUANTIDADE, VAL_UNITARIO, VAL_CUSTO_MEDIO, VAL_DEVERIA, VAL_DESCONTO, TOTAL_LIQUIDO, DTA_ENTRADA_SAIDA) VALUES(? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,?, ?)", (empresa,revenda,nota,serie,item_pub,des_item,quantidade,unitario,customedio,deveria,desconto,liquido,data))
            banco_bip.commit()

############################# Le e grava SERVICOS das notas
        cursor.execute("SELECT fms.EMPRESA, fms.REVENDA, fms.NUMERO_NOTA_FISCAL, fms.SERIE_NOTA_FISCAL, os.SERVICO, fms.DESCRICAO, os.MAODEOBRA, fms.QUANTIDADE, fms.VAL_REAL_UNITARIO, fms.VAL_DESCONTO, fms.VAL_REAL_UNITARIO * fms.QUANTIDADE - fms.VAL_DESCONTO AS Total_Liquido, fmc.DTA_ENTRADA_SAIDA FROM FAT_MOVIMENTO_SERVICO fms LEFT JOIN FAT_MOVIMENTO_CAPA fmc ON fmc.EMPRESA = fms.EMPRESA AND fmc.REVENDA = fms.REVENDA AND fmc.NUMERO_NOTA_FISCAL = fms.NUMERO_NOTA_FISCAL AND fmc.SERIE_NOTA_FISCAL = fms.SERIE_NOTA_FISCAL AND fmc.TIPO_TRANSACAO = fms.TIPO_TRANSACAO LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fms.TIPO_TRANSACAO LEFT JOIN OFI_SERVICO os ON os.EMPRESA = fms.EMPRESA AND os.SERVICO = fms.SERVICO where fmc.STATUS = 'F' and fmc.modalidade = 'V' and ftt.tipo = 'S' and ftt.SUBTIPO_TRANSACAO = 'N' and fmc.EMPRESA = " + xempresa +" and fmc.REVENDA = " + xrevenda + " AND fmc.DTA_ENTRADA_SAIDA BETWEEN '" + xdataini + "' AND '" + xdatafin + "'")

        for linha in cursor.fetchall():
            empresa = int(linha[0])
            revenda = int(linha[1])
            nota = int(linha[2])
            serie = linha[3]
            servico = int(linha[4])
            descricao = linha[5]
            maodeobra = linha[6]
            quantidade = float(linha[7])
            unitario = float(linha[8])
            desconto = float(linha[9])
            liquido = float(linha[10])
            data = datetime.date(linha[11])
            cp.execute("INSERT INTO servicos(EMPRESA, REVENDA, NUMERO_NOTA_FISCAL, SERIE_NOTA_FISCAL, SERVICO, DESCRICAO, MAODEOBRA, QUANTIDADE, VAL_UNITARIO, VAL_DESCONTO, TOTAL_LIQUIDO, DTA_ENTRADA_SAIDA) VALUES(? ,? ,? ,? ,? ,? ,?, ? ,? ,? ,? , ?)", (empresa,revenda,nota,serie,servico,descricao,maodeobra,quantidade,unitario,desconto,liquido,data))
            banco_bip.commit()
        cursor.close()
        cp.close()

########################################################################################################################
# Extração dos dados banco temporario para DataFrame e salvar em Excel
########################################################################################################################
        exporta = sqlite3.connect(r"c:\coletor\Coletor_DB.db") # Abre banco para ser populado
        cp = exporta.cursor()

# ---------------------- Gera DataFrame venda peças
        sql_pecas = ("SELECT n.USUARIO as 'VENDEDOR', n.NOME as 'NOME DO VENDEDOR', p.item_estoque_pub as 'CODIGO ITEM', p.DES_ITEM_ESTOQUE as 'DESCRICAO DO ITEM' , p.QUANTIDADE, sum(p.TOTAL_LIQUIDO) as 'TOTAL LIQUIDO', sum(p.VAL_CUSTO_MEDIO) as 'TOTAL CUSTO MEDIO', ((sum(p.TOTAL_LIQUIDO)/sum(p.VAL_CUSTO_MEDIO))-1)*100 as '% LUCRO', p.VAL_DEVERIA as 'VALOR TABELA' FROM notas n INNER JOIN pecas p ON p.EMPRESA = n.EMPRESA AND p.REVENDA = n.REVENDA AND n.NUMERO_NOTA_FISCAL = p.NUMERO_NOTA_FISCAL AND n.SERIE_NOTA_FISCAL = p.SERIE_NOTA_FISCAL WHERE n.USUARIO in ("+vendedor+") and p.item_estoque_pub in ("+pecas+") GROUP BY n.NOME, p.DES_ITEM_ESTOQUE")
        sql_servicos = ("SELECT n.USUARIO AS 'VENDEDOR', n.NOME AS 'NOME DO VENDEDOR', s.MAODEOBRA AS 'CODIGO DO SERVICO', s.DESCRICAO AS 'DESCRICAO DO SERVICO', sum(s.TOTAL_LIQUIDO) AS 'TOTAL LIQUIDO' FROM notas n INNER JOIN servicos s ON s.EMPRESA = n.EMPRESA AND s.REVENDA = n.REVENDA AND s.NUMERO_NOTA_FISCAL = n.NUMERO_NOTA_FISCAL AND s.SERIE_NOTA_FISCAL = n.SERIE_NOTA_FISCAL WHERE n.USUARIO IN ("+vendedor+") AND s.MAODEOBRA  IN ("+servicos+") GROUP BY n.NOME, s.MAODEOBRA")

        df_venda_pecas = pd.read_sql(sql_pecas, exporta) 
        df_venda_servicos = pd.read_sql(sql_servicos, exporta) 

        nome_planilha = 'Mov_'+ xempresa + '_'+ xrevenda+'_'+salvar
        df_venda_pecas.to_excel(nome_planilha, index = False)
