#Objetivo: Implementar la función convolución en una imagen con padding
#Fecha de creación: 20/03/25
#Fecha de modificación: 22/03/25
#Autora: Libia Flores

import numpy as np
import cv2
import matplotlib.pyplot as plt

#Definir función convolución
def convolution(matriz_foto, matriz_kernel):

    #Dimensiones de la imagen y kernel
    f_matriz, col_matriz = matriz_foto.shape
    f_kernel, col_kernel = matriz_kernel.shape

    #Dimensiones de la matriz de salida
    f_salida = f_matriz - f_kernel + 1
    col_salida = col_matriz - col_kernel + 1

    #Matriz de salida
    salida = np.zeros((f_salida, col_salida))

    #Aplicar la convolución recorriendo la matriz
    for i in range(f_salida):
        for j in range(col_salida):
            smatriz = matriz_foto[i:i + f_kernel, j:j + col_kernel] 
            salida[i][j] = np.sum(smatriz * matriz_kernel)  

    return salida

#Función para agregar padding
def padding(foto, p_size):
    return np.pad(foto, pad_width=p_size, mode='constant', constant_values=0)

#Ruta path de la imagen
foto_path = 'gatito2.jpg'  
foto = cv2.imread(foto_path)

#Convertir la imagen a escala de grises
if len(foto.shape) == 3:  
    foto = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)

#Agregar padding y aplicar funcion
p_size = 8 
foto_padd = padding(foto, p_size)

#Kernel de ejemplo
kernel = np.array([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
])

#Aplicar la convolución
resultado = convolution(foto_padd, kernel)

# Mostrar resultados
plt.subplot(1, 2, 1)
plt.imshow(foto, cmap='gray')
plt.title("Imagen Original")

plt.subplot(1, 2, 2)
plt.imshow(resultado, cmap='gray')
plt.title("Imagen con Convolución y Padding")

plt.show()
