mensagem_cripto = []
alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

ROT = 13
letra = "rkrzcybmmmmm"
listagem_letra = list(letra)

# Achar indice
for i in listagem_letra:
    mensagem_cripto.append(alfabeto.index(i))

try:
    for i in mensagem_cripto:

        if i >= 2:
            print(alfabeto[i - ROT])

        else:
            print(alfabeto[26 + i - ROT])

except Exception as e:
    print(e)