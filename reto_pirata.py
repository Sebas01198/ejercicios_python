from xml.dom.minidom import Element


print("=================bienvenido a la isla, tu mision sera encontrar el tesoro================")

#funciones
def elegir_puerta():
    puerta = input("¿cual puerta eliges? solo puedes elegir (roja, azul y amarilla):")
    if(puerta == "amarilla"):
        print("haz ganado, felicidades")
    elif(puerta == "azul"):
        print("haz sido deborado, game over")
    elif(puerta == "roja"):
        print("te haz quemado game over")
    else:
        print("opcion invalida")

    

derecha_izquiera = input("¿derecha o izquiera?: ")

if(derecha_izquiera == "derecha"):
    print("Caiste en el agujero Game over")

elif(derecha_izquiera =="izquierda"):
    nadar_esperar = input("¿nadar, esperar o pensar ?: ")

    if(nadar_esperar == "nadar"):
        print("Atacado por una tribu")

        sobrevivir = input("¿Sobrevivio al ataque?")
        if(sobrevivir =="si"):

            huir = input("¿pudiste huir?")
            if(huir == "si"):
                print("corre y elige una puerta")
                elegir_puerta()
               

            elif(huir == "no"):
                print("estas muerto, Game over")
            else:
                print("Opcion incorrecta")

        elif(sobrevivir=="no"):
            print("Estas muerto, Game over")
        else:
            print("opcion no valida")


    elif(nadar_esperar == "esperar"):

            elegir_puerta()

    elif(nadar_esperar == "pensar"):
        idea = input("Tiene una idea: ")
        
        while(idea == "no"):
            print("Piensa rapido o moriras")
            idea = input("Tiene una idea: ")
            

        if(idea == "si"):
            print("Ejecuta rapidamente la idea pirata!!")
            funciono = input("¿Funciono la idea?: ")
            if(funciono == "si"):
                elegir_puerta()
            elif(funciono == "no"):
                print("Haz sido deborado por las malas decisiones")
        
        else:
            print("opcion no valida")
    


    else:
        print("opcion no valida")


else:
    print("opcion no valida")





