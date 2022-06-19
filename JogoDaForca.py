from random import choice

def palavra_secreta():
    # Importa o arquivo na extensão "txt" com as palavras secretas para o game iniciar
    with open("Palavras.txt","r",encoding="utf-8") as arquivo:
        P = []
        for Palavra in arquivo:
            P.append(Palavra)
    Palavras = choice(P)
    Letras = []
    # Aqui será gerado as palavras separadamentes para iniciar 
    for letra in Palavras:
        Letras.append(letra)
    Letras.pop()
    return Letras

# Aqui contém o desenho da forca para gera o desenho indicando a forca 
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

# Nessa função será retornado quando o usuário acerta a palavra chave do programa 
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

# Nessa função será retornado quando o usuário erra a palavra chave do programa 
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


# Nessa função é o ínicio do projeto que vai acontecer o jogo com a interaçaõ do usuário
def jogar(Palavra):
    Tentativas = []
    Chances = 0
    Palavra_misteriosa = ["_" for linha in range(1,len(Palavra)+1)]
    print("="*30)
    print("BEM VINDO AO JOGO DA FORCA")
    print("="*30)
    while "_" in Palavra_misteriosa:
        print("-"*45)
        L = str(input("DIGITE UMA LETRA PARA ADIVINHA A PALAVRA: ")).lower()
        if L in Tentativas:
            Chances = Chances + 1
            print("VOCÊ JÁ USOU ESSA PALAVRA")
            desenha_forca(Chances)
            print(f"VOCÊ TEM {7-Chances} TENTATIVAS")
            if Chances == 7:
                imprime_mensagem_perdedor(Palavra)
                break
        elif L in Palavra:
            Tentativas.append(L)
            for n in Palavra:
                i = [K for K, Valor in enumerate(Palavra) if Valor == L ]
                if L == n: 
                    for numero in i:
                        Palavra_misteriosa[numero] = L
            print(Palavra_misteriosa)
            print(f'FALTA {Palavra_misteriosa.count("_")} LETRAS PARA ACERTA AINDA')
        else:
            Chances = Chances + 1   
            desenha_forca(Chances)
            Tentativas.append(L)
            print(f"A PALAVRA {L.upper()} NÃO SE ENCONTRA NA PALAVRA SECRETA") 
            print()
            if Chances == 7:
                imprime_mensagem_perdedor(Palavra)
                break
    if "_" not in Palavra_misteriosa:
        imprime_mensagem_vencedor()

jogar(palavra_secreta())