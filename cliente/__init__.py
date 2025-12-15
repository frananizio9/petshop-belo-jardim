from listas import lista_animais, lojao, agendamento, compras_cliente
import datetime as dt

def menu_cliente(cliente):
    opcao_shop = 0
    while opcao_shop != 7:
        print('૮･ﻌ･ა so atedemos cachorro e gato ≽(•⩊ •マ≼')
        print('[1]banho')
        print('[2]loja do pet shop ')
        print('[3]agendamento')
        print('[4]remover agedamento')
        print('[5]carrinho de compra')
        print('[6]listar atendimentos')
        print('[7]volta')
        print('૮･ﻌ･ა -------------- ≽(•⩊ •マ≼')

        opcao_shop = int(input('escolha uma opcao a cima: '))

        if opcao_shop == 1:
            lista_de_banho()

        elif opcao_shop == 2:
            loja()

        elif opcao_shop == 3:
            agendar(cliente)

        elif opcao_shop == 4:
            remover_agendamento()

        elif opcao_shop == 5:
            carrinho()

        elif opcao_shop == 6:
            pegar_atendimentos(cliente)



def lista_de_banho():
    print("--- Lista de Banhos e Serviços ---")
    print(
        f'{"--Animais--":<15} | {"--Tipo de Banho--":<20} | {"--Descrição--":<40} | {"--Valor--":<10}')

    i = 1
    for banho in lista_animais:
        print(f"{banho['id']} - {banho['animal']:<15} | {banho['nome']:<20} | {banho['descricao']:<40} | R$ {banho['valor']:<10}")
        i += 1
    print("-" * 90)

    opc = input("Deseja comprar algum banho? (s/n): ").lower()
    if opc == 's':
        bh = int(input("Digite o número do banho que deseja: "))
        if bh >= 0 and bh < len(lista_animais):
            compras_cliente.append(lista_animais[bh])
            print(" Banho adicionado à sua lista de compras!")
        else:
            print("Número inválido.")

def loja ():
    print("------- Produtos Disponíveis -------")
    print(f'{"--Produto--":<20} | {"--Marca--":<20} | {"--Valor--":<10}')

    i = 1
    for valor in lojao:
        print(f"{valor['id']} - {valor['nome']:<20} | {valor['marca']:<20} | R$ {float(valor['valor']):<10}")
        i += 1
    print("-" * 60)

    opc = input("Deseja comprar algum produto? (s/n): ").lower()
    if opc == 's':
        indice = int(input("Digite o número do produto que deseja: "))
        if indice >= 0 and indice < len(lojao):
            compras_cliente.append(lojao[indice])
            print(" Produto adicionado à sua lista de compras!")
        else:
            print("Número inválido.")

def pegar_atendimentos(cliente):
    print(40*'=')
    for agen in agendamento:
        if agen['cliente'] == cliente:
            print(f'{agen['id']} - tipo: {agen['tipo']}, data: {agen['data']}, hora: {agen['hora']}, cliente: {agen['cliente']}')
    print(40 * '=')

def agendar(cliente):
    qntd = int(input('Quantos animais você quer agendar? '))

    for a in range(qntd):
        tipo = input('Informe tipo (gato/cachorro): ')
        data = input('data YYYY-MM-DD: ')
        hora = input('Horário: ')
        agendamento.append({'tipo': tipo, 'data': data, 'hora': hora, 'cliente': cliente})

    print('Agendamentos feitos:')
    i = 1
    for age in agendamento:
        print(f"{i} --- {age}")
        i += 1

def remover_agendamento():
    sn = input('voce que fala com algum atedente (s/n)').lower()
    if sn == 's':

        remover = int(
            input('Digite o número do agendamento que deseja remover (ou -1 para não remover): '))
        if remover >= 0 and remover < len(agendamento):
            agendamento.pop(remover)
            print('Agendamento removido com sucesso!')
    else:
        print('voce nao quis remover2')

def carrinho():
    if len(compras_cliente) == 0:
        print(" Seu carrinho está vazio!")
    else:
        print(" Itens no seu carrinho:")
        total = 0
        for item in compras_cliente:
            valor = float(item['valor'])
            print(f"- {item['nome']} | R$ {valor}")
            total += valor
        print(f" Total da compra: R$ {total}")

        finalizar = input("Deseja finalizar a compra? (s/n): ").lower()
        if finalizar == 's':
            print("Compra finalizada com sucesso! Obrigado por comprar conosco ")
            compras_cliente.clear()
        else:
            print("Compra não finalizada. Itens continuam no carrinho.")
