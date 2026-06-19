fila = []
dados = ""
senha = 0
total_atendidos = 0
desistentes = 0
soma = 0
while True:
    print("Menu")
    print("G - Gerar senha comum")
    print("P - Gerar senha preferencial")
    print("C - Chamar próximo cliente")
    print("A - Avançar tempo")
    print("F - Exibir fila")
    print("E - Exibir estatísticas")
    print("S - Sair")
    dados = input("Escolha uma opção: ").upper()
    # Condições
    if dados == "G":
        senha += 1
        cliente = [senha, 'C', 0]
        fila.append(cliente)
        print(f'Senha {senha} gerada para cliente comum.')

    elif dados == "P":
        senha += 1
        cliente = [senha, 'P', 0]
        fila.append(cliente)
        print(f'Senha {senha} gerada para cliente preferencial.')

    elif dados == "C":
        if len(fila) == 0:
            print('Não há clientes aguardando.')
        else:
            # 1. Descobrir o maior tempo manualmente
            maior_tempo = fila[0][2]
            for cliente in fila:
                if cliente[2] > maior_tempo:
                    maior_tempo = cliente[2]
            cliente_chamado = None
            # 2. Procurar preferencial com maior tempo
            for cliente in fila:
                if cliente[2] == maior_tempo and cliente[1] == 'P':
                    cliente_chamado = cliente
                    break
            # 3. Se não tiver preferencial, pega qualquer com maior tempo
            if cliente_chamado == None:
                for cliente in fila:
                    if cliente[2] == maior_tempo:
                        cliente_chamado = cliente
                        break
            # 4. Chamar cliente
            print('Cliente chamado:')
            print(f'Senha {cliente_chamado[0]} | Tipo {cliente_chamado[1]} | Espera {cliente_chamado[2]}')
            fila.remove(cliente_chamado)
            total_atendidos += 1
            soma += cliente_chamado[2]
    elif dados == "A":
        i = 0
        while i < len(fila):
            fila[i][2] += 1
            if fila[i][2] >= 10:
                print('Cliente desistiu:')
                print(f'Senha {fila[i][0]} | Tipo {fila[i][1]} | Espera {fila[i][2]}')
                fila.pop(i)
                desistentes += 1
            else:
                i += 1

    elif dados == "F":
        print("Fila atual:")
        if len(fila) == 0:
            print("Fila vazia")
        else:
            for cliente in fila:
                print(f'Senha {cliente[0]} | Tipo {cliente[1]} | Espera {cliente[2]}')

    elif dados == "E":
        print('Estatísticas:')
        print(f'Total de senhas geradas: {senha}')
        print(f'Total de clientes atendidos: {total_atendidos}')
        print(f'Total de clientes que desistiram: {desistentes}')
        print(f'Total de clientes aguardando na fila: {len(fila)}')
        if total_atendidos > 0:
            media = soma/total_atendidos
            print(f'Tempo médio de espera dos clientes: {media:.2f}')
        else:
            print('Não é possível calcular o tempo médio de espera.')
    
    elif dados == "S":
        print('Encerrando sistema...')
        break
    
    else:
        print('Opção inválida!')