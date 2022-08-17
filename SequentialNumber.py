from tensorflow import keras
import numpy as np

# Primeiro estudo de ML - 17/08/2022 às 15h23

# Instancia a rede neural com 1 camada e 1 neurônio e 1 valor de entrada
modelo = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

# Otimizador e perda - OTIMIZADOR: Gera o palpite - PERDA: Verifica se o palpite é bom ou não
modelo.compile(optimizer='sgd', loss='mean_squared_error')

# Dados 
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)
# Fórmula = y = 2x - 1

# Encaixa x e y - leitura de 500 vezes, ou épocas.
modelo.fit(xs, ys, epochs=500)
x = 0


# Loop para prever com o y com base x para a leitura que já foi efetuada
while x != -22:  
    x = float(input('Insira o número (Insira -22 para sair): '))
    resultado = modelo.predict([x])

    # Arredondar para manter a saída clean, porém ciente da perda de especificidade 
    resultado = float(resultado)
    resultado = round(resultado, 1)

    print(resultado)
