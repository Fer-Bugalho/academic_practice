#Exercício 1: Cálculo de Área de um Círculo
#Escreva um programa que calcula a área de um círculo. O usuário deve fornecer o raio e o programa deve retornar a área.

import math

def area_circulo(raio):

    return math.pi * raio ** 2

raio = float(input("Digite o raio do círculo: "))

print("Área do círculo:", area_circulo(raio))

#Exercício 2: Conversão de Temperatura
#Crie uma função que converte a temperatura de Celsius para Fahrenheit e vice-versa. O usuário deve informar a temperatura e a escala de origem.

def celsius_para_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5 / 9

temp = float(input('Digite a temperatura: '))

escala = input('Digite a escala (C para celsius, F para fahrenheit):')

if escala.upper() == 'C':
    print("Temperatura em Fahrenheit:", celsius_para_fahrenheit(temp))
else:
    print("Temperatura em Celsius:", fahrenheit_para_celsius(temp))


#Exercício 3: Resolver uma Equação Linear
#Faça um programa que resolve uma equação linear do tipo ax + b = 0. Os valores de a e b são fornecidos pelo usuário.

def resolve_linear (a,b):

    if a == 0:
        return "Sem solução" if b != 0 else "Soluções infinitas!"
    
    return - b / a

a = float(input('Digite o valor de a: '))

b = float(input('Digite o valor de b: '))

print("Solução da equação:", resolve_linear(a,b))

#Exercício 4: Cálculo de Média Aritmética
#Escreva um programa que calcula a média aritmética de uma lista de números fornecida pelo usuário.

def media_aritmetica(numeros):

    return sum(numeros) / len(numeros)

numeros = [float(n) for n in input("Digite a lista de números separados por espaço: ").split()]

print("Média aritmética",media_aritmetica(numeros))

#Exercício 5: Determinar as Raízes de uma Equação Quadrática
#Crie um programa que encontra as raízes de uma equação quadrática do tipo ax^2 + bx + c = 0. O programa deve lidar com todos os tipos de raízes (reais e complexas).

import cmath

def raizes_quadraticas (a, b, c):
    delta = cmath.sqrt(b**2 - 4*a*c)

    x1 = (-b + delta) / (2 * a)
    
    x2 = (-b - delta) / (2 * a)

    return (x1, x2)

a = float(input("Digite o valor de a: "))

b = float(input("Digite o valor de b: "))

c = float(input("Digite o valor de c: "))

print("As raízes da equação são: ", raizes_quadraticas(a, b, c))

#Exercício 6: Calcular o Fatorial de um Número
#Escreva uma função que calcula o fatorial de um número inteiro fornecido pelo usuário.

def fatorial(n):

    return 1 if n == 0 else n * fatorial(n-1)

num = int(input("Digite um número "))

print("Fatorial: ", fatorial(num))

#Exercício 7: Sequência de Fibonacci
#Crie um programa que gera a sequência de Fibonacci até um determinado número n fornecido pelo usuário.

def fibonacci(n):

    a , b = 0 , 1

    for _ in range (n):

        yield a

        a, b = b, a + b

n = int(input("Digite o número de termos da sequência de Fibonacci: "))

print("Sequências: ", list(fibonacci(n)))

#Exercício 8: Cálculo de Juros Compostos
#Faça um programa que calcula o montante final de um investimento com juros compostos. O usuário deve fornecer o capital inicial, a taxa de juros anual, e o número de anos.

def juros_compostos(capital, taxa, anos):

    return capital * (1 + taxa) ** anos

capital = float(input("Digite o capital inicial: "))

taxa = float(input("Digite a taxa de juros anual (em decimal): "))

anos = int(input("Digite o número de anos: "))

print("Montante final:", juros_compostos(capital, taxa, anos))

#Exercício 9: Conversão de Moedas
#Escreva um programa que converte uma quantidade de uma moeda (como dólar) para outra (como euro), considerando uma taxa de câmbio fornecida pelo usuário.

def converter_moeda(valor,taxa_cambio):

    return valor * taxa_cambio

valor = float(input("Digite o valor da moeda original: "))

taxa_cambio = float(input("Digite a taxa de câmbio: "))

print("Valor convertido: ",converter_moeda(valor,taxa_cambio))

#Exercício 10: Verificar se um Número é Primo
#Crie uma função que verifica se um número fornecido pelo usuário é primo ou não.

def e_primo(num):

    if num < 2:
        
        return False
    
    for i in range (2,int(num**0.5) +1):

        if num % i == 0:
            return False
    return True

numero = int(input("Digite um número "))

print("O número é primo!" if e_primo(numero) else "O número não é primo!")
