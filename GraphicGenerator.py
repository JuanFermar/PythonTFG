import ReadScript as rs
import matplotlib.pyplot as plt

#"C:\\Users\\JuanF\\Desktop\\TFG\\current.dat"

a=[]
log=True
prueba=["C:\\Users\\JuanF\\Desktop\\TFG\\current.dat", "C:\\Users\\JuanF\\Desktop\\TFG\\texto_prueba.txt"]

# def addButton(dir):
#     # excepcion no se entra
#     #si
#         a.append(dir)


def graphVg(x, y, log, num, axes):    #Graphic generator of Vg vs Id

    if log:
        plt.yscale("log")       #Log Scale
        
    if num == 0:
        plt.plot(x,y, 'o-')
    elif num == 1:
        plt.plot(x,y, 'x-')
    elif num == 2:
        plt.plot(x,y, 's-')
    elif num == 3:
        plt.plot(x,y, '^-')
    elif num == 4:
        plt.plot(x,y, 'D-')
    else:
        plt.plot(x,y, '+-')

    if axes == "Vg":
        plt.xlabel('$V_G (V)$') #axes
    elif axes == "Vd":
        plt.xlabel('$V_D (V)$')

    plt.ylabel('$I_D (μA)$')


def graphManage(lista, magnitud):

    plt.figure()
    
    for i in range(len(lista)):
        if magnitud == "Vg":
            grafica=rs.ReadVg(lista[i])
        elif magnitud == "Vd":
            grafica=rs.ReadVg(lista[i]) #FUTURE READVD


        x=grafica[0] 
        y=grafica[1]
        e=grafica[2]
        graphVg(x, y, log, i, magnitud)
    
    plt.show()


graphManage(prueba, "Vd")


# Aqui para ver el estilo de los puntos y las lineas
# http://research.iac.es/sieinvens/python-course/matplotlib.html
