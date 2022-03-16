from tkinter import *
from functools import partial

root= Tk()

root.title("Simulación de Transistores")

#---------------Frame definition-------------

frame1=Frame(root)  #Directions Frame
frame1.grid(row=0, column=0)

frame2=Frame(root)  #options Freme
frame2.grid(row=0, column=1)

my_listbox = Listbox(frame1)
my_listbox.grid(row=1, column=1, padx=5, pady=5)


#--------------Funciones------------------------

lista=[]

def Add(text):
    #lista.append(text.get())
    my_listbox.insert(END, text.get())
    

def Delete():
    my_listbox.delete(ANCHOR)


#-----------------Texts Directions----------------

#Text str
graph1=StringVar()

#Text Box
cuadro1=Entry(frame1, textvariable=graph1)
cuadro1.grid(row=0, column=1, padx=5, pady=5)


#Text Title

text1=Label(frame1, text="Documento 1")
text1.grid(row=0, column=0, padx=5, pady=5)


#----------Buttons------------------

bAdd=Button(frame1, text="Add", width=5, command=partial(Add,graph1))
bAdd.grid(row=0, column=3, padx=5, pady=5)

bDelete=Button(frame1, text="Delete", width=5, command=Delete)
bDelete.grid(row=2, column=3, padx=5, pady=5)

root.mainloop()

#print(my_listbox.get(0, my_listbox.size())) #Metodo para extraer la info