import random


class JuegoAventura:

  def __init__(self):
  
    self.actual = 0
    
  def iniciar_juego(self):
    print("¡Bienvenido a Marte !!!")
    
    while self.actual != -1:
      self.mostrar_situacion()
      self.tomar_decision()

  def mostrar_situacion(self):
    if self.actual  == 0:
      print("ESTÁS EN UN CAMINO MUY EXTRAÑO, DECIDE SI IR AL ESTE O AL OESTE \n")
    
      print("¿Qué quieres hacer? \n")

    
    elif self.actual == 1:
      print("\nTE HAS ENCONTRADO CON UN PERRO MUTANTE DE 8 CABEZAS Y TE QUIERE HACER UNA FATALITY \n")

    elif self.actual == 2:
      print("UNA TRIBU ALIENÍGENA DE UMPALUMGAS INTERGALÁCTICOS DE QUIEREN RAPTAR Y CRUCIFICAR \n")

    elif self.actual == 3:
        print("TE HAS ENCONTRADO UN RÍO \n")


    elif self.actual == 4:
        print("HAS ENCONTRADO UNA CUEVA EXTRAÑA \n")

    elif self.actual == 5:
        print("HAS ENCONTRADO 5 CAMINOS DISTINTOS\n")
      
      
      
      

  def tomar_decision(self):

    if self.actual  == 0:
      decision = input("iNGRESA 1 PARA IR AL ESTE, Y 2 PARA IR AL OESTE \n")
      if(decision == "1"):
        print("HAZ CAÍDO EN UN KRATER MUY PORFUNDO, MORISTE... :´( ")
        self.actual = -1
      elif decision == "2":
          self.actual = self.actual + 1

    
    elif self.actual == 1:
        decision = input("Si quieres atacarlo con una roca selecciona 1, si quieres correr selecciona 2 \n")
        if decision == "2":
          print("EL PERRO ES MUY RÁPIDO Y TE HA ALCANZADO, AHORA ERES PUROS HUESOS PARA PERRO! \n")
          self.actual = -1
        elif decision == "1":
          print("MUY BIEN, LO HAS MATADO, AHORA TIENES COMIDA \n")
          self.actual = self.actual + 1

    elif self.actual == 2:
        decision = input("Si quieres pelear selecciona 1 \n"
                          "Si quieres correr rendirte selecciona 2 \n"
                          "Si quieres huir selecciona 3")
        if(decision == "1"):
            print("HAY DEMASIADOS UMPALUMPA, TE MOLIERON !!! \n")
            self.actual = -1
        elif(decision == "2"):
            print("TE HAN SOMETIDO Y CRUCIFICADO !!! \n")
            self.actual = -1
        elif(decision == "3"):
            print("HAS ESCAPADO, ERES MUY SUERTUDO :) \n") 
            self.actual = self.actual +1

    elif self.actual == 3:
        decision = input("Si quieres pasarlo para ahorrar tiempo, selecciona 1 \n"
                  "Si quieres rodearlo selecciona 2 \n")
        if(decision == "1"):
            print("EL RÍO ES DE UN COMPUESTO ÁCIDO, TE HAS DERRETIDO...           x( ) \n")
            self.actual = -1
        elif(decision == "2"):
            self.actual = self.actual +1 

    elif self.actual == 4:
        decision = input("HAY 3 PUERTAS \n"
                                    "Si quieres ir por la primera, selecciona 1 \n"
                                    "Si quieres ir por la segunda, selecciona 2 \n"
                                    "Si quieres ir por la tercera, selecciona 3 \n")
        if decision == "1":
            print("TE HAS ENCONTRADO UN OSO ALIENÍGENA Y TE HA COMIDO ! \n")
            self.actual = -1  
        elif decision == "2":
            pass
        elif decision == "3":
            self.actual  = self.actual + 1
            
    elif self.actual == 5:
        decision = input("Si quieres ir por camino color rojo, selecciona 1\n"
                                          "Si quieres ir por el camino azul, selecciona 2\n"
                                          "Si quieres ir por el camino verde, selecciona 3\n"
                                          "Si quieres ir por cualquier otro de los dos caminos selecciona 4 \n")
        if decision == "1":
            print("TE HAS CAÍDO EN UN HUECO QUE LLEGA AL EPICENTRO DE MARTE, TE PULVERIZASTE... \n")
            self.actual = -1
        elif decision == "2":
            print("TE ENCONTRASTE CON MURCIÉLAGOS ASESINOS, MORISTE... !!! \n")
            self.actual = -1
        elif decision == "3":
            print("FELICIDADES !!! TE ENCONTRASTE CON UNA BASE DE INGENIÉROS DE SPACE X\n"
                                  "CON ELLOS ESTABA ELON MUSK :) \n")
            self.actual = -1
        else:
              print("TE TROPESASTE Y TE GOLPEASTE LA CABEZA, HAS MUERTO!!! \n")
              self.actual = -1



if __name__ == "__main__":
  juego = JuegoAventura()
  juego.iniciar_juego()