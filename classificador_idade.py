# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Classificação da idade
if 0 <= idade <= 12:
    print("Você é uma Criança.")
elif 13 <= idade <= 17:
    print("Você é um Adolescente.")
elif 18 <= idade <= 59:
    print("Você é um Adulto.")
else:
    print("Você é um Idoso.")
