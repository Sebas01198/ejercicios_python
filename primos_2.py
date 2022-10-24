

numero = int(input("Ingrese un numero: "))

contador_de_ceros = 0
i = 2

if(numero > 1):

    while(i < numero):
        resto = numero % i
        if(resto == 0):
            contador_de_ceros = contador_de_ceros + 1
        i = i + 1
    
    if(contador_de_ceros == 0):
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} no es primo")

else:
    print("El numero tiene que ser mayor que 1")