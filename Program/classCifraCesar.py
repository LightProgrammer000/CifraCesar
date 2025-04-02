# Importacao
from colorama import Fore


class cifraCesar:

    # Construtor
    def __init__(self, valor=None, rot=None):

        self.valor = valor
        self.rotacional = 3 if rot is None else rot

        self.mensagem_cripto =    []
        self.mensagem_descripto = []

        self.alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                         "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


    # Objeto (string)
    def __str__(self):
        return f"{Fore.LIGHTYELLOW_EX}Cifra de Cesar{Fore.RESET}"


    # Funcao: Criptografar os dados
    def criptografar(self):

        # Variaveis de controle
        listagem_letra = list(self.valor)

        print(f"{Fore.LIGHTBLUE_EX}# Mensagem original: {self.valor}")

        # Adicionando na lista os indices
        for i in listagem_letra:
            self.mensagem_cripto.append(self.alfabeto.index(i))

        print(f"{Fore.LIGHTRED_EX}# Mensagem criptografada ROT ({self.rotacional}): ", end="")

        # Sistema de calculo
        for i in self.mensagem_cripto:

            if i >= (self.rotacional - 26):
                print(self.alfabeto[i + self.rotacional - 26], end="")

            else:
                print(self.alfabeto[i + self.rotacional], end="")

        print(f"{Fore.RESET}\n")


    # Funcao: Descriptografando os dados
    def descriptografar(self):

        # Variaveis de controle
        listagem_letra = list(self.valor)

        print(f"{Fore.LIGHTBLUE_EX}# Mensagem original: {self.valor}")

        # Adicionando na lista os indices
        for i in listagem_letra:
            self.mensagem_descripto.append(self.alfabeto.index(i))

        print(f"{Fore.LIGHTGREEN_EX}# Mensagem descriptografada ROT ({self.rotacional}): ", end="")

        # Sistema de calculo
        for i in self.mensagem_descripto:

            if i >= 2:
                print(self.alfabeto[i - self.rotacional], end="")

            else:
                print(self.alfabeto[26 + i - self.rotacional], end="")

        print(f"{Fore.RESET}\n")