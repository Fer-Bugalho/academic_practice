#Exercício 1: Gráfico de Uma Função Linear
#Crie um gráfico para a função y = 2x + 3 para valores de x no intervalo de 5 a 10.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(5, 10, 100)
y = 2 * x + 3

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico da Função Linear y = 2x + 3')
plt.grid(True)
plt.show()

#Exercício 2: Gráfico de uma Função Quadrática
#Desenhe o gráfico da função y = x^2 - 4x + 4. Crie uma massa de dados de exemplo usando np.linspace().

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,6,1000)
y = x ** 2 - 4 * x + 4

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico da Função Linear y = x^2 - 4x + 4')
plt.grid(True)
plt.show()

#Exercício 3: Gráfico de Uma Função Senoidal
#Crie um gráfico da função y = sin(x) para valores de x no intervalo de 0 a 2π.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,(2 * np.pi),100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de uma Função Senoidal y = sin(x)')
plt.grid(True)
plt.show()

#Exercício 4: Gráfico de Uma Função Exponencial
#Crie um gráfico para a função y = e^x para valores de x no intervalo de -2 a 2.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,2,100)
y = np.exp(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de uma Função Exponencial y = e^x')
plt.grid(True)
plt.show()

#Exercício 5: Gráfico de uma Função Logarítmica: 
#Desenhe o gráfico de y = log(x) (logaritmo natural) para valores de x no intervalo de 0.1 a 10.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1,10,100)
y = np.log(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de uma Função Logarítmica y = log(x)')
plt.grid(True)
plt.show()

#Exercício 6: Resolver uma Equação Quadrática
#Escreva um script em Python que resolve a equação x^2 − 5x + 6 = 0 e imprime as raízes.

import cmath

a, b, c = 1, -5, 6

delta = (b ** 2) - (4 * a * c)

sol_positivo = (-b + cmath.sqrt(delta)) / (2 * a )
sol_negativo = (-b - cmath.sqrt(delta)) / (2 * a )

print("As raízes são {0} e {1}".format(sol_positivo,sol_negativo))

#Exercício 7: Equação Quadrática com Entrada do Usuário
#Modifique o programa anterior para aceitar coeficientes a, b, e c de um usuário e resolver a equação quadrática correspondente.

a = float(input("Digite o Coeficiente a: "))
b = float(input("Digite o Coeficiente b: "))
c = float(input("Digite o Coeficiente c: "))

import cmath

delta = (b ** 2) - (4 * a * c)

sol_positivo = (-b + cmath.sqrt(delta)) / (2 * a )
sol_negativo = (-b - cmath.sqrt(delta)) / (2 * a )

print("As raízes são {0} e {1}".format(sol_positivo,sol_negativo))



