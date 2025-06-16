nome = "João"
idade = 30
print(f"Meu nome é {nome} e eu tenho {idade} anos.")

# 2. Troca de valores entre variáveis a e b
a = 5
b = 10
a, b = b, a
print("Valores trocados:")
print("a =", a)
print("b =", b)

# 3. Constante PI e cálculo da área de um círculo
PI = 3.14159
raio = 4
area = PI * raio ** 2
print(f"A área de um círculo de raio {raio} é {area}")

# 4. Três variáveis de tipos diferentes e exibição de seus tipos
inteiro = 7
flutuante = 3.14
texto = "Python"
print("Tipo da variável inteiro:", type(inteiro))
print("Tipo da variável flutuante:", type(flutuante))
print("Tipo da variável texto:", type(texto))

# 5. Avaliação de expressão matemática
resultado = 10 + 5 * 2 - 3 ** 2
# Ordem de precedência:
# Potência (**), Multiplicação (*), Adição (+), Subtração (-)
# 3 ** 2 = 9
# 5 * 2 = 10
# 10 + 10 - 9 = 11
print("Resultado da expressão 10 + 5 * 2 - 3 ** 2 =", resultado)

# 6. Conversão de Celsius para Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura de {celsius}°C em Fahrenheit é {fahrenheit}°F")

# 7. Verificação se duas variáveis são diferentes e maiores que zero
x = 7
y = 9
if x != y and x > 0 and y > 0:
    print("x e y são diferentes e maiores que zero")
else:
    print("Condição não satisfeita")

# 8. Avaliação de expressão lógica
resultado_logico = (5 > 3) and (2 < 1)
# (5 > 3) é True
# (2 < 1) é False
# True and False = False
print("Resultado da expressão (5 > 3) and (2 < 1):", resultado_logico)

# 9. Conversão de string para float
altura_str = "1.75"
altura_float = float(altura_str)
print(f"A altura convertida é: {altura_float}")

# 10. Conjuntos de alunos
alunos_python = {"Ana", "Carlos", "João"}
alunos_java = {"Carlos", "Joana", "Marcos"}

# Alunos que fazem as duas linguagens
print("Alunos que fazem as duas linguagens:", alunos_python & alunos_java)

# Alunos que fazem só Python
print("Alunos que fazem só Python:", alunos_python - alunos_java)

# Todos os alunos (sem repetição)
print("Todos os alunos:", alunos_python | alunos_java)


