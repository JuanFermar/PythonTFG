from operator import contains
import matplotlib.pyplot as plt
import numpy as np
from io import open

#COMENTARIO DE PRUEBA
#COMENTARIO DE PRUEBA 2

archivo_text=open("C:\\Users\\JuanF\\Desktop\\TFG\\texto_prueba.txt", "r")

text = archivo_text.read().split("\n")

archivo_text.close()

error = False
x = ([])
y = ([])
y_error = ([])
y_def = ([])
y_def_error = ([])


for i in text:
    if not i[0] == "#": 
        for j in i.split(" "):
            if not "E" in j:
                x.append(float(j))
            else:
                if not error:
                    temp = j.split("E")
                    y.append(float(temp[0]) * (10**(float(temp[1]))))
                    error=True
                else:
                    temp = j.split("E")
                    y_error.append(float(temp[0]) * (10**(float(temp[1]))))
                    error=False


for i in range(len(y)):
    y_def.append(abs((10**6) * y[i]))
    y_def_error.append(abs((10**6) * y_error[i]))


#GRAFICA
plt.yscale("log")
plt.plot(x,y_def, 'o-')
plt.xlabel('$V_G (V)$')
plt.ylabel('$I_D (μA)$')
plt.show()

# Aqui para ver el estilo de los puntos y las lineas
# http://research.iac.es/sieinvens/python-course/matplotlib.html

#Leer tecto por filas y columnas
#https://www.lawebdelprogramador.com/foros/Python/691962-leer-txt-por-fila-y-columnas.html

