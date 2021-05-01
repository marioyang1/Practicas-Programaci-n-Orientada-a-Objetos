#CREAR UNA LISTA Y CONTAR EL NUMERO DE PALABRAS.
  
numero = int(input("Hola...\nEscribe el numero de palabras para tu lista: "))

if numero < 1:
    print ("Lo siento, intente con un numero mayor. ")
else:

    lista = []
    for a in range (numero):
        print ("Escribe la palabra", str (a + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print ("Listo, tu lista creada fue: ", lista)
    print ("Y el numero total de palabras es de: ", str (numero) + (".") + " ", end = "")
    
    
