import ReadScript as rs
import matplotlib.pyplot as plt

#"C:\\Users\\JuanF\\Desktop\\TFG\\Experimento1\\current.dat"

log=True
error=False
tipe = True

prueba=["C://Users//JuanF//Desktop//TFG//Experimento1//14nm.dat", "C://Users//JuanF//Desktop//TFG//Experimento1//12nm.dat"]

def graphId(x, y, e, log, type, error, num):    #Graphic generator of Vg vs Id

    if log:
        plt.yscale("log")       #Log Scale
        
    if num == 0:
        if error:
            plt.plot(x,y, 'bo-')
            plt.plot(x,e, 'bo--')
        else:
            plt.plot(x,y, 'bo-')

    elif num == 1:
        if error:
            plt.plot(x,y, 'rx-')
            plt.plot(x,e, 'rx--')
        else:
            plt.plot(x,y, 'rx-')

    elif num == 2:
        if error:
            plt.plot(x,y, 'gs-')
            plt.plot(x,e, 'gs--')
        else:
            plt.plot(x,y, 's-')

    elif num == 3:
        if error:
            plt.plot(x,y, 'm^-')
            plt.plot(x,e, 'm^--')
        else:
            plt.plot(x,y, 'm^-')

    elif num == 4:
        if error:
            plt.plot(x,y, 'yD-')
            plt.plot(x,e, 'yD--')

    else:
        if error:
            plt.plot(x,y, 'k+-')
            plt.plot(x,e, 'k+--')
        else:
            plt.plot(x,y, 'k+-')

    if type:
        plt.xlabel('$V_G (V)$') #axes
    else:
        plt.xlabel('$V_D (V)$')

    plt.ylabel('$I_D (μA)$')


def graphManage(lista, log, type, error):

    plt.figure()
    
    for i in range(len(lista)):
        if type:
            grafica=rs.ReadVg(lista[i])
        else:
            grafica=rs.ReadVg(lista[i]) #FUTURE READVD


        x=grafica[0] 
        y=grafica[1]
        e=grafica[2]
        graphId(x, y, e, log, type, error, i)
    #plt.legend(loc="best", facecolor="w", fontsize=16)
    plt.show()


graphManage(prueba, log, tipe, error)


# Aqui para ver el estilo de los puntos y las lineas
# http://research.iac.es/sieinvens/python-course/matplotlib.html
