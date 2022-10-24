from xml.dom.minidom import Element


print("=================bienvenido a la isla, tu mision sera encontrar el tesoro================")

def elegir_puerta():
    puerta = input("ingrese una puerta roja amarilla o azul: ")
    if(puerta == "amarilla"):
        print("haz ganado, felicidades")
    elif(puerta == "azul"):
        print("haz sido deborado, game over")
    elif(puerta == "roja"):
        print("te haz quemado game over")
    else:
        print("opcion invalida")

    

derecha_izquiera = input("¿derecha o izquiera: ")

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
                eleccion_puerta()
               

            elif(huir == "no"):
                print("estas muerto, Game over")
            else:
                print("Opcion incorrecta")

        elif(sobrevivir=="no"):
            print("Estas muerto, Game over")
        else:
            print("opcion no valida")


    elif(nadar_esperar == "esperar"):

        eleccion_puerta = input("¿cual puerta eliges? solo puedes elegir (roja, azul y amarilla): ")
        if(eleccion_puerta == "amarilla"):
            print("Haz ganado!!!! Felicidades")
        
        elif(eleccion_puerta == "azul"):
            print("Deborado por las bestias, Game over")
        
        elif(eleccion_puerta =="roja"):
            print("Quemado, Game over")

    elif(nadar_esperar == "pensar"):
        idea = input("Tiene una idea: ")
        
        while(idea == "no"):
            idea = input("Tiene una idea: ")

        if(idea == "si"):
            print("Ejecuta rapidamente la idea pirata!!")
            funciono = input("¿Funciono la idea?: ")
            if(funciono == "si"):
                print("elige una puerta: ")
            elif(funciono == "no"):
                print("Haz sido deborado por las malas decisiones")
        
        else:
            print("opcion no valida")
        


        


    else:
        print("opcion no valida")




else:
    print("opcion no valida")





