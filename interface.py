from tkinter import *
from functools import partial
from tkinter import filedialog
from turtle import left
root= Tk()

root.title("Simulación de Transistores")

#---------------Frame definition-------------

frame1=Frame(root)  #Directions Frame
frame1.grid(row=0, column=0)

frame2=Frame(root)  #options Frame
frame2.grid(row=0, column=1)

my_listbox = Listbox(frame1)
my_listbox.grid(row=1, column=1, padx=5, pady=5)

scrollVert=Scrollbar(frame1,orient="vertical")
scrollVert.config(command=my_listbox.yview)
scrollVert.grid(row=1, column=2, sticky="nsew")


scrollHori=Scrollbar(frame1, orient="horizontal")
scrollHori.config(command=my_listbox.xview)
scrollHori.grid(row=2, column=1, sticky="nsew")

my_listbox.config(yscrollcommand=scrollVert.set, xscrollcommand=scrollHori.set)

#--------------Funciones------------------------

def Add(text):
    my_listbox.insert(END, text.get())
    graph1.set("")
    

def Delete():
    my_listbox.delete(ANCHOR)

def Search():
    frame1.filename = filedialog.askopenfilename(title="search documents", filetypes=(('archivos txt', '*.txt'),('todos los archivos', '*')))
    newtext = frame1.filename.replace('/', "//")
    graph1.set(newtext)

    


#-----------------Texts Directions----------------

#Text str
graph1=StringVar()
graphTitle=StringVar()

#Text Box
cuadro1=Entry(frame1, textvariable=graph1)
cuadro1.grid(row=0, column=1, padx=5, pady=5)

cuadro2=Entry(frame2, textvariable=graphTitle)
cuadro2.grid(row=0, column=1, padx=5, pady=5)


#Text Title

text1=Label(frame1, text="Documentos:")
text1.grid(row=0, column=0, padx=5, pady=5)


text2=Label(frame2, text="Title:")
text1.grid(row=0, column=0, padx=5, pady=5)


#----------Buttons------------------

bAdd=Button(frame1, text="Add", width=5, command=partial(Add,graph1))
bAdd.grid(row=0, column=4, padx=5, pady=5)

bDelete=Button(frame1, text="Delete", width=5, command=Delete)
bDelete.grid(row=3, column=4, padx=5, pady=5)

bGraph=Button(frame1, text="Graph",height=1, width=15)
bGraph.grid(row=3, column=1, padx=5, pady=5)

bSearch = Button(frame1, text="···", command=Search)
bSearch.grid(row=0, column=3, padx=5, pady=5)

#-----------Graphic options-----------

Log=BooleanVar()
choiceVg=BooleanVar()
errorChoice=BooleanVar()
Log.set(True)
choiceVg.set(True)
errorChoice.set(False)


scales = Label(frame2, text="Y axe scale:", justify=RIGHT)
scales.grid(row=1, column=0, padx=5, pady=5)

bLog = Radiobutton(frame2, text="Logarithmic", variable=Log, value=True)
bLog.grid(row=1, column=1, padx=5, pady=5)

bLin = Radiobutton(frame2, text="Linear", variable=Log, value= False)
bLin.grid(row=1, column=2, padx=5, pady=5)



simulationType = Label(frame2, text="Type of simulation:", justify=RIGHT)
simulationType.grid(row=2, column=0, padx=5, pady=5)

bVg = Radiobutton(frame2, text="Vg", variable=choiceVg, value=True)
bVg.grid(row=2, column=1, padx=5, pady=5)

bVd = Radiobutton(frame2, text="Vd", variable=choiceVg, value=False)
bVd.grid(row=2, column=2, padx=5, pady=5)



error = Label(frame2, text="Graph Error:", justify=RIGHT)
error.grid(row=3, column=0, padx=5, pady=5)

bError = Radiobutton(frame2, text="Yes", variable=errorChoice, value=True)
bError.grid(row=3, column=1, padx=5, pady=5)

bError = Radiobutton(frame2, text="No", variable=errorChoice, value=False)
bError.grid(row=3, column=2, padx=5, pady=5)

root.mainloop()

#print(my_listbox.get(0, my_listbox.size())) #Metodo para extraer la info