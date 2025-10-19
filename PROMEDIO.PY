from colorama import Fore, Style
#En esta parte le esto dando el "titulo"
print(Fore.WHITE+"===== CÁLCULO DE PROMEDIO DE CALIFICACIONES =====\n")

# Ingreso de calificaciones de cada materia, el fore es para darle color al texto y escogiendo el texto que se le quiera cambiar el color
N = (input(Fore.MAGENTA+("Ingresa el Nombre y Apellido del alumno a calificar: ")))
P = float(input(Fore.CYAN+("Ingresa la calificación de PROGRAMACIÓN: "+Fore.WHITE)))
ED = float(input(Fore.CYAN+"Ingresa la calificación de ESTRUCTURA DE DATOS: "+Fore.WHITE))
ADS = float(input(Fore.CYAN+"Ingresa la calificación de ANALISIS Y DISEÑO DE SOFTWARE: "+Fore.WHITE))
M = float(input(Fore.CYAN+"Ingresa la calificación de MICROPROCESADORES: "+Fore.WHITE))
AM = float(input(Fore.CYAN+"Ingresa la calificación de APLICACIONES MOVILES: "+Fore.WHITE))

# Cálculo Promedio, el cual suma todos los datos ingresados y se dividen entre las 5 materias
promedio = (P + ED + ADS + M + AM) / 5

# Mostrar el promedio junto con el nombre ingresado al incio

print(Fore.YELLOW+f"\nEl promedio del alumno {N} es:", round(promedio, 2))

# Condición para aprobar o reprobar, el cual se dice que si es mayor que 6 aprueba, pero en caso de que no se cumpla esa condicion por ende reprueba
if promedio >= 6:
    print(Fore.GREEN+"Resultado: El alumno APROBÓ🎉")
else:
    print(Fore.RED+"Resultado: El alumno REPROBÓ 😔")
