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

