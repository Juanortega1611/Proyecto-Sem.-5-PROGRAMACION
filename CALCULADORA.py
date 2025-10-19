from colorama import Fore, Style
def menu():
    print(Fore.YELLOW+'===== PROYECTO FINAL PROGRAMACION====\n')
    print(Fore.CYAN+'      ***Calculadora JJ***')
    print(Fore.BLUE+'1.Sumar')
    print(Fore.BLUE+'2.Resta')
    print(Fore.BLUE+'3.Multiplicacion')
    print(Fore.BLUE+'4.Division')
    print(Fore.BLUE+'5.Salir')

def Calculadora():
    while True:
        menu()
        opcion = input(Fore.YELLOW+'Selecciona la operacion que quieras realizar: ')
        if opcion == '5':
            print(Fore.MAGENTA+'Gracias por dejarme descansar un poco💤, nos vemos hasta que me ocupes. ')
            break
        
        try:
            
            if opcion == '1':
                print(Fore.GREEN+'Elegiste SUMA➕') 
            if opcion == '2':
                print(Fore.GREEN+'Elegiste RESTA➖')
            if opcion == '3':
                print(Fore.GREEN+'Elegiste MULTIPLICACION✖️')
            if opcion == '4':
                print(Fore.GREEN+'Elegiste DIVISION➗')

            num1 = float(input('Ingresa el primer numero: '))
            num2 = float(input('Ingresa el segundo numero: '))
        
        except ValueError:
            print(Fore.RED+'Introduce un numero valido')
            continue

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
                print('⚠️ No se puede DIVIDIR entre o, que no sabes😡 ⚠️ ')
        else:
            print('Opcion no valida')
        break

Calculadora()