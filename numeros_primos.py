
numero = int(input("Ingrese un numero: "))

contador = 0

if (numero > 1):
    
    for i in range(2,numero):
        resto = numero % i

        if(resto == 0):
            contador = contador + 1;

    if(contador == 0):
        print(f"El numero {numero} es un numero primo")
    else:
        print(f"El numero {numero} no es un numero primo")

else:
    print("El numero tiene que ser mayor a 1")
    
