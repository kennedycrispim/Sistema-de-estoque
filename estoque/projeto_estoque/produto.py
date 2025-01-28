#imports
import sqlite3
import time


#Ciação da classe produto
class Produto:
    #Definindo os atributos de produto | Método construtor
    def __init__(self, produto = "", categoria = "", qtd = 0, preco = 0, localizacao= ""):
        self.nome_produto = produto
        self.categoria = categoria
        self.qtd = qtd
        self.preco = preco
        self.localizacao = localizacao
        self.criar_tabelas()
    
    #Criação das tabelas do banco
    def criar_tabelas(self):
        #Estabelecemos a conexão com o banco de dados caso exista, se não ela é criada
        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()
        
        #Comando SQL que será executado
        cursor.execute("""
                            CREATE TABLE IF NOT EXISTS estoque (
                                id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
                                produto VARCHAR,
                                categoria VARCHAR,
                                qtd INTEGER,
                                preco FLOAT,
                                localizacao VARCHAR)
                       """)
        
    #Método de cadastro de produto
    def cadastro_produtos(self, produto, categoria, qtd, preco, localizacao):
        """
        Realiza o cadastro de um novo produto no sistema
        
        nome_produto (string) = nome do produto, item
        categoria (string) = tipo de categoria
        qtd (int) = quantidade do produto atualiza
        preco (float) = preço, valor do produto
        localização (string) = local onde se encontra o produto
        
        Retorno: É cadastrado um novo produto ao banco, 
        informando ao final para o usuário que o cadastro foi realizado.
        """
        self.nome_produto = produto
        self.categoria = categoria
        self.qtd = qtd
        self.preco = preco
        self.localizacao = localizacao
        
        produto = (self.nome_produto, self.categoria, self.qtd, self.preco, self.localizacao)
                
        #Estabelecemos a conexão com o banco de dados caso exista, se não ele é criado 
        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()
        
        #Código SQL que será executado
        cursor.execute("""
                            INSERT INTO estoque (produto, categoria, qtd, preco, localizacao)
                            VALUES(?, ?, ?, ?, ?)
                       """, produto)
        conexao.commit()
        conexao.close()
        
        time.sleep(1.5)
        
        #Informamos ao usuário que o produto foi atualizado
        print("")
        print("Produto adicionado com Sucesso")
      
    #Método para atualizar os produtos    
    def atualizar_produtos(self, nome_produto, nova_quantidade):
        """
        Realiza uma atualização da quantidade de determinado produto no estoque
        
        nome_produto (string) = nome do produto, item
        nova_quantidade (int) = quantidade do produto atualiza
        
        Retorno: Atualiza a quantidade de um produto de acordo com o valor infomado pelo usuário,
        ao final o do método o usuário recebe a mensagem 'Produto atualizado com sucesso!'
        informando a atualização.
        """
        
        #Estabelecemos a conexão com o banco de dados caso exista, se não ela é criada
        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()    
        
        #Código SQL que será executado
        cursor.execute("UPDATE estoque SET qtd = ? WHERE id_produto = ?", (nova_quantidade, nome_produto))
        conexao.commit()
        conexao.close()
        
        #Informamos ao usuário que o produto foi atualizado
        print("Produto atualizado com sucesso!")
        
    #Método para atualizar os produtos da entrada    
    def atualizar_produtos_movimento(self, nome_produto, nova_quantidade):
        """
        Realiza uma atualização da quantidade de determinado produto no estoque
        
        nome_produto (string) = nome do produto, item
        nova_quantidade (int) = quantidade do produto atualiza
        
        Retorno: Atualiza a quantidade de um produto de acordo com o valor infomado pelo usuário,
        ao final o do método o usuário recebe a mensagem 'Produto atualizado com sucesso!'
        informando a atualização.
        """
        
        #Estabelecemos a conexão com o banco de dados caso exista, se não ela é criada
        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()    
        
        #Código SQL que será executado
        cursor.execute("UPDATE estoque SET qtd = qtd + ? WHERE produto = ?", (nova_quantidade, nome_produto))
        conexao.commit()
        conexao.close()
        
        #Informamos ao usuário que o produto foi atualizado
        print("Produto atualizado com sucesso!")
    
    #Método para mostrar os produtos
    def mostrar_produtos(self):
        #conexão ao banco
        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()
        
        cursor.execute("SELECT * FROM estoque")
        produtos = cursor.fetchall()
        for produto in produtos:
            time.sleep(1)
            print(produto)
    
    #Método para localizar os produtos
    def localiza_produtos(self, id_produto):
        """
        Realiza uma busca no banco de dados da localização de um produto por meio do id.
        
        id_produto (int) = id do produto, item
        
        Retorno: A localização do produto no estoque
        """
        
        #Estabelecemos a conexão com o banco de dados caso exista, se não ela é criada
        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()
        
        #Código SQL que será executado
        cursor.execute("SELECT localizacao FROM estoque WHERE id_produto = ?", (id_produto,))
        localizacao = cursor.fetchone()
        
        #Informamos ao usuário a localização do produto no estoque
        print(f"O produto está localizado no: {localizacao[0]}")

        
    
        
    