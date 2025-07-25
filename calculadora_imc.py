# Solicitar o peso e altura do usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calcular o IMC
imc = peso / (altura ** 2)

# Classificar o IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 25:
    classificacao = "Peso normal"
elif 25 <= imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

# Exibir o IMC e a classificação
print(f"Seu IMC é {imc:.2f}")
print(f"Classificação: {classificacao}")
