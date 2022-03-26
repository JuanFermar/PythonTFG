from io import open

archivo_text=open("C://Users//JuanF//Desktop//TFG//Experimento1//$V_G$=0.5.dat", "r")

text = archivo_text.read().split("\n")

archivo_text.close()

probando=text[0].split("    ")
print(probando[1].split("  "))