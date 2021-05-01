#lo basico de PHYTHON. ejercicios 1, 2, 3, 4 


#1
print("Buenos días")


#2
print(12*13)
print(226/5)
print(16**2)
print(169%7)

#3
input ("Hola Sr. Escriba su nombre: ")
input("Ahora escriba su apellido: ")

nombre1 = input ("Escriba un nombre: ")
nombre2 = input ("Escriba otro nombre: ")
c = (" ")
print ("Su producto es : ", nombre1 + c + nombre2)

n1 = int(input("Dime el valor para a: "))
n2 = int(input("Dime el valor para b: "))
n3 = int(input("Dime el valor para c: "))
print ("El resiultado de (a+c)*c es: ", (n1 + n2) * n3)
print ("Y el resultdo de a*c+b*c es: ", n1 * n3 + n2 *n3)

#4
num = input ("Dame un numero: ")
num = int(num)
if num%2 == 0:
     print ("Este numero es par.")
else:
    print ("Este numerop es impar")
    
num = int(input("Dame un numero real: "))
if num > 0:
    print("Tu numero es positivo")
else:
    print ("Tu numero es negativo o cero")

num1 = int(input("Dame tu primer numero (entero): "))
num2 = int(input("Dame tu segundo numero (entero): "))
print ("Dividiendo esos numeros, el resultado es: ", num1 / num2)
