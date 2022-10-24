from Modulos import *

class Pre_Dados():

    def limpa_tab(self):
        self.conecta_col()
        self.cursor_col.execute('DELETE FROM itens_s')
        self.cursor_col.execute('DELETE FROM itens_p')
        self.cursor_col.execute('DELETE FROM notas')
        self.banco_col.commit()
        self.desconecta_col()
############################# Le e grava CAPA de notas
        self.conecta_DB()
        self.conecta_col()
        if self.bancodados == 'SQLSERVER':
            self.cursor.execute("SELECT fmc.EMPRESA, fmc.REVENDA, fmc.NUMERO_NOTA_FISCAL, fmc.SERIE_NOTA_FISCAL, fmc.TIPO_TRANSACAO, fmc.TOT_SERVICOS-fmc.VALDESCONTO_MO AS SERVICOS, fmc.TOT_MERCADORIA-fmc.VALDESCONTO AS PECAS, fmc.USUARIO, fv.NOME, fmc.DTA_ENTRADA_SAIDA FROM FAT_MOVIMENTO_CAPA fmc left join FAT_TIPO_TRANSACAO ftt on ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO left join FAT_VENDEDOR fv ON fv.VENDEDOR = fmc.USUARIO and fv.EMPRESA = fmc.EMPRESA and fv.REVENDA = fmc.REVENDA where fmc.STATUS = 'F' and fmc.modalidade = 'V' and ftt.tipo = 'S'and ftt.SUBTIPO_TRANSACAO = 'N' and fmc.EMPRESA = " + self.empresa + " and fmc.REVENDA = " + self.revenda + " AND fmc.DTA_ENTRADA_SAIDA BETWEEN '"+ self.data_ini + "' AND '" + self.data_fim + "'")
        else:
            self.cursor.execute("SELECT fmc.EMPRESA, fmc.REVENDA, fmc.NUMERO_NOTA_FISCAL, fmc.SERIE_NOTA_FISCAL, fmc.TIPO_TRANSACAO, fmc.TOT_SERVICOS-fmc.VALDESCONTO_MO AS SERVICOS, fmc.TOT_MERCADORIA-fmc.VALDESCONTO AS PECAS, fmc.USUARIO, fv.NOME, fmc.DTA_ENTRADA_SAIDA FROM FAT_MOVIMENTO_CAPA fmc left join FAT_TIPO_TRANSACAO ftt on ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO left join FAT_VENDEDOR fv ON fv.VENDEDOR = fmc.USUARIO and fv.EMPRESA = fmc.EMPRESA and fv.REVENDA = fmc.REVENDA where fmc.STATUS = 'F' and fmc.modalidade = 'V' and ftt.tipo = 'S'and ftt.SUBTIPO_TRANSACAO = 'N' and fmc.EMPRESA = " + self.empresa + " and fmc.REVENDA = " + self.revenda + " AND fmc.DTA_ENTRADA_SAIDA BETWEEN TO DATE('"+ self.data_ini + ",'dd/mm/yyyy')' AND TO DATE('" + self.data_fim + ",'dd/mm/yyyy')'")
        for linha in self.cursor.fetchall():# A variavel linha é uma tupla
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
            self.cursor_col.execute("INSERT INTO notas(EMPRESA, REVENDA, NUMERO_NOTA_FISCAL, SERIE_NOTA_FISCAL, TIPO_TRANSACAO, SERVICO, PECA, USUARIO, NOME, DTA_ENTRADA_SAIDA) VALUES(? ,? ,? ,? ,? ,? ,? ,? ,?, ?)", (empresa,revenda,nota,serie,transacao,servico,peca,usuario,nome,data))
        self.banco_col.commit()
