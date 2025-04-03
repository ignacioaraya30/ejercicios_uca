#que ingrese dos valores y cual es el mayor que ingreso

valor1 = input("Ingrese el primer valor: ")
valor2 = input("Ingrese el segundo valor: ")

if valor1 > valor2:
    print("El primer valor ingresado es mayor")
elif valor2 > valor1:
    print("El segundo valor ingresado es mayor")
elif valor1 == valor2:
    print("Ambos valores son iguales")


