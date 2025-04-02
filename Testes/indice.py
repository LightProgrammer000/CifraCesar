mensagem_cripto = []
alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

letra = "olaz"
listagem_letra = list(letra)

# Achar indice
for i in range(len(listagem_letra)):

    for j in range(len(alfabeto)):

        if listagem_letra[i] == alfabeto[j]:
            mensagem_cripto.append(j)

print(mensagem_cripto)