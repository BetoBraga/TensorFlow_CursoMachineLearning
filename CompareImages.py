import tensorflow as tf
from tensorflow import keras

# Segundo estudo de ML - 17/08/2022 às 16h12

# Carrega o DataSet fashion_mnist do Keras
fashion_mnist = keras.datasets.fashion_mnist

# Ajusta imagens de treinamento aos labels
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Rede neural
modelo = keras.Sequential([
    # Entrada - imagem 28x28px  
    keras.layers.Flatten(input_shape=(28,28)),
    
    # 128 funções - f0 à f127
    keras.layers.Dense(128, activation=tf.nn.relu),
    
    # Última camada = 10 (Número de itens diferentes de roupas no dataset)
    keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

# Otimizador e Perda
modelo.compile(optimizer=tf.train.AdamOptimizer(),
               loss='sparse_categorical_crossentropy')

# Experimenta as imagens e labels em 5 épocas
modelo.fit(train_images, train_labels, = epochs=5)

# Testa o desempenho do modelo
test_loss, test_acc = modelo.evaluate(test_images, test_labels)

# Previsoes de volta
previsoes = modelo.predict(my_images)
