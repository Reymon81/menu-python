def menu():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input())
            correcto=True
        except ValueError:
            print('Error, introduce un numero entre 1 y 6: ', end=" ")
     
    return num
 
salir = False
opcion = 0
 
while not salir:
    
    print()
    print("1. opcion 1")
    print("2. opcion 2")
    print("3. opcion 3")
    print("4. opcion 4")
    print("5. opcion 5")
    print("6. salir")
    print() 
    print("Elige una opcion: ", end=" ")
    opcion = menu()

    if opcion == 1:
        print("opcion 1")
    
    elif opcion == 2:
        
        print("opcion 2")

    elif opcion == 3:
        
        print("opcion 3")

    elif opcion == 4:
        
        print("opcion 4")

    elif opcion == 5:
        
        print("opcion 5")

    elif opcion == 6:
        salir = True
    else:
        print ("\n Error, debes introducir un numero entre 1 y 6")