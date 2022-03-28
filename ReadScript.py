from io import open

#Read the output file, that a have a constant drain voltage

def ReadVg(dir):
    archivo_text=open(dir, "r")

    try:
        text = archivo_text.read().split("\n")
        archivo_text.close()

        error = False
        x = ([])    #Gate voltage vector
        y = ([])    #Drain current vector
        y_error = ([])  #Drain current error vector

        y_def = ([])
        y_def_error = ([])

        #Reads the txt file
        for i in text:
            if not i[0] == "#": #Discard first line 
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


        for i in range(len(y)): #adjust magnitud order (uA)
            y_def.append(abs((10**6) * y[i]))
            y_def_error.append(abs((10**6) * y_error[i]))

        return(x, y_def, y_def_error)   #return the result
    except:
        print("Error")  #We detect that de direction is incorrect

#Read the output file, that a have a constant gate voltage

def ReadVd(dir):
    archivo_text=open(dir, "r")

    try:
        text = archivo_text.read().split("\n")
        archivo_text.close()

        error = False
        x = ([])    #Gate voltage vector
        y = ([])    #Drain current vector
        y_error = ([])  #Drain current error vector

        y_def = ([])
        y_def_error = ([])


        #Reads the txt file
        for i in text:
            aux = i.split("    ")   #we ignore the first tabulation 

            for j in aux[1].split("  "):    #we work with the data
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


        for i in range(len(y)): #adjust magnitud order (uA)
            y_def.append(abs((10**6) * y[i]))
            y_def_error.append(abs((10**6) * y_error[i]))

        return(x, y_def, y_def_error)   #return the result

    except:
        print("Error")  #We detect that de direction is incorrect