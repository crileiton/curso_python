entrada_1 = int(input("Escriba el número hasta la tabla de multiplicar que quiera \n"))

for numero in range(1,entrada_1 + 1):
    for n in range(1,entrada_1 + 1):
        print(r'{:3d}'.format(numero * n))


