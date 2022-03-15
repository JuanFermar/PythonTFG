#from ReadScript import ReadVg
import ReadScript as rs
import matplotlib.pyplot as plt

#"C:\\Users\\JuanF\\Desktop\\TFG\\current.dat"

grafica=rs.ReadVg("C:\\Users\\JuanF\\Desktop\\TFG\\current.dat") #Load the information

#Save in 3 variables
x=grafica[0] 
y=grafica[1]
e=grafica[2]

def graficarVg(x, y, e):    #Graphic generator of Vg vs Id
    plt.yscale("log")       #Log Scale
    plt.plot(x,y, 'o-')     #plot
    plt.xlabel('$V_G (V)$') #axes
    plt.ylabel('$I_D (μA)$')
    plt.show()


def graficarVd(x, y, e):  #Graphic generator of Vg vs Id
    plt.yscale("log")
    plt.plot(x,y, 'o-')
    plt.xlabel('$V_D (V)$')
    plt.ylabel('$I_D (μA)$')
    plt.show()
    
graficarVg(x, y, e)
# Aqui para ver el estilo de los puntos y las lineas
# http://research.iac.es/sieinvens/python-course/matplotlib.html

#Leer tecto por filas y columnas
#https://www.lawebdelprogramador.com/foros/Python/691962-leer-txt-por-fila-y-columnas.html