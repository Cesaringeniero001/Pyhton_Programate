print("BIENVENIDO A MARTE, ESTE ES UN LUGAR MUY HOSTIL !!!")
print("")
print("VAS A TENER QUE ADENTRARTE EN ESTE PLANETA PARA ENCONTRAR \n"
      "UN LUGAR EN EL QUE PUEDAS INSTALARTE Y ESTÁR A SALVO PARA \n"
      "UNA NUEVA VIDA...  ")
print("")
print("MUCHA SUERTE HUMANO !!!")
print("\n\n")

print("ESTÁS EN UN CAMINO MUY EXTRAÑO, DECIDE SI IR AL ESTE O AL OESTE")
def validacion_2opciones(decision):
    while((type(decision)!=str) or (decision != "1" and decision != "2")):
       decision = input("INGRESA UN VALOR VÁLIDO")

def validacion_3opciones(decision):
    while((type(decision)!=str) or (decision != "1" and decision != "2" and decision != "3")):
        decision = input("INGRESA UN VALOR VÁLIDO")
def validacion_4opciones(decision):
    while((type(decision)!=str) or (decision != "1" and decision != "2" and decision != "3" and decision != "4")):
        decision = input("INGRESA UN VALOR VÁLIDO")        

    
        

eleccion1 = input("iNGRESA 1 PARA IR AL ESTE, Y 2 PARA IR AL OESTE\n"
                  "Nota: Suponemos que sabemos donde es el este y el oeste jeje")


validacion_2opciones(eleccion1)

if(eleccion1 == "1"):
    print("HAZ CAÍDO EN UN KRATER MUY PORFUNDO, MORISTE... :´( ")
elif(eleccion1 == "2"):
    print("\nTE HAS ENCONTRADO CON UN PERRO MUTANTE DE 8 CABEZAS Y TE QUIERE HACER UNA FATALITY ")
    print("\n\n")
    eleccion2 = input("Si quieres atacarlo con una roca selecciona 1, si quieres correr selecciona 2")
    validacion_2opciones(eleccion2)
    if(eleccion2 == "1"):
        print("MUY BIEN, LO HAS MATADO, AHORA TIENES COMIDA :)")
        print("\n\n")
        eleccion3 = input("UNA TRIBU ALIENÍGENA DE UMPALUMGAS INTERGALÁCTICOS DE QUIEREN RAPTAR Y CRUCIFICAR \n\n"
                          "Si quieres pelear selecciona 1 \n"
                          "Si quieres correr rendirte selecciona 2 \n"
                          "Si quieres huir selecciona 3")
        validacion_3opciones(eleccion3)
        if(eleccion3 == "1"):
            print("HAY DEMASIADOS UMPALUMPA, TE MOLIERON !!!")
        elif(eleccion3 == "2"):
            print("TE HAN SOMETIDO Y CRUCIFICADO !!!")
        elif(eleccion3 == "3"):
            print("HAS ESCAPADO, ERES MUY SUERTUDO :)")
            print("\n\n")
            eleccion4 = input("TE HAS ENCONTRADO UN RÍO \n"
                  "Si quieres pasarlo para ahorrar tiempo, selecciona 1 \n"
                  "Si quieres rodearlo selecciona 2")
            validacion_2opciones(eleccion4)
            if(eleccion4 == "1"):
                print("EL RÍO ES DE UN COMPUESTO ÁCIDO, TE HAS DERRETIDO... x( )")
            else:
                print("HAS ENCONTRADO UNA CUEVA EXTRAÑA")
                print("\n\n")
                eleccion55 = "2"
                conteo_retornos = 0
                while(eleccion55 == "2"):
                    if(conteo_retornos == 0):
                        eleccion5 = input("HAY 3 PUERTAS \n"
                                    "Si quieres ir por la primera, selecciona 1 \n"
                                    "Si quieres ir por la segunda, selecciona 2 \n"
                                    "Si quieres ir por la tercera, selecciona 3")
                        validacion_3opciones(eleccion5)
                    elif(conteo_retornos > 0):
                        eleccion5 = input("\n\nHAS VUELTO A LA ENTRADA DE LA CASS, ESCOGE OTRO CAMINO")
                        validacion_3opciones(eleccion5)
                    
                    if(eleccion5 == "1"):
                        print("\n\n")
                        eleccion55 = "np"
                        print("TE HAS ENCONTRADO UN OSO ALIENÍGENA Y TE HA COMIDO !")
                    elif(eleccion5 == "2"):
                        print("\n\n")
                        eleccion55 = input("ENCONTRASTE OTROS 2 CAMINOS \n"
                                    "Si quieres ir por la izquieda seleccion 1 \n"
                                    "Si quieres ir por la derecha selecciona 2")
                        validacion_2opciones(eleccion55)
                        if(eleccion55 == "2"):
                            conteo_retornos +=1
                        elif(eleccion55 == "1"):
                            print("TE HAS ENCONTRADO UNA ARAÑA GALÁCTICA, TE PICÓ Y TE CONVERTISTE EN EL HOMBRE ARAÑA xO\n"
                                   "LASTIMOSAMENTE MORISTE AL OTRO DÍA, PORQUE PORQUE NO AGUANTASTE EL VENENO")    
                        
                
                    elif(eleccion5 == "3"):
                        print("\n\n")
                        eleccion55 = "np"
                        print("HAS ENCONTRADO 5 CAMINOS DISTINTOS\n")
                        eleccion6 = input("Si quieres ir por camino color rojo, selecciona 1\n"
                                          "Si quieres ir por el camino azul, selecciona 2\n"
                                          "Si quieres ir por el camino verde, selecciona 3\n"
                                          "Si quieres ir por cualquier otro de los dos caminos selecciona 4")
                        validacion_4opciones(eleccion6)

                        if(eleccion6 == "1"):
                            print("TE HAS CAÍDO EN UN HUECO QUE LLEGA AL EPICENTRO DE MARTE, TE PULVERIZASTE...")
                        elif(eleccion6 == "2"):
                            print("TE ENCONTRASTE CON MURCIÉLAGOS ASESINOS, MORISTE... !!!")
                        elif(eleccion6 == "3"):
                            print("FELICIDADES !!! TE ENCONTRASTE CON UNA BASE DE INGENIÉROS DE SPACE X\n"
                                  "CON ELLOS ESTABA ELON MUSK :)")
                        else:
                            print("TE TROPESASTE Y TE GOLPEASTE LA CABEZA, HAS MUERTO!!!")
                
    else:
        print("EL PERRO ES MUY RÁPIDO Y TE HA ALCANZADO, AHORA ERES PUROS HUESOS PARA PERRO!")
