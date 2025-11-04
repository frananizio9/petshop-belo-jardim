lista_ADM = [['g', 'g@.com', 'gutim123']]
lista = [['g', 'gg@.com', 'gutim123']]
codigo_ADM = ['123456']
lista_animais = [['Gato', 'Banho Arretado', 'O banho completo, o melhor de todos', 50.00],
                 ['Cachorro Pequeno', 'Banho Arretado', 'O banho completo, o melhor de todos', 50.00]]
lojao = [['racao gato', 'gato premio', 25.00],
         ['racao cachorro', 'cachorro premio', 35.50]]
agendamento = []
opcao = 0
compras_cliente = []
while opcao != 3:
    print('૮･ﻌ･ა MENU PRINCIPAL ≽(•⩊ •マ≼')
    print('[1]cadastro')
    print('[2]login')
    print('[3]sair')
    print('૮･ﻌ･ა -------------- ≽(•⩊ •マ≼')
    opcao = int(input('digite uma opcao: '))

    if opcao == 1:

        nome = input('digite seu nome: ')
        email = input('digite seu email: ')
        senha = input('digite sua senha: ')
        confirmar_senha = input('digite sua senha novamente: ')

        email_existente = False
        for l in lista:
            if l[1] == email:
                print('email ja exister')
                email_existente = True
                break
        if email_existente:
            continue

        if '@' in email and '.com' in email:
            print('cadastro conpleto')
        else:
            print('email nao corresponde')
        if senha == confirmar_senha:
            if len(senha) >= 8:
                print('senha responde todos requisitos')

            else:
                print('digite senha maior que 7')

        else:
            print('senhas não coincidem, tente novamente')

        if (senha == confirmar_senha) and len(senha) >= 8:
            lista.append([nome, email, senha])

    elif opcao == 2:

        email = input('digite seu email: ')
        senha = input('digite sua senha: ')
        login_sucesso = False

        for l in lista:
            if l[1] == email and l[2] == senha:
                print(f'seja bem vindo {l[0]}')
                login_sucesso = True

                opcao_shop = 0
                while opcao_shop != 6:
                    print('૮･ﻌ･ა so atedemos cachorro e gato ≽(•⩊ •マ≼')
                    print('[1]banho')
                    print('[2]loja do pet shop ')
                    print('[3]agendamento')
                    print('[4]remover agedamento')
                    print('[5]carrinho de compra')
                    print('[6]volta')
                    print('૮･ﻌ･ა -------------- ≽(•⩊ •マ≼')

                    opcao_shop = int(input('escolha uma opcao a cima: '))

                    if opcao_shop == 1:
                        print("--- Lista de Banhos e Serviços ---")
                        print(
                            f'{"--Animais--":<15} | {"--Tipo de Banho--":<20} | {"--Descrição--":<40} | {"--Valor--":<10}')

                        i = 0
                        for banho in lista_animais:
                            print(f"{i} - {banho[0]:<15} | {banho[1]:<20} | {banho[2]:<40} | R$ {banho[3]:<10}")
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



                    elif opcao_shop == 3:

                        qntd = int(input('Quantos animais você quer agendar? '))

                        for a in range(qntd):
                            agen = input('Informe tipo (gato/cachorro) e data __/__/____: ')
                            hora = input('Horário: ')
                            agendamento.append([agen, hora])

                        print('Agendamentos feitos:')
                        i = 0
                        for age in agendamento:
                            print(f"{i} --- {age}")
                            i += 1
                    elif opcao_shop == 4:
                        sn = input('voce que fala com algum atedente (s/n)').lower()
                        if sn == 's':

                            remover = int(
                                input('Digite o número do agendamento que deseja remover (ou -1 para não remover): '))
                            if remover >= 0 and remover < len(agendamento):
                                agendamento.pop(remover)
                                print('Agendamento removido com sucesso!')
                        else:
                            print('voce nao quis remover2')


                    elif opcao_shop == 2:
                        print("------- Produtos Disponíveis -------")
                        print(f'{"--Produto--":<20} | {"--Marca--":<20} | {"--Valor--":<10}')

                        i = 0
                        for valor in lojao:
                            print(f"{i} - {valor[0]:<20} | {valor[1]:<20} | R$ {float(valor[2]):<10}")
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

                    elif opcao_shop == 5:
                        if len(compras_cliente) == 0:
                            print(" Seu carrinho está vazio!")
                        else:
                            print(" Itens no seu carrinho:")
                            total = 0
                            for item in compras_cliente:
                                valor = float((item[-1]))
                                print(f"- {item[0]} | R$ {valor}")
                                total += valor
                            print(f" Total da compra: R$ {total}")

                            finalizar = input("Deseja finalizar a compra? (s/n): ").lower()
                            if finalizar == 's':
                                print("Compra finalizada com sucesso! Obrigado por comprar conosco ")
                                compras_cliente.clear()
                            else:
                                print("Compra não finalizada. Itens continuam no carrinho.")



    elif opcao == 763:
        email = input('digite seu email: ')
        senha = input('digite seu senha: ')

        login_sucesso = False
        for l in lista_ADM:
            if l[1] == email and l[2] == senha:
                print(f'seja bem vindo {l[0]}')
                login_sucesso = True

                opcao_ADM = 0
                while opcao_ADM != 9:
                    print('૮･ﻌ･ა ------ ADM ------ ≽(•⩊ •マ≼')
                    print('[1]adicionar banho e valor')
                    print('[2]remover banho e valor')
                    print('[3]ver banhos ')
                    print('[4]adicionar produtos no lojao')
                    print('[5]remover produtos do lojao')
                    print('[6]ver lojao')
                    print('[7]ver a agenda')
                    print('[8]cadastrar novo ADM')
                    print('[9]sair')
                    print('૮･ﻌ･ა -------------- ≽(•⩊ •マ≼')

                    opcao_ADM = int(input('digite uma opcao acima: '))

                    if opcao_ADM == 1:
                        animais = input('digite o animal ')
                        nome_banho = input('digite o nome do banho')
                        descricao_banho = input('digite a descricao do banho')
                        valor = float(input('digite o valor do banho'))

                        lista_animais.append([animais, nome_banho, descricao_banho, valor])


                    elif opcao_ADM == 2:
                        print('banho disponíveis:')
                        for banho in range(len(lista_animais)):
                            print(f'{banho} --- {lista_animais[banho]}')
                        remove = int(input('Digite o número da banho para remover: '))
                        lista_animais.pop(remove)

                    elif opcao_ADM == 3:
                        for banho in lista_animais:
                            print(f"{banho[0]:<25} | {banho[1]:<10} | {banho[2]:>10} | {banho[3]:<10}")
                            print("-" * 60)
                    elif opcao_ADM == 4:
                        produto = input('adiciona nome do produto')
                        marca = input('adicione sua marca')
                        valor = float(input('qual sera o valo do produtor'))
                        lojao.append([produto, marca, valor])

                    elif opcao_ADM == 5:
                        print('produtos disponíveis:')
                        for prodtu in range(len(lojao)):
                            print(f'{prodtu} --- {lojao[prodtu]}')
                        remover = int(input('Digite o número da banho para remover: '))
                        lista_animais.pop(remover)

                    elif opcao_ADM == 6:
                        for item in lojao:
                            print(f"{item[0]:<25} | {item[1]:<10} | {item[2]:>10}")
                            print("-" * 60)

                    elif opcao_ADM == 7:
                        for agenda in agendamento:
                            print(agenda)

                    elif opcao_ADM == 8:
                        nome = input('digite seu nome: ')
                        email = input('digite seu email: ')
                        senha = input('digite sua senha: ')
                        confirmar_senha = input('digite sua senha novamente: ')
                        codigo_adm = input('digite o codigo do ADM: ')

                        email_existente = False
                        for l in lista_ADM:
                            if l[1] == email:
                                print('email ja exister')
                                email_existente = True
                                break
                        if email_existente:
                            continue

                        if '@' in email and '.com' in email:
                            print('n/')
                        else:
                            print('email nao corresponde')
                        if senha == confirmar_senha:
                            if len(senha) >= 8:
                                print('senha responde todos requisitos')

                            else:
                                print('digite senha maior que 7')

                        else:
                            print('senhas não coincidem, tente novamente')

                        if (codigo_adm in codigo_ADM) and (senha == confirmar_senha) and len(senha) >= 8:
                            lista_ADM.append([nome, email, senha])

    elif opcao == 3:
        print('saiuuuuu')
        break