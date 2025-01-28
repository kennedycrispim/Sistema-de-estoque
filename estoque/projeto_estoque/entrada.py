#imports
import sqlite3, time

#Criação da classe entrada
class Entrada:
    #Definindo os atributos de entrada | Método construtor
    def __init__(self, produto = "", qtd = 0, data_entrada = "", nf = 0):
        self.produto = produto
        self.qtd = qtd
        self.data_entrada = data_entrada
        self.nf = nf
        self.criar_tabelas()
    
    #Criação das tabelas do banco       
    def criar_tabelas(self):
        """
            Realiza a criação da tabela 'entrada' no banco de dados, 
            principal base de dados que será trabalhada nese módulo
            
            Retorno: tabela 'entrada' é criada.
        """
        #Estabelecemos a conexão com o banco de dados caso exista, se não ela é criada
        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()
        
        #Comando SQL que será executado
        cursor.execute("""
                            CREATE TABLE IF NOT EXISTS entrada(
                                id_entrada INTEGER PRIMARY KEY AUTOINCREMENT,
                                produto VARCHAR,
                                qtd INTEGER,
                                data_entrada DATE,
                                nf INTEGER
                            )
                       """)
  
        conexao.commit()
        conexao.close()      
        
    #Método de entrada
    def registrar_entrada(self, produto, qtd, data_entrada, nf):
        """
        Registra uma nova entrada no sistema. Faz parte do sistema de inserção se NF  no  sistema
        
        produto (string) = nome do produto, item
        qtd (int) = quantidade do produto atualiza
        data_entrada (string) = Recebe a data em que a mercadoria está entrando no sitema 
        nf (int) = recebe o número da NF
        
        Retorno: é feito um registro dos produtos da NF no banco.
        """
        self.produto = produto
        self.qtd = qtd
        self.data_entrada = data_entrada
        self.nf = nf
        
        #Estabelecemos a conexão com o banco de dados, caso não for possível o usuário será informado
        try: 
            conexao = sqlite3.connect("estoque.db")
            cursor = conexao.cursor()

            cursor.execute("""
                                INSERT INTO entrada (produto, qtd, data_entrada, nf)
                                VALUES (?, ?, ?, ?)
                            """, (self.produto, self.qtd, self.data_entrada, self.nf))
            conexao.commit()
            conexao.close()
            
            time.sleep(1)
            print("Produto adicionado com sucesso")
        #Exibimos a mensagem caso o erro
        except sqlite3.Error as e:
            print(f"Erro ao registrar entrada: {e}")  # Mensagem de erro
        finally:
            conexao.close()  
            
    #Método para mostrar entradas existentes
    def mostrar_entradas(self):
        """
        Apresenta ao usuário todos os registros de entradas(movimentações)
        
        Retorno: é apresentados os registros de entrada armazenados no banco de dados.
        """
        #conexão ao banco
        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()
        
        #Comando SQL que será executado
        cursor.execute("SELECT * FROM entrada")
        entradas = cursor.fetchall()
        print(entradas)
    
 