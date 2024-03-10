while True:
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    eleccion = input("Ingrese el número de la operación deseada: ")

    if eleccion == '5':
        print("¡Hasta luego!")
        break

    if eleccion not in ['1', '2', '3', '4']:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        continue

    A = float(input("Ingrese el primer número: "))
    B = float(input("Ingrese el segundo número: "))

    if eleccion == '1':
        resultado = A + B
        operacion = "suma"
    elif eleccion == '2':
        resultado = A - B
        operacion = "resta"
    elif eleccion == '3':
        resultado = A * B
        operacion = "multiplicación"
    elif eleccion == '4':
        if B == 0:
            print("Error: división por cero.")
            continue
        else:
            resultado = A / B
            operacion = "división"

    print(f"El resultado de la {operacion} es: {resultado}\n")