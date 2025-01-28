import time

print("")
print("Selecione o tipo de acesso:")
tipoacesso = 0
#Verificação do tipo de acesso(estoquista, usuario ou gerente de setor)
while tipoacesso not in [1,2,3,4]:
    tipoacesso = int(input(f"{'-'*65}\n1)Estoquista | 2)Usuario | 3)Gerente de setor | 4)Parar programa\n{'-'*65}\n"))
    time.sleep(1.5)
    if tipoacesso == 1:
        #Acesso como estoquista
        estoquista()
    elif tipoacesso == 2:
        #Acesso como usuario
        usuario()
    elif tipoacesso == 3:
        #Acesso como gerente
        gerente()
    elif tipoacesso == 4:
        break