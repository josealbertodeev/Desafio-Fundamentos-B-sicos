# Desafio 01 - Dominando os Fundamentos Básicos do Python

def recomendar_plano(consumo):
    if consumo <= 10:
        print('Plano Essencial Fibra - 50Mbps') 

    elif consumo <= 20:
        print('Plano Prata Fibra - 100Mbps')

    else:
        print('Plano Premium Fibra - 300Mbps')
    
consumo = float(input('Insira o consumo médio mensal de dados: '))
recomendar_plano(consumo)

