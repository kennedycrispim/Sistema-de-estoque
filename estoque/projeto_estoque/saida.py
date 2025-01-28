import sqlite3, time

class Saida:
    def __init__(self, produto = "", qtd = 0, data_saida = ""):
        self.produto = produto
        self.qtd = qtd
        self.data_saida = data_saida
        self.criar_tabelas()

    def criar_tabelas(self):
        #Estabelecemos a conexão com o banco de dados caso exista, se não ela é criada
        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()
        
        #Comando SQL que será executado
        cursor.execute("""
                            CREATE TABLE IF NOT EXISTS saida(
                                id_saida INTEGER PRIMARY KEY AUTOINCREMENT,
                                produto VARCHAR,
                                qtd INTEGER,
                                data_saida DATE
                            )
                       """)
  
        conexao.commit()
        conexao.close()      

    #Método de saida
    def registrar_saida(self, produto, qtd, data_saida):
        self.produto = produto
        self.qtd = qtd
        self.data_saida = data_saida
        
        dados = (self.produto, self.qtd, self.data_saida)
        #Estabelecemos a conexão com o banco de dados caso exista, se não ele é criado 
        try: 
            conexao = sqlite3.connect("estoque.db")
            cursor = conexao.cursor()

            cursor.execute("""
                                INSERT INTO saida (produto, qtd, data_saida)
                                VALUES (?, ?, ?)
                            """, dados)
            conexao.commit()
            conexao.close()
            
            time.sleep(1.5)
            print("")
            print("Saída efetuada com sucesso")
        except sqlite3.Error as e:
            print(f"Erro ao registrar saída: {e}")  # Mensagem de erro
        finally:
            conexao.close()  
        