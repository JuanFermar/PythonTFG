from PIL import ImageTk
import PIL.Image
from tkinter import *
from functools import partial
from tkinter import filedialog
from tkinter import messagebox
import webbrowser

import GraphicGenerator as gg



#--------------------ROOT DEFINITION-----------------
root= Tk()

root.title("Transistor Simulation")
root.resizable(0,0)

barraMenu=Menu(root)
root.config(menu=barraMenu)

#--Variables---

bg1= "white" 
bg2= "#808080" 
root.config(background=bg2)

Log=IntVar()
vgChoice=IntVar()
errorChoice=IntVar()

graph1=StringVar()
graphTitle=StringVar()


#---------------FRAME DEFINITION-------------

frame1=Frame(root,width=100, height=100, background=bg1)  #Directions Frame
frame1.grid(row=0, column=0)

frame2=Frame(root)  
frame2.grid(row=0, column=1)
frame2.config(bg=bg2)

#------------------LISTBOX & SCROLLBARS--------------------

my_listbox = Listbox(frame1)
my_listbox.grid(row=1, column=1, padx=5, pady=5)

scrollVert=Scrollbar(frame1,orient="vertical")
scrollVert.config(command=my_listbox.yview)
scrollVert.grid(row=1, column=2, sticky="nsew")


scrollHori=Scrollbar(frame1, orient="horizontal")
scrollHori.config(command=my_listbox.xview)
scrollHori.grid(row=2, column=1, sticky="nsew")

my_listbox.config(yscrollcommand=scrollVert.set, xscrollcommand=scrollHori.set)

#--------------FUNCTIONS------------------------

aux = ()

def Add(text):  #We add a direction in the listbox
    my_listbox.insert(END, text.get())
    graph1.set("")
    

def Delete():   #Delect the selected direction
    my_listbox.delete(ANCHOR)


def Search():
    frame1.filename = filedialog.askopenfilename(title="search documents", filetypes=(('archivos txt', '*.dat'),('todos los archivos', '*')))
    newtext = frame1.filename.replace('/', "//")    #We need the replace
    graph1.set(newtext) 

def preGraph(): #Extract the information from the listbox and the other variables
    try:
        aux = my_listbox.get(0, my_listbox.size())
        listaFinal=[]

        for i in range(len(aux)):
            listaFinal.append(aux[i])
        gg.graphManage(listaFinal, Log.get(), vgChoice.get(), errorChoice.get(), graphTitle.get())
    except:
        messagebox.showerror(title= "ERROR", message="This files are not suitable")

#--Menus Functions--

def Default():  #We stablish a default values
    graph1.set("")
    graphTitle.set("")
    Log.set(1)
    vgChoice.set(1)
    errorChoice.set(1)

def callback():
    webbrowser.open_new("https://www.google.es/")
    pop.destroy

def CodeSource():   #generate the window with github url

    global pop
    pop = Toplevel(root)
    pop.title("Source Code")
    pop.geometry("300x135")
    pop.config(bg="white")

    global pic 
    global new_pic

    pic = PIL.Image.open("C:\\PythonTFG\\github.png")

    resized = pic.resize((40, 40), PIL.Image.ANTIALIAS)
    
    new_pic = ImageTk.PhotoImage(resized)

    pop_label = Label(pop, text = "Do you want to see the Source Code?", background="white")
    pop_label.grid(row=0, column=1, padx=5, pady=5)

    image_Frame = Frame(pop, background="white")    
    image_Frame.grid(row=1, column=0, padx=10, pady=10)

    but_Frame = Frame(pop, background="white")
    but_Frame.grid(row=1, column=1, padx=10, pady=10)

    my_icon = Label(image_Frame, image = new_pic, borderwidth=0)
    my_icon.grid(row=0, column=0, padx=10, pady=10)

    yes = Button(but_Frame, text="Yes", command= callback)
    yes.grid(row=0, column=0, padx=10, pady=10)

    no = Button(but_Frame, text="No", command=pop.destroy)
    no.grid(row=0, column=2, padx=10, pady=10)
       

#-----------------------MENUS---------------------
#    
generalMenu=Menu(barraMenu, tearoff=0)
generalMenu.add_command(label="Default", command=Default)
generalMenu.add_command(label="Source Code...", command=CodeSource)


barraMenu.add_cascade(label="Options", menu=generalMenu)


#-----------------TEXTS DIRECTIONS----------------

#Text Box
cuadro1=Entry(frame1, textvariable=graph1)
cuadro1.grid(row=0, column=1, padx=5, pady=5)

cuadro2=Entry(frame2, textvariable=graphTitle)
cuadro2.grid(row=0, column=1, padx=5, pady=5)


#Text 
text1=Label(frame1, text="Files:", background=bg1)
text1.grid(row=0, column=0, padx=5, pady=5)


text2=Label(frame2, text="Title:", background=bg2)
text2.grid(row=0, column=0, padx=5, pady=5)


#-----------------------------Graphic options---------------------------------

#Linear or Logarithmic Scale

scales = Label(frame2, text="Y axe scale:", justify=RIGHT, background=bg2)
scales.grid(row=1, column=0, padx=5, pady=5)

bLog = Radiobutton(frame2, text="Logarithmic", variable=Log, value=1, background=bg2)
bLog.grid(row=1, column=1, padx=5, pady=5)

bLin = Radiobutton(frame2, text="Linear", variable=Log, value= 2, background=bg2)
bLin.grid(row=1, column=2, padx=5, pady=5)

#Vg vs Id or vd vs Id

simulationType = Label(frame2, text="Type of simulation:", justify=RIGHT, background=bg2)
simulationType.grid(row=2, column=0, padx=5, pady=5)

bVg = Radiobutton(frame2, text="Vg", variable=vgChoice, value=1, background=bg2)
bVg.grid(row=2, column=1, padx=5, pady=5)

bVd = Radiobutton(frame2, text="Vd", variable=vgChoice, value=2, background=bg2)
bVd.grid(row=2, column=2, padx=5, pady=5)

#Decide to graph the error 

error = Label(frame2, text="Graph Error:", justify=RIGHT, background=bg2)
error.grid(row=3, column=0, padx=5, pady=5)

bError = Radiobutton(frame2, text="Yes", variable=errorChoice, value=1, background=bg2)
bError.grid(row=3, column=1, padx=5, pady=5)

bError = Radiobutton(frame2, text="No", variable=errorChoice, value=2, background=bg2)
bError.grid(row=3, column=2, padx=5, pady=5)


#------------------------------BUTTONS---------------------------------

bAdd=Button(frame1, text="Add", width=5, command=partial(Add,graph1))   #Add a File
bAdd.grid(row=0, column=4, padx=5, pady=5)

bDelete=Button(frame1, text="Delete", width=5, command=Delete)  #Delete a File
bDelete.grid(row=3, column=4, padx=5, pady=5)

bSearch = Button(frame1, text="···", command=Search)    #Search a File
bSearch.grid(row=0, column=3, padx=5, pady=5)

bGraph=Button(frame1, text="Graph", height=1, width=15, command=preGraph)   #Graph the selected files
bGraph.grid(row=3, column=1, padx=5, pady=5)



root.mainloop() #WE END