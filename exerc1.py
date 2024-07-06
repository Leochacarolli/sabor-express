# 1 - Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Leonardo', 'Thais', 'Pedro', 'Antonio', 'Levi']
anos = [2000, 2024]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

for numero in numeros:
    print(numero)

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

soma = 0

for numero in numeros:
    if numero % 2 != 0:
        soma += numero

print(f'A soma dos números ímpares de 1 a 10 é: {soma}')


# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

for numero in range(len(numeros), 0, -1):
    print(numero)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

numero = int(input('Digite um número: '))

for i in range(1,11):
    produto = numero * i
    print(f'{numero} X {i} = {produto}')

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

soma = 0

try:
    for numero in numeros:
        soma += numero
except TypeError:
    print("Erro: Todos os elementos da lista devem ser números.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

print("A soma dos elementos da lista é:", soma)

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

soma = 0

for numero in numeros:
    soma += numero

try:
    media = soma / len(numeros)
    print("A média dos elementos da lista é:", media)
except ZeroDivisionError:
    print("Erro: Não é possível calcular a média de uma lista vazia.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")