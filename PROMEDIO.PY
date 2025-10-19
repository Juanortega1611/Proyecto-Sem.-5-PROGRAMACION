from colorama import Fore, Style
print(Fore.WHITE+"===== CÁLCULO DE PROMEDIO DE CALIFICACIONES =====\n")

# Ingreso de calificaciones
N = (input(Fore.MAGENTA+("Ingresa el Nombre y Apellido del alumno a calificar: ")))
P = float(input(Fore.CYAN+("Ingresa la calificación de PROGRAMACIÓN: "+Fore.WHITE)))
ED = float(input(Fore.CYAN+"Ingresa la calificación de ESTRUCTURA DE DATOS: "+Fore.WHITE))
ADS = float(input(Fore.CYAN+"Ingresa la calificación de ANALISIS Y DISEÑO DE SOFTWARE: "+Fore.WHITE))
M = float(input(Fore.CYAN+"Ingresa la calificación de MICROPROCESADORES: "+Fore.WHITE))
AM = float(input(Fore.CYAN+"Ingresa la calificación de APLICACIONES MOVILES: "+Fore.WHITE))

# Cálculo Promedio
promedio = (P + ED + ADS + M + AM) / 5

# Mostrar el promedio

print(Fore.YELLOW+f"\nEl promedio del alumno {N} es:", round(promedio, 2))

# Condición para aprobar o reprobar
if promedio >= 6:
    print(Fore.GREEN+"Resultado: El alumno APROBÓ🎉")
else:
    print(Fore.RED+"Resultado: El alumno REPROBÓ 😔")
