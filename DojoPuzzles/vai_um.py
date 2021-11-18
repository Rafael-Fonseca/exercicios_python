'''
Disponível em: https://dojopuzzles.com/problems/vai-um/

As crianças aprendem a adicionar multi-dígitos da direita para a esquerda,
um dígito por vez.
Muitas acham o "vai um", operação aonde o 1 é carregado para a posição seguinte,
um desafio significativo. Seu trabalho é dado dois números inteiros positivos,
contar o número de operações de "vai um" para adição.
Entrada: dois valores inteiros positivos.
Retorno: quantidade de "vai um" da soma.

Exemplos:
Entrada: 123 456 Retorno: 0 "vai um";
Entrada: 555 555 Retorno: 3 "vai um";
Entrada: 123 594 Retorno: 1 "vai um";

Adaptado a partir do problema "Carry" do
livro Programming Challenges - The Programming Contest Training Manual_Steven S.
Skiena, Miguel A. Revilla (Springer 2003)
'''

while True:

    num1 = ''
    num2 = ''
    while True:
        num1 = input('Insira um número inteiro positivo: ')
        num2 = input('Insira outro número inteiro positivo: ')

        try:
            int(num1)
            int(num2)
            break
        except ValueError:
            input('Insira valores válidos.\nPresione qualquer tecla para continuar..')

    num1 = list(num1)
    num2 = list(num2)
    carry = 0

    for i in range(0, min(len(num1), len(num2))):
        if int(num1[i]) + int(num2[i]) > 9:
            carry += 1

    print(f'Entrada: {"".join(num1)} {"".join(num2)} Retorno: {carry} "vai um";')
    cont = input('Pressione enter para continuar ou fim para sair: ').lower()

    if cont == 'fim':
        break
