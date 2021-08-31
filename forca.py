print("***BEM VINDO AO JOGO DA FORCA!***")

def bonequin(erros):
    
    
    print("  __   ")
    print(" |/  |    ")

    if(erros == 1):
        print(" |x")
        print(" |")
        print(" |")

    if(erros == 2):
        print(" |o")
        print(" |")
        print(" |")

    if(erros == 3):
        print(" |o")
        print(" |@")
        print(" |")

    if(erros == 4):
        print(" | o")
        print(" |~@")
        print(" |")

    if(erros == 5):
        print(" | o")
        print(" |~@~")
        print(" |")

    if(erros == 6):
        print(" | o")
        print(" |~@~")
        print(" |]")
        
    if(erros == 7):
        print(" |   o")
        print(" |  ~@~")
        print(" |  ] [")

    print("_|___         ")
    print()

def shadowpalavra():
    
   palavra = (input("Digite a palavra secreta!")).upper()
   print("A palavra possui", len(palavra),"letras")
   print('_ ' * len(palavra))
   
   acertos = 0
   erros = 0
   letras_acertadas = ''
   letras_erradas = ''
    
   while acertos != len(palavra) and erros !=6:
        
    print("voce ja acertou " +letras_acertadas)
    print("voce ja errou " +letras_erradas)
        
    letra = input("Digite a letra: ").upper()
        
    if letra in palavra:
        print("Voce acertou a letra")
        letras_acertadas += letra
        acertos += 1
    else:
        print("Voce errou a letra")
        letras_erradas += letra
        erros += 1
        
    if(erros == 1):
        bonequin(6)
        print("Perdi minha perna!")
    elif(erros == 2):
        bonequin(5)
        print("Estou sem pernas!")
    elif(erros == 3):
        bonequin(4)
        print("Ai meu bracinho de macarrão!!")
    elif(erros == 4):
        bonequin(3)
        print("=(")
    elif(erros == 5):
        bonequin(2)
        print("barriguinha sumiu rsrs!")
    elif(erros == 6):
        bonequin(1)
        print("RIP |press f para jogar dnv")
    else:
        print("")

                
shadowpalavra()
    
    
    

    






