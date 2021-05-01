#actividad 1.4-- atributos    
    
class Automovil: 
    """
Esta clase es para automoviles
    """
    marca = ""
    modelo = ""
    color = ""
    potencia = ""
    kilometraje = ""
    combustible = ""
    velocidad = ""

automovil1 = Automovil()

automovil1.marca = "nissan, bmw, audi, ford, chevrolet."
automovil1.modelo = "2021, 2020, 2019, 2018, 2017."
automovil1.color = "negro, rojo, azul, blanco, verde."
automovil1.potencia = "200 PH, 300 PH, 250 PH, 275 PH, 30 PH."
automovil1.kilometraje = "10 km, 11 km, 14 km, 31 km, 14 km."

print ("""
Esta clase es para automoviles:
    """)
print (automovil1.marca)
print (automovil1.modelo)
print (automovil1.color)
print (automovil1.potencia)
print (automovil1.kilometraje)
print (automovil1.combustible)
print (automovil1.velocidad)



class CompañiaTelefonica:
    """
    Esta clase es compañias de telefono
    """
    nombre = ""
    tarifa_por_minuto = ""
    tarifa_por_mensaje = ""
    
compañia = CompañiaTelefonica()

compañia.nombre = "telcel, movistar, unefo, atyt, claro."
compañia.tarifa_por_minuto = "$1, $2, $3, $4, $5."
compañia.tarifa_por_mensaje = "$0.1, $0.2, $0.3, $0.4, $0.5."

    
class Celulular:
    """
    Esta clase es para Celululares
    """
    marca = ""
    modelo = ""
    color = ""
    compañia_telefonica = ""
    saldo = ""
    
celular = Celulular()

celular.marca = "samsung, motorola, alcatel, lenovo, lg."
celular.modelo = "5030, a20, g6, a5, q6."
celular.color = "negro, rojo, azul, blanco, verde."
celular.compañia_telefonica = "telcel, movistar, unefo, atyt, claro."
celular.saldo = "$1, $2, $3, $4, $5."

class Alumno:
    """
    Esta clase es para alumnos
    """
    nombre = ""
    grado = ""
    grupo = ""
    promedio_general = ""
    
alumno = Alumno()
alumno.nombre = "manuel, raul, antonio, miguel, luis."
alumno.grado = "1º, 2º, 3º, 4º, 5º."
alumno.promedio_general = "10, 9, 8, 7, 6, 5"

class Materia:
    """
    Esta clase es para materias.
    """
    nombre = ""
    clave_asignatura = ""
    criterios_evaluacion = ""
    
materia = Materia()

materia.nombre = "ingles, matematicas, historia, contabilidad, quimica"
materia.clave_asignatura = "231, 312, 564, 364,234"
materia.criterios_evaluacion = "tareas, trabajos, participacion, asistencia, ortografia."


    