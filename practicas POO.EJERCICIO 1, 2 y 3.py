#practicas POO.EJERCICIO 1, 2 y 3


class Persona:
    """
    Esta clase es para personas
    
    """
nombre = ""
edad = None
DNI = ""

persona = Persona()
persona.nombre = input("Escribe tu nombre: ")

persona.edad = int(input("¿Cuántos años tiene? "))
if persona.edad <= 18:
    print("Eres menor de edad <-----")
else:
    print(persona.nombre, "ERES MAYOR DE EDAD <-----")
persona.NDI = input("Escribe tu DNI: ")

print (persona.nombre, "TIENES ", persona.edad, "AÑOS Y TU DNI ES:", persona.NDI)


# EJERCICIO 2 

class Cuenta:
    """
    Esta clase es para Cuenta
    
    """
titular = ""
cantidad = None
saldo = 500

cuenta = Cuenta()
cuenta.titular = input("Nombre del titular: ")
while cuenta.titular =="": 
 print ("Debes escribir el nombre del titular, intenta de nuevo.", )
 cuenta.titular = input("Nombre del titular: ")
print ("Hola", cuenta.titular,"tu saldo disponible es de: $", saldo)
cuenta.ingresar = float (input("Escribe la cantidad a ingresar: "))
print ("los datos de tu cuenta son: ")
print ("Nombre del Titular:", cuenta.titular)
print ("Tu saldo disponible ahora es de: $", saldo + cuenta.ingresar)
cuenta.cantidad = float (input("Escribe la cantidad a retirar: "))

while cuenta.cantidad > cuenta.ingresar + saldo:
    print ("No tienes la cantidad esa suficiente de saldo")
    cuenta.cantidad = float (input("Escribe la cantidad a retirar: "))
else:
    cuenta.cantidad - saldo
    print ("Tu saldo disponible ahora es de: ")
    print ("$", saldo + cuenta.ingresar - cuenta.cantidad)
    print ("Hasta luego")
    

#ejercicio 3

class CuentaJoven:
    """
    Esta clase es para Cuenta Joven
    
    """
titular = ""
edad = None
saldo = 500
ingresar = None
cuenta = CuentaJoven()
cuenta.retirar = None

cuenta.titular = input("Nombre del titular: ")
print ("Hola", cuenta.titular,"si estas en el rango de edad requerido, puedes ganarte una bonificacion")
cuenta.edad = int(input("Dime tu edad: "))
if cuenta.edad == (18,19,20,21,22,23,24,25):
    print ("aceptado")
else:
    print ( "Ganaste una bonificacion del 10%")
print ("los datos de tu cuenta son: ")
print ("Nombre del Titular:", cuenta.titular)
print ("Tu saldo disponible era de: $", saldo)
print ("Mas 10% de bonificacion")
print ("Tu saldo ahora es de: ", "$", saldo + saldo * 10 / 100)
cuenta.total = (saldo + saldo * 10 / 100)
cuenta.ingresar = float (input("Escribe la cantidad a ingresar: "))
print (cuenta.ingresar + saldo + saldo * 10 / 100 )
print ("los datos de tu cuenta son: ")
print ("Nombre del Titular:", cuenta.titular)
print ("Tu saldo disponible ahora es de: $", cuenta.ingresar + saldo + saldo * 10 / 100 )
cuenta.retirar = float (input("Escribe la cantidad a retirar: "))
if cuenta.retirar > cuenta.total:
    print ("No tienes la cantidad esa suficiente de saldo")
    cuenta.cantidad = float (input("Escribe la cantidad a retirar: "))
else:
    cuenta.total - cuenta.retirar
    print ("Tu saldo disponible ahora es de: ")
    print ("$", cuenta.total - cuenta.retirar)
    print ("Hasta luego")


