"""
# Programa: Cifra de Cesar
# Testes: https://site112.com/cifra-de-cesar-codificar-descodificar
"""

# Importando classe
from classCifraCesar import cifraCesar


def main():

    cesar_1 = cifraCesar("exemploz")
    cesar_2 = cifraCesar("exemploz", 13)
    cesar_3 = cifraCesar("exemploz", 16)

    print("Exemplo 1")
    cesar_1.criptografar()
    cesar_1.descriptografar()

    print("Exemplo 2")
    cesar_2.criptografar()
    cesar_2.descriptografar()

    print("Exemplo 3")
    cesar_3.criptografar()
    cesar_3.descriptografar()


if __name__ == '__main__':
    main()