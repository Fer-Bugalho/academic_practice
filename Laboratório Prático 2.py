#Exercício 1: Gráfico de Uma Função Linear
#Crie um gráfico para a função y = 2x + 3 para valores de x no intervalo de 5 a 10.

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    
    return (2 * x + 3)

x = np.linspace(5,10)

plt.figure(figsize = (6,4))
plt.plot(x, f(x), label = 'y = 2x + 3')
plt.grid()

