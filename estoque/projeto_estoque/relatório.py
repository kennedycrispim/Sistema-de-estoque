import pandas as pd
import time
import sqlite3

class Relatorio:
    def __init__(self):
        #Estabelecemos a conexão com o banco de dados caso exista, se não ela é criada
        self.conexao = sqlite3.connect("estoque.db")
        self.cursor = self.conexao.cursor()    
   
    
    #Método para gerar relatório de itens com maior estoque
    def maior_estoque(self):                
        #Comando SQL que será executado
        df = pd.read_sql_query("""
                                    SELECT produto, MAX(qtd) FROM estoque 
                                    GROUP BY produto ORDER BY MAX(qtd) 
                                    DESC LIMIT 10
                               """, self.conexao)
        self.cursor.fetchall()
        time.sleep(1.5)
        
        #Imprimimos o relatório para o usuário 
        print("")
        print("Top 10 - Itens com maior estoque")
        print(df)
                
    #Método    
    def menor_estoque(self): 
        #Estabelecemos a conexão com o banco de dados caso exista, se não ele é criado 
        con = sqlite3.connect("estoque.db")
        cursor = con.cursor()
        cursor.fetchall()
        
        df = pd.read_sql_query("SELECT produto, MIN(qtd) FROM estoque GROUP BY produto ORDER BY MIN(qtd) ASC LIMIT 5", con)
        
        time.sleep(1.5)
        print("")
        print("Top 5 - Itens com menor estoque")
        print(df)
    
    #Método para gerar relatório semanal   
    def movimentacao_periodo(self, data_inicial, data_final): 
        #Comando SQL que será executado
        df = pd.read_sql_query(f"""
                                    SELECT * FROM entrada WHERE data_entrada 
                                    BETWEEN '{data_inicial}' AND '{data_final}' 
                                    ORDER BY data_entrada ASC
                               """, self.conexao)
        self.cursor.fetchall()
        
        #Imprimimos o relatório para o usuário 
        time.sleep(1.5)
        print("")
        print(f"Relatório por período - {data_inicial} a {data_final}")
        print(df)
        
    #Método    
    def entradas_tipo(self, produto): 
        try:
            #Estabelecemos a conexão com o banco de dados caso exista, se não ele é criado 2
            con = sqlite3.connect("estoque.db")
            cursor = con.cursor()
            cursor.fetchall()
            
            
            #Comando SQL que será executado
            df = pd.read_sql_query(f"SELECT produto,qtd,nf,data_entrada FROM entrada WHERE produto = '{produto}'", con)
            time.sleep(1)
            
            print("")
            print(f"Relatório de entrada - {produto}")
            print(df)
        except ValueError:
            print("prduto não encontrado!")    
    
    #Método produtos por nf
    def entrada_nf(self, nf):
        #Estabelecemos a conexão com o banco de dados caso exista, se não ele é criado 
        con = sqlite3.connect("estoque.db")
        cursor = con.cursor()
        cursor.fetchall()
        
        df = pd.read_sql_query(f"SELECT produto,qtd,nf,data_entrada FROM entrada WHERE nf = {nf}", con)
        time.sleep(1)
        print("")
        print(df)