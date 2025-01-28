#imports
import sqlite3
import pandas as pd
import time

#Criação da classe pedido
class Pedido:
    #Definindo os atributos de pedido | Método construto
    def __init__(self, pedido = 0, produto = "", qtd = 0, preco = 0):
        self.pedido = pedido 
        self.produto = produto
        self.qtd = qtd 
        self.preco = preco
        self.criar_tabelas()
         
    #Método para criar tabela
    def criar_tabelas(self):    
        """
            Realiza a criação da tabela 'pedido' no banco de dados, 
            principal base de dados que será trabalhada nese módulo
            
            Retorno: tabela 'pedido' é criada.
        """
        #Estabelecemos a conexão com o banco de dados caso exista, se não ela é criada
        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()
        
        #Comando SQL que será executado
        cursor.execute("""
                            CREATE TABLE IF NOT EXISTS pedido (
                                id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                                pedido INTEGER,
                                produto VARCHAR,
                                qtd INTEGER,
                                preco FLOAT
                                )
                       """)
        
    #Método para criar pedido
    def criar_pedidos(self, pedido, produto, qtd, precouni):
        """
        Permite criar um novo pedido
        
        pedido (int) = Número do pedido
        produto (string) = Descrição do produto, nome do produto
        qtd (int) = quantidade do produto
        precouni (float) = preço unitario do produto
        
        Retorno: Cria um novo registro(pedido no banco de dados)
          
        """
        self.pedido = pedido
        self.produto = produto
        self.qtd = qtd
        self.preco = precouni
        
        data = (self.pedido, self.produto, self.qtd, self.preco)
        
        #Estabelecemos a conexão com o banco de dados caso exista, se não ele é criado 
        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()

        #Comando SQL que será executado
        cursor.execute("""
                            INSERT INTO pedido (pedido, produto, qtd, preco) 
                            VALUES(? ,? ,? ,?)
                        """, data)
        conexao.commit()
        conexao.close()
    
    #Método para mostrar os pedidos
    def mostrar_pedidos(self):
        """
        Mostra os registros de pedidos armazenados na base de dados
        
        Retorno: Apresenta os registros de pedido.
        """
        #Estabelecemos a conexão com o banco de dados caso exista, se não ele é criado 2
        con = sqlite3.connect("estoque.db")
        cursor = con.cursor()
        cursor.fetchall()
        
        #Comando SQL que será executado
        df = pd.read_sql_query("SELECT pedido, produto, qtd,  preco FROM pedido ORDER BY pedido ASC", con)
        time.sleep(1)
        
        #Informamos ao usuário os pedidos criados
        print("")
        print("Pedidos criados:")
        print(df)
        
    #Método para mostrar os pedidos
    def mostrar_pedidos_unico(self, pedido):
        """
        Nos mostrar um pedido especifico com base no numero informado.
        
        pedido (int): Número do pedido criado pelo usuário.
        
        Retorno: Apresenta os dados de determinado pedido
        """
        #Estabelecemos a conexão com o banco de dados caso exista, se não ele é criado 2
        con = sqlite3.connect("estoque.db")
        cursor = con.cursor()
        cursor.fetchall()
        
        #Comando SQL que será executado
        df = pd.read_sql_query(f"SELECT produto, qtd, preco FROM pedido WHERE pedido = {pedido}", con)
        
    
        #Informamos ao usuário os dados do pedido
        print(df)
        
    #Método para aprovar pedido
    def aprovar_pedidos(self, pedido):
        """
        Realiza a aprovação dos pedidos
        
        pedido (int) - Numero do pedido criado pelo usuário
        
        Retorno: O Pedido informado é excluido da base de dados
        """
        self.pedido = pedido
        
        #Estabelecemos a conexão com o banco de dados caso exista, se não ele é criado 2
        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()
        
        #Comando SQL que será executado
        cursor.execute("DELETE FROM pedido WHERE pedido = ?", (self.pedido,))
        conexao.commit()
        conexao.close()