import ReadScript as rs
import matplotlib.pyplot as plt

def graphId(x, y, e, log, type, error, num, name):    #Graphic generator of Vg/Vd vs Id

    if log==1:
        plt.yscale("log")       #Log Scale
        
    if num == 0:    #Define the style in function the amount of curves (num) 
        if error==1:    #we discuss if we want to graph the error
            plt.plot(x,y, 'bo-', label=name)
            plt.plot(x,e, 'bo--', label=name+" error")
        else:
            plt.plot(x,y, 'bo-', label=name)

    elif num == 1:
        if error==1:
            plt.plot(x,y, 'r^-', label=name)
            plt.plot(x,e, 'r^--', label=name+" error")
        else:
            plt.plot(x,y, 'r^-', label=name)

    elif num == 2:
        if error==1:
            plt.plot(x,y, 'yD-', label=name)
            plt.plot(x,e, 'yD--', label=name+" error")
        else:
            plt.plot(x,y, 'yD-', label=name)

    elif num == 3:
        if error==1:
            plt.plot(x,y, 'mx-', label=name)
            plt.plot(x,e, 'mx--', label=name+" error")
        else:
            plt.plot(x,y, 'mx-', label=name)

    elif num == 4:
        if error==1:
            plt.plot(x,y, 'g+-', label=name)
            plt.plot(x,e, 'g+--', label=name+" error")
        else:
            plt.plot(x,y, 'g+-', label=name)

    else:
        if error==1:
            plt.plot(x,y, 'k+-', label=name)
            plt.plot(x,e, 'k+--', label=name+" error")
        else:
            plt.plot(x,y, 'k+-', label=name)

    #Axes

    if type==1:                 #Vg vs Id or vd vs Id
        plt.xlabel('$V_G (V)$') 
    else:
        plt.xlabel('$V_D (V)$')

    plt.ylabel('$I_D (μA)$')


def graphManage(lista, log, type, error, title):
    if len(lista) != 0: 
        plt.figure()

        for i in range(len(lista)): #we graph all the files of the list
            if type == 1:   #We read the data in function of the file
                grafica=rs.ReadVg(lista[i])
            else:
                grafica=rs.ReadVd(lista[i]) #FUTURE READVD
            
            name2=lista[i].split("//")  #we obtain the name of the graph
            name1=name2[len(name2)-1].split(".d")
            name=name1[0]

            x=grafica[0] 
            y=grafica[1]
            e=grafica[2]

            graphId(x, y, e, log, type, error, i, name) 
            plt.legend(loc="best", facecolor="w", fontsize=8)

        plt.title(title)
        plt.show()