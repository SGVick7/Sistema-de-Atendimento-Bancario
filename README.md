# Sistema-de-Atendimento-Bancario
Sistema de fila para atendimento bancário

Registro de testes
1. Teste
Objetivo:
Verificar se o cliente com maior tempo de espera é atendido primeiro.
Entrada:
G
P
A
A
A
A
A
A
A
A
A
C
S
Saída:
Cliente chamado:
Senha 2 | Tipo P | Espera 9
2. Teste
Objetivo:
Verificar se em caso de mesmo tempo de espera entre o cliente “P” e ”C”, o cliente
preferencial será atendido primeiro.
Entrada:
G
P
A
A
A
A
A
A
A
A
C
S
Saída:
Cliente chamado:
Senha 2 | Tipo P | Espera 8
3. Teste
Objetivo:
Verificar se clientes são removidos corretamente após atingirem o tempo de espera
limite.
Entrada:
G
A
A
A
A
A
A
A
A
A
A
S
Saída:
Cliente desistiu:
Senha 1 | Tipo C | Espera 10
4. Teste
Objetivo:
Verificar se o sistema calcula corretamente as estatísticas.
Entrada:
G
P
G
A
A
C
A
A
A
A
A
A
A
A
E
S
Saída:
Estatísticas:
Total de senhas geradas: 3
Total de clientes atendidos: 1
Total de clientes que desistiram: 2
Total de clientes aguardando na fila: 0
Tempo médio de espera dos clientes: 2.00
5. Teste
Objetivo:
Verificar se o sistema inválida entradas diferente das opções do “Menu”
Entrada:
x
Saída:
Opção inválida!
