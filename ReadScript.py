from io import open

#COMENTARIO DE PRUEBA

def ReadVg(dir):
    archivo_text=open(dir, "r")

    text = archivo_text.read().split("\n")
    archivo_text.close()

    error = False
    x = ([])
    y = ([])
    y_error = ([])
    y_def = ([])
    y_def_error = ([])

    #Reads the txt file
    for i in text:
        if not i[0] == "#": #Descarto las lineas que esten comentadas
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

    return(x, y_def, y_def_error)