############################# Le e grava PECAS das notas
        if self.bancodados == 'SQLSERVER':
            self.cursor.execute("SELECT fmi.EMPRESA, fmi.REVENDA, fmi.NUMERO_NOTA_FISCAL, fmi.SERIE_NOTA_FISCAL, pie.ITEM_ESTOQUE_PUB, pie.DES_ITEM_ESTOQUE, fmi.QUANTIDADE, fmi.VAL_UNITARIO_ITEM_4CASAS, fmi.VAL_CUSTO_MEDIO, fmi.VAL_DEVERIA, fmi.VAL_DESCONTO, fmi.QUANTIDADE * fmi.VAL_UNITARIO_ITEM_4CASAS - fmi.VAL_DESCONTO AS Total_liquido, fmc.DTA_ENTRADA_SAIDA FROM FAT_MOVIMENTO_ITEM fmi LEFT JOIN FAT_MOVIMENTO_CAPA fmc ON fmc.EMPRESA = fmi.EMPRESA AND fmc.REVENDA = fmi.REVENDA AND fmc.NUMERO_NOTA_FISCAL = fmi.NUMERO_NOTA_FISCAL AND fmc.SERIE_NOTA_FISCAL = fmi.SERIE_NOTA_FISCAL AND fmc.TIPO_TRANSACAO = fmi.TIPO_TRANSACAO LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmi.TIPO_TRANSACAO left JOIN PEC_ITEM_ESTOQUE pie ON pie.EMPRESA = fmi.EMPRESA AND pie.ITEM_ESTOQUE = fmi.ITEM_ESTOQUE where fmc.STATUS = 'F' and fmc.modalidade = 'V' and ftt.tipo = 'S' and ftt.SUBTIPO_TRANSACAO = 'N' and fmc.EMPRESA = " + self.empresa + " and fmc.REVENDA = " + self.revenda + " AND fmc.DTA_ENTRADA_SAIDA BETWEEN '" + self.data_ini +"' AND '" + self.data_fim +"'")
        else:
            self.cursor.execute("SELECT fmi.EMPRESA, fmi.REVENDA, fmi.NUMERO_NOTA_FISCAL, fmi.SERIE_NOTA_FISCAL, pie.ITEM_ESTOQUE_PUB, pie.DES_ITEM_ESTOQUE, fmi.QUANTIDADE, fmi.VAL_UNITARIO_ITEM_4CASAS, fmi.VAL_CUSTO_MEDIO, fmi.VAL_DEVERIA, fmi.VAL_DESCONTO, fmi.QUANTIDADE * fmi.VAL_UNITARIO_ITEM_4CASAS - fmi.VAL_DESCONTO AS Total_liquido, fmc.DTA_ENTRADA_SAIDA FROM FAT_MOVIMENTO_ITEM fmi LEFT JOIN FAT_MOVIMENTO_CAPA fmc ON fmc.EMPRESA = fmi.EMPRESA AND fmc.REVENDA = fmi.REVENDA AND fmc.NUMERO_NOTA_FISCAL = fmi.NUMERO_NOTA_FISCAL AND fmc.SERIE_NOTA_FISCAL = fmi.SERIE_NOTA_FISCAL AND fmc.TIPO_TRANSACAO = fmi.TIPO_TRANSACAO LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmi.TIPO_TRANSACAO left JOIN PEC_ITEM_ESTOQUE pie ON pie.EMPRESA = fmi.EMPRESA AND pie.ITEM_ESTOQUE = fmi.ITEM_ESTOQUE where fmc.STATUS = 'F' and fmc.modalidade = 'V' and ftt.tipo = 'S' and ftt.SUBTIPO_TRANSACAO = 'N' and fmc.EMPRESA = " + self.empresa + " and fmc.REVENDA = " + self.revenda + " AND fmc.DTA_ENTRADA_SAIDA BETWEEN TO DATE ('" + self.data_ini +",'dd/mm/yyyy') AND TO DATE ('" + self.data_fim +",'dd/mm/yyyy')'")
        for linha in self.cursor.fetchall():
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
            self.cursor_col.execute("INSERT INTO itens_p(EMPRESA, REVENDA, NUMERO_NOTA_FISCAL, SERIE_NOTA_FISCAL, ITEM_ESTOQUE_PUB, DES_ITEM_ESTOQUE, QUANTIDADE, VAL_UNITARIO, VAL_CUSTO_MEDIO, VAL_DEVERIA, VAL_DESCONTO, TOTAL_LIQUIDO, DTA_ENTRADA_SAIDA) VALUES(? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,?, ?)", (empresa,revenda,nota,serie,item_pub,des_item,quantidade,unitario,customedio,deveria,desconto,liquido,data))
        self.banco_col.commit()

############################# Le e grava SERVICOS das notas
        if self.bancodados == 'SQLSERVER':
            self.cursor.execute("SELECT fms.EMPRESA, fms.REVENDA, fms.NUMERO_NOTA_FISCAL, fms.SERIE_NOTA_FISCAL, os.SERVICO, fms.DESCRICAO, os.MAODEOBRA, fms.QUANTIDADE, fms.VAL_REAL_UNITARIO, fms.VAL_DESCONTO, fms.VAL_REAL_UNITARIO * fms.QUANTIDADE - fms.VAL_DESCONTO AS Total_Liquido, fmc.DTA_ENTRADA_SAIDA FROM FAT_MOVIMENTO_SERVICO fms LEFT JOIN FAT_MOVIMENTO_CAPA fmc ON fmc.EMPRESA = fms.EMPRESA AND fmc.REVENDA = fms.REVENDA AND fmc.NUMERO_NOTA_FISCAL = fms.NUMERO_NOTA_FISCAL AND fmc.SERIE_NOTA_FISCAL = fms.SERIE_NOTA_FISCAL AND fmc.TIPO_TRANSACAO = fms.TIPO_TRANSACAO LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fms.TIPO_TRANSACAO LEFT JOIN OFI_SERVICO os ON os.EMPRESA = fms.EMPRESA AND os.SERVICO = fms.SERVICO where fmc.STATUS = 'F' and fmc.modalidade = 'V' and ftt.tipo = 'S' and ftt.SUBTIPO_TRANSACAO = 'N' and fmc.EMPRESA = " + self.empresa +" and fmc.REVENDA = " + self.revenda + " AND fmc.DTA_ENTRADA_SAIDA BETWEEN '" + self.data_ini + "' AND '" + self.data_fim + "'")
        else:
            self.cursor.execute("SELECT fms.EMPRESA, fms.REVENDA, fms.NUMERO_NOTA_FISCAL, fms.SERIE_NOTA_FISCAL, os.SERVICO, fms.DESCRICAO, os.MAODEOBRA, fms.QUANTIDADE, fms.VAL_REAL_UNITARIO, fms.VAL_DESCONTO, fms.VAL_REAL_UNITARIO * fms.QUANTIDADE - fms.VAL_DESCONTO AS Total_Liquido, fmc.DTA_ENTRADA_SAIDA FROM FAT_MOVIMENTO_SERVICO fms LEFT JOIN FAT_MOVIMENTO_CAPA fmc ON fmc.EMPRESA = fms.EMPRESA AND fmc.REVENDA = fms.REVENDA AND fmc.NUMERO_NOTA_FISCAL = fms.NUMERO_NOTA_FISCAL AND fmc.SERIE_NOTA_FISCAL = fms.SERIE_NOTA_FISCAL AND fmc.TIPO_TRANSACAO = fms.TIPO_TRANSACAO LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fms.TIPO_TRANSACAO LEFT JOIN OFI_SERVICO os ON os.EMPRESA = fms.EMPRESA AND os.SERVICO = fms.SERVICO where fmc.STATUS = 'F' and fmc.modalidade = 'V' and ftt.tipo = 'S' and ftt.SUBTIPO_TRANSACAO = 'N' and fmc.EMPRESA = " + self.empresa +" and fmc.REVENDA = " + self.revenda + " AND fmc.DTA_ENTRADA_SAIDA BETWEEN TO DATE ('" + self.data_ini + ",'dd/mm/yyyy')' AND TO DATE ('" + self.data_fim + ",'dd/mm/yyyy')'")
        for linha in self.cursor.fetchall():
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
            self.cursor_col.execute("INSERT INTO ITENS_s(EMPRESA, REVENDA, NUMERO_NOTA_FISCAL, SERIE_NOTA_FISCAL, SERVICO, DESCRICAO, MAODEOBRA, QUANTIDADE, VAL_UNITARIO, VAL_DESCONTO, TOTAL_LIQUIDO, DTA_ENTRADA_SAIDA) VALUES(? ,? ,? ,? ,? ,? ,?, ? ,? ,? ,? , ?)", (empresa,revenda,nota,serie,servico,descricao,maodeobra,quantidade,unitario,desconto,liquido,data))
        self.banco_col.commit()
        self.desconecta_DB()
        self.desconecta_col()

########################################################################################################################
# Extração dos dados banco temporario para DataFrame e salvar em Excel
########################################################################################################################
        self.conecta_col()

# ---------------------- Gera DataFrame venda peças
        self.vendedor = ''
        self.peca = ''
        self.servico = ''
        self.cursor_col.execute("select cod_usuario from consultores where empresa ="+self.empresa+" and revenda = "+self.revenda)
        for vend in self.cursor_col.fetchall():
            self.vendedor = self.vendedor + "'"+vend[0]+"',"
            self.vendedores = self.vendedor[:-1]
        self.cursor_col.execute("select cod_item from pecas where empresa ="+self.empresa+" and revenda = "+self.revenda)
        for pec in self.cursor_col.fetchall():
            self.peca = self.peca + "'"+pec[0]+"',"
            self.pecas = self.peca[:-1]
        self.cursor_col.execute("select cod_servico from servicos where empresa ="+self.empresa+" and revenda = "+self.revenda)
        for serv in self.cursor_col.fetchall():
            self.servico = self.servico + "'"+serv[0]+"',"
            self.servicos = self.servico[:-1]
        self.conecta_col()    

        sql_pecas = ("SELECT n.USUARIO as 'VENDEDOR', n.NOME as 'NOME DO VENDEDOR', p.item_estoque_pub as 'CODIGO ITEM', p.DES_ITEM_ESTOQUE as 'DESCRICAO DO ITEM' , p.QUANTIDADE, sum(p.TOTAL_LIQUIDO) as 'TOTAL LIQUIDO', sum(p.VAL_CUSTO_MEDIO) as 'TOTAL CUSTO MEDIO', ((sum(p.TOTAL_LIQUIDO)/sum(p.VAL_CUSTO_MEDIO))-1)*100 as '% LUCRO', p.VAL_DEVERIA as 'VALOR TABELA' FROM notas n INNER JOIN itens_p p ON p.EMPRESA = n.EMPRESA AND p.REVENDA = n.REVENDA AND n.NUMERO_NOTA_FISCAL = p.NUMERO_NOTA_FISCAL AND n.SERIE_NOTA_FISCAL = p.SERIE_NOTA_FISCAL WHERE n.USUARIO in ("+self.vendedores+") and p.item_estoque_pub in ("+self.pecas+") GROUP BY n.NOME, p.DES_ITEM_ESTOQUE")
        sql_servicos = ("SELECT n.USUARIO AS 'VENDEDOR', n.NOME AS 'NOME DO VENDEDOR', s.MAODEOBRA AS 'CODIGO DO SERVICO', s.DESCRICAO AS 'DESCRICAO DO SERVICO', sum(s.TOTAL_LIQUIDO) AS 'TOTAL LIQUIDO' FROM notas n INNER JOIN itens_s s ON s.EMPRESA = n.EMPRESA AND s.REVENDA = n.REVENDA AND s.NUMERO_NOTA_FISCAL = n.NUMERO_NOTA_FISCAL AND s.SERIE_NOTA_FISCAL = n.SERIE_NOTA_FISCAL WHERE n.USUARIO IN ("+self.vendedores+") AND s.MAODEOBRA  IN ("+self.servicos+") GROUP BY n.NOME, s.MAODEOBRA")

        df_venda_pecas = pd.read_sql(sql_pecas, self.banco_col) 
        df_venda_servicos = pd.read_sql(sql_servicos, self.banco_col) 

        nome_planilha = 'Mov_'+ self.empresa + '_'+ self.revenda+'_ Peças'
        df_venda_pecas.to_excel(nome_planilha, index = False)

        nome_planilha = 'Mov_'+ self.empresa + '_'+ self.revenda+'_ Serviços'
        df_venda_servicos.to_excel(nome_planilha, index = False)