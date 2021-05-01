#ARREGLOS UNIDIMENSIONAL EN PHYTHON

def leer_frase ():
    global txt
    txt= (input("Esta es mi frase: " )).lower()
def contar_vocales():
        vocal = ["a", "e", "i", "o", "u"]
        cont=0
        for a in vocal:
             for b in txt:
                 if(a==b):
                    cont+=1
        print ("Las vocales que hay son: ", cont)
leer_frase()
contar_vocales()