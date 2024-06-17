while True:
    nota = int(input("Insira uma nota de 1 a 10"))
    if 1 <= nota <= 10:
        if nota >=7:
            print("Aprovada")
        else:
            print("Reprovada")
        break
    else:
        print("Nota Invalida, digite uma nota entre 1 e 10")
        