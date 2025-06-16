# Questão 1: Imprimir "Olá, mundo!" na tela
print("Olá, mundo!")

# Questão 2: Solicitar o nome do usuário e exibir uma mensagem de boas-vindas
nome = input("Digite seu nome: ")
print(f"Seja bem-vindo(a), {nome}!")

# Questão 3: Ler dois números inteiros e exibir a soma deles
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
print(f"A soma de {num1} e {num2} é {soma}")

# Questão 4: Ler um número e exibir o seu dobro, triplo e raiz quadrada
numero = float(input("Digite um número: "))
print(f"O dobro de {numero} é {numero * 2}")
print(f"O triplo de {numero} é {numero * 3}")
print(f"A raiz quadrada de {numero} é {numero ** 0.5:.2f}")

# Questão 5: Converter metros para centímetros e milímetros
metros = float(input("Digite o valor em metros: "))
print(f"{metros} metros são {metros * 100} centímetros e {metros * 1000} milímetros")

# Questão 6: Tabuada de um número
n = int(input("Digite um número para ver sua tabuada: "))
print(f"Tabuada de {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")