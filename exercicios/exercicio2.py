# Mensagem de boas-vindas
print("Olá, Bem-Vinda")

# Solicitação da nota da aluna
nota = float(input("Insira uma nota de 1 a 10: "))

# Solicitação da frequência da aluna
frequencia = int(input("Insira a frequência em %: "))

# Verificação de aprovação
if nota >= 7 and frequencia >= 75: 
    print("Aprovada, Parabéns")
else:
    print("Reprovada, Estude Mais")
