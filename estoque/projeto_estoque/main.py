#imports
from produto import Produto
from entrada import Entrada
from saida import Saida
from relatório import Relatorio
from datetime import datetime
from pedido import Pedido
import time  

#Declaração das classes
produto = Produto()
entrada = Entrada()
relatorio = Relatorio()
pedido = Pedido()
saida = Saida()

#Códigos Ansi
reset = "\033[0m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"

#menu
def menu():
    time.sleep(1)
    print("")
    print("Selecione o tipo de acesso:")
    tipoacesso = 0
    #Verificação do tipo de acesso(estoquista, usuario ou gerente de setor)
    while tipoacesso not in [1,2,3,4]:
        try:
            tipoacesso = int(input(f"{'-'*65}\n1)Estoquista | 2)Usuario | 3)Gerente de setor | 4)Parar programa\n{'-'*65}\n"))
            time.sleep(1.5)
            if tipoacesso == 1:
                estoquista()
            elif tipoacesso == 2:
                usuario()
            elif tipoacesso == 3:
                gerente()
            elif tipoacesso == 4:
                break
        except ValueError:
            print("Valor inválido!")
        
#Estoquista
def estoquista():
    print("")
    print(f"Bem vindo {magenta}Estoquista!{reset}")
    acao = 0
    while acao != 7:
        print("")
        acao = int(input(f"O que deseja fazer:\n{'-'*90}\n1)mostrar produtos | 2)adicionar novo produto | 3)Atualizar produto | 4)Cadastrar nova NF\n5)Registrar saída de mercadoria | 6)Localizar produto | 7)Sair\n{'-'*90}\n"))
        
        #Mostrar os produtos cadastrados
        if acao == 1:  
            print("")
            print("Segue lista de produtos Cadastrados:")
            
            #Método
            produto.mostrar_produtos()
        
        #Adicionar um novo produto ao banco
        elif acao == 2:
            print("")
            nome = input("nome produto: ")
            categoria = input("categoria produto: ")
            qtd = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            localizacao = input("localização: ")
            
            #Armazena os valores em lower case
            nome = str.lower(nome)
            categoria = str.lower(categoria)
            localizacao = str.lower(localizacao)
            
            #Chamamos o método para cadastro
            produto.cadastro_produtos(nome, categoria, qtd, preco, localizacao)    
        
        #Atualiza produto
        elif acao == 3:
            produtoAtualiza = input("Id do produto: ")
            quantidade = int(input("Quantidade: "))
            try:
                produto.atualizar_produtos(produtoAtualiza, quantidade)
                time.sleep(1)
                print("Quantidade atualizada com sucesso!")
            except ValueError:
                print("erro ao adicionar")
                
        #Cadastro de NF (movimento)
        elif acao == 4: 
            print("\nCadastro de Nota Fiscal")
            print("verifique se todos os produtos na NF possuem cadastro antes de realizar a entrada!")
            verificador = input("Todos os produtos se encontram cadastrados? (sim | nao): ")
            
            #Verifica se todos os produtos possuem cadastro
            if verificador == "sim":
                nf = int(input("Digite o número da nota fiscal: "))
                data = input("Digite a data (formato YYYY-MM-DD): ")
                
                #Loop que permite adicionar novos produtos(nova linha na nota fiscal)
                while verificador.lower() == "sim":  # Converte para minúsculas para comparação
                    nota = nf
                    datanf = datetime.strptime(data,'%Y-%m-%d')
                    datanf = datanf.date()
                    novoproduto = input("Produto: ")
                    quantidade = int(input("Quantidade: "))

                    # Método: registro de entrada
                    entrada.registrar_entrada(novoproduto, quantidade, datanf, nota)

                    #Verifica se haverá necessidade de adicionar nova linha
                    print("")
                    verificador = input("Adicionar nova linha? (sim | nao): ")
                    print("")
                    verificador = verificador.lower()  # Converte a entrada para minúsculas
                    produto.atualizar_produtos_movimento(novoproduto, quantidade)
                time.sleep(1)
                print("Estrada de NF finalizada com sucesso,\nSegue produtos adicionados:\n")
                relatorio.entrada_nf(nf)
                
        #Registro de saída de mercadoria
        elif acao == 5:
            print("")
            produto_saida = input("Produto: ") 
            qtd = int(input("Quantidade: "))
            data_saida = input("Digite a data (formato YYYY-MM-DD): ")
            
            #Chamamos o método para registrar as saídas
            saida.registrar_saida(produto_saida, qtd, data_saida)
                    
        #Localiza Produto no estoque
        elif acao == 6:
            print("")
            id_produto = int(input("Localizador de produtos\nDigite o id do produto: "))
            
            time.sleep(1)
            produto.localiza_produtos(id_produto)
            
        #retorna para o menu principal  
        elif acao == 7: 
            menu()                    

#Usuário
def usuario():
    print("")
    print(f"Bem vindo {blue}Usuario{reset}")
    acao = 0
    while acao != 3:
        print("")
        acao = int(input(f"o que deseja fazer:\n{'-'*77}\n1)Relatórios | 2)solicitação de compra | 3)Localizador de produtos | 4)Sair\n{'-'*77}\n"))
        
        #Acessa o menu de relatórios
        if acao == 1:
            time.sleep(1)
            print("")
            tiporelatório = int(input(f"Selecione o tipo de relatório:\n{'-'*127}\n1)Top 10 maiores estoque | 2)Top 5 menores estoque | 3)Venda por período(Semanal) | 4)Entradas por produto | 5)Entrada por NF\n{'-'*127}\n"))
            
            #Relatórios de itens com maior estoque
            if tiporelatório == 1:
                #Chamamos o metódo para gerar o relatório
                relatorio.maior_estoque()
            
            #Relatórios de itens com menor estoque
            elif tiporelatório == 2:
                relatorio.menor_estoque()
            
            #Relatório Semanal(período)
            elif tiporelatório == 3:
                print("")
                data_inicial = input("Digite a data inicial (formato YYYY-MM-DD): ")
                data_final = input("Digite a data final (formato YYYY-MM-DD): ")
                
                #Chamamos o método para gerar o relatório
                relatorio.movimentacao_periodo(data_inicial, data_final)
            
            #Relatório de todas as entradas de um tipo de produto
            elif tiporelatório == 4:
                print("")
                produto = input("Produto: ")
                relatorio.entradas_tipo(produto)              
            
            #Relatório de itens por NF
            elif tiporelatório == 5:
                print("")
                nf = input("Nº NF: ")
                time.sleep(1)
                
                print("")
                print(f"Seguem dados da nf {nf}:")
                relatorio.entrada_nf(nf)
        
        #Permite criar nova solicitação de compra
        elif acao == 2:
            
            #Setamos a classe Pedido
            pedido = Pedido()
            
            time.sleep(1)
            print("")
            print("solicitação de compra")
            novopedido = int(input("Digite um novo número de pedido: "))
            
            #variavel verificadora - se será necessário adicionar novo produto
            verificador = "sim"
            
            while verificador == "sim":
                produto = input("Produto: ")
                qtd = int(input("Quantidade: "))
                precouni = float(input("Digite o preço unitário: "))
                
                pedido.criar_pedidos(novopedido, produto, qtd, precouni)
                
                print("")
                verificador = input("Deseja adicionar um novo produto: sim | nao\n")    
                print("")
                
            time.sleep(1)
            print(f"Pedido {blue}{novopedido}{reset} criado com sucesso!")
            
        #Localiza Produto no estoque
        elif acao == 3:
            print("")
            id_produto = int(input("Localizador de produtos\nDigite o id do produto: "))
            
            time.sleep(1)
            produto.localiza_produtos(id_produto)
        
        #retorna para o menu principal
        elif acao == 4:
            menu()
     
#Gerente       
def gerente():
    print("")
    print(f"Bem vindo {yellow}Gerente{reset}")
    
    acao = 0
    
    while acao != 2:
        try:
            print("")
            acao = int(input(f"o que deseja fazer:\n{'-'*20}\n1)Pedidos | 2)Sair\n{'-'*20}\n"))
            
            #Acessa o menu de pedidos
            if acao == 1:
                time.sleep(1)
                contador = 0
                print("")
                contador = int(input(f"Opções:\n{'-'*30}\n 1)Ver Pedidos | 2)Autorizar\n{'-'*30}\n"))
                
                #Verifica os pedidos criados pelo usuário
                if contador ==1:
                    time.sleep(0.8)
                    pedido.mostrar_pedidos()
                
                #Permite autorizar ou rejeitar os pedidos
                elif contador == 2:
                    
                    time.sleep(0.5)
                    print("")    
                    print("Autorizações de compra:")
                    numpedido = int(input("Digite o número do pedido: "))

                    
                    print("Pedidos")
                    pedido.mostrar_pedidos_unico(numpedido)
                    print("")
                    decisao = input("Deseja aprova-lo: sim | nao\nPara cancelar a ação precione 0\n")
                    
                    #Aceita o pedido
                    if decisao == 'sim':
                        time.sleep(1.5)
                        print("")
                        print("O pedido foi aprovado")
                        pedido.aprovar_pedidos(numpedido)
                    
                    #Rejeita o pedido
                    elif decisao == 'nao':
                        time.sleep(1.5)
                        print("")
                        print("O pedido foi excluido")
                    
                    #Cancela a ação
                    elif decisao == '0':
                        time.sleep(1.5)
                        print("Ação cancelada")
                        continue
              
            #retorna para o menu principal
            elif acao == 2:
                menu()     

        except ValueError:
            print("Digite um valor válido!")
            print("")

#Inicio do programa
print("")
print(f"{green}Bem Vindo ao sistema de estoque{reset}\n")
menu()