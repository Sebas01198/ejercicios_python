
#paso a paso para fritar un huevo

huevo = input("¿Hay huevo?, responde si o no: ")

if(huevo == "si"):
    print("Buscar utencilios")
    print("Buscar ingredientes")
    print("Encender estufa")
    print("Calentar el sarten")
    print("Esperar que caliente el sarten")
    print("Verter el aceite")
    print("Esperar que caliente el aceite")
    print("Romber huevo")
    print("Verifica que el huevo este bueno\n")

    huevo_frito = input("¿El huevo esta bueno?: ")
    while(huevo_frito == "no"):
        print("Escoger otro huevo")
        print("Verifica que el huevo este bueno")
        huevo_frito = input("¿El huevo esta bueno?: ")
        
    if(huevo_frito == "si"):
        print("echar huevo")
        print("condimentar huevo")
        print("revisar que el huevo este al gusto")
        huevo_gusto = input("¿El huevo esta al gusto? responde si o no: ")

        while(huevo_gusto == "no"):
            print("Seguir cocinando")
            print("revisar que el huevo este al gusto")
            huevo_gusto = input("¿El huevo esta al gusto? responde si o no: ")
        if(huevo_gusto == "si"):
            print("Se sirve")
            print("Ponerlo en el plato")
            print("Comer, FIN!!! :)")
        else:
            print("Opcion no valida, recuerda responder 'si' o 'no'")
    
    else:
        print("Opcion no valida, recuerda responder 'si' o 'no'")

elif(huevo == "no"):
    print("Compralo, vuelve inicia el programa")

else:
     print("Opcion no valida, recuerda responder 'si' o 'no'")