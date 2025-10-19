from colorama import Fore, Style

#en este apartado se esta mostranto el titulo, por decirlo asi y el menu de nuestra calculadora.
def menu():
    print(Fore.YELLOW+'===== PROYECTO FINAL PROGRAMACION====\n')
    print(Fore.CYAN+'      ***Calculadora JJ***')
    print(Fore.BLUE+'1.Sumar')
    print(Fore.BLUE+'2.Resta')
    print(Fore.BLUE+'3.Multiplicacion')
    print(Fore.BLUE+'4.Division')
    print(Fore.BLUE+'5.Salir')

#en esta parte se pregunta al usuario que accion quiere realizar del menu, en caso de que seleccione el 5 esta por defaul que se termine el ciclo y deje "descansar el programa"
def Calculadora():
    while True:
        menu()
        opcion = input(Fore.YELLOW+'Selecciona la operacion que quieras realizar: ')
        if opcion == '5':
            print(Fore.MAGENTA+'Gracias por dejarme descansar un poco💤, nos vemos hasta que me ocupes. ')
            break

#ya en esta parte se muestra la eleccion que hizo el ususario, ya sea suma, resta, multiplicacion y division        
        try:
            
            if opcion == '1':
                print(Fore.GREEN+'Elegiste SUMA➕') 
            if opcion == '2':
                print(Fore.GREEN+'Elegiste RESTA➖')
            if opcion == '3':
                print(Fore.GREEN+'Elegiste MULTIPLICACION✖️')
            if opcion == '4':
                print(Fore.GREEN+'Elegiste DIVISION➗')
#y aqui es donde nos pide los dos numeros a realizar la operacion seleccionada
            num1 = float(input('Ingresa el primer numero: '))
            num2 = float(input('Ingresa el segundo numero: '))
#en esta parte se genera una validacion o condicion que dice que nada mas se pueden ingresar numeros que esten en el menu        
        except ValueError:
            print(Fore.RED+'Introduce un numero valido')
            continue
#y aqui ya es la impresion del resultado de la operacion elegida
        if opcion == '1':
            print('El resultado de tu SUMA es:', num1+num2)
        elif opcion == '2':
            print('El resultado de tu RESTA es:', num1-num2)
        elif opcion =='3':
            print('El resultado de tu MULTIPLICACION es:', num1*num2)
        elif opcion=='4':
            try:
                print('El resultado de tu DIVISION es', num1/num2)
            except ZeroDivisionError:
#en caso de que se quiera dividir entre 0, y muestra un mensaje 
                print('⚠️ No se puede DIVIDIR entre o, que no sabes😡 ⚠️ ')
        else:
            print('Opcion no valida')
        break

Calculadora()