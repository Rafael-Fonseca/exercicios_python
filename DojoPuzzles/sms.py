"""
Disponível em: https://dojopuzzles.com/problems/escrevendo-no-celular/

Um dos serviços mais utilizados pelos usuários de aparelhos celulares são os
SMS (Short Message Service), que permite o envio de mensagens curtas
(até 255 caracteres em redes GSM e 160 caracteres em redes CDMA).

Para digitar uma mensagem em um aparelho que não possui um teclado QWERTY
embutido é necessário fazer algumas combinações das 10 teclas numéricas do
aparelho para conseguir digitar.
Cada número é associado a um conjunto de letras como a seguir:

Letras  ->  Número
ABC    ->  2
DEF    ->  3
GHI    ->  4
JKL    ->  5
MNO    ->  6
PQRS   ->  7
TUV    ->  8
WXYZ   ->  9
Espaço ->  0

Desenvolva um programa que, dada uma mensagem de texto limitada a 255
caracteres, retorne a seqüência de números que precisa ser digitada.

Uma pausa, para ser possível obter duas letras referenciadas pelo mesmo número,
deve ser indicada como _.

Por exemplo, para digitar "SEMPRE ACESSO O DOJOPUZZLES", você precisa digitar:

77773367_7773302_222337777_777766606660366656667889999_9999555337777

Este problema foi baseado em uma sugestão de Denis Costa
"""


def define_alpha(dict, start, repeat, value):
    dict.update({chr(repeat+start): repeat*value})


translate = {}
for i in range(1, 4):
    define_alpha(translate, 64, i, '2')
    define_alpha(translate, 67, i, '3')
    define_alpha(translate, 70, i, '4')
    define_alpha(translate, 73, i, '5')
    define_alpha(translate, 76, i, '6')
    define_alpha(translate, 79, i, '7')
    define_alpha(translate, 83, i, '8')
    define_alpha(translate, 86, i, '9')

translate.update({'S': '7777'})
translate.update({'Z': '9999'})
translate.update({' ': '0'})

sentence = list(input('Insira um sms com no máximo 255 caracteres:\n').upper())
if len(sentence) > 254:
    print('O sms tem mais caracteres do que o permitido.')

encripted = ''
for index in range(0, len(sentence)):
    try:
        if translate[sentence[index]][0] in translate[sentence[index + 1]]:
            encripted += translate[sentence[index]] + '_'
        else:
            encripted += translate[sentence[index]]

    except IndexError:
        pass

encripted += translate[sentence[-1]]
print(encripted)
