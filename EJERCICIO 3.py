
import random



class vuelo:
  def __init__(self,codigo,aerolinea,aeropuerto_inicio,aeropuerto_destino,puntos_bloqueo):
    self.codigo = codigo
    self.puntos_vida = puntos_vida
    self.nivel = nivel
    self.experiencia_del_nivel = experiencia_del_nivel
    self.defensa = defensa
    self.puntos_bloqueo = puntos_bloqueo
    
    
   
  def adquirir_experiencia(self):
    print(self.nombre+ " Comienza a entrenar para obtener experiencia....")
    self.experiencia_del_nivel = int(self.experiencia_del_nivel)
    self.experiencia_del_nivel = int(self.experiencia_del_nivel + 50)
    print("con el entrenamiento se han ganado 50 puntos de experiencia")
  def subir_nivel(self):
    self.nivel = int(self.nivel)
    if self.experiencia_del_nivel == 100:
      self.nivel = self.nivel + 1
      self.puntos_vida = int(self.puntos_vida)
      self.puntos_vida = int(self.puntos_vida + 20)
      print( self.nombre+" ha subido de nivel, el nuevo nivel es: " +str(self.nivel), "y se ha aumentado en 20 los puntos de vida")
      print( self.nombre+" ahora tiene " +str(self.puntos_vida))

  def asignar_nombre(self):
    print("Por favor ingrese el nombre del jugador: ")
    self.nombre = input()

  def recibir_daño(self,valor_ataque):
    
    if self.defensa == 1:
      valor_ataque = valor_ataque - self.puntos_bloqueo
      self.defensa = int(0)
      self.puntos_bloqueo = int(0)
    else:
      valor_ataque = valor_ataque
    self.puntos_vida = int(self.puntos_vida - valor_ataque)
    

class Arma:
  def __init__(self,nombre_arma,elemento_arma,nivel_arma,daño_arma,dueño_arma):     
    self.nombre_arma = nombre_arma
    self.elemento_arma = elemento_arma
    self.nivel_arma = nivel_arma
    self.daño_arma = daño_arma
    self.dueño_arma = dueño_arma

  def atacar(self):
    pass

  def defenderse(self):
    pass
    
  def afilar_arma(self):

    print( self.dueño_arma+ " va a afilar su arma con la piedra de obsidiana del monte chrui...")
    self.daño_arma = int(self.daño_arma)
    self.daño_arma = int(self.daño_arma + 15)
    print("Se ha afilado el arma exitosamente! , el daño del arma se ha incrementado en 15 puntos de daño", )

class Arma_toxica(Arma):
  def __init__(self,nombre_arma,elemento_arma,nivel_arma,daño_arma,dueño_arma): 
    self.puntos_bloqueo = 7
    self.probabilidad_bloqueo = "50%"
    super().__init__(nombre_arma,elemento_arma,nivel_arma,daño_arma, dueño_arma)  

  def atacar(self,objetivo):
    valor_ataque = int(0)
    self.daño_arma = int(self.daño_arma)
    print(self.dueño_arma+ " ha ejecutado el ataque explosión venenosa")
    print("Este ataque causa:"  +str(self.daño_arma), "puntos de daño")
    valor_ataque = self.daño_arma
    personaje.recibir_daño(objetivo,valor_ataque)
    
    
  def defenderse(self,defendido):
    print( self.dueño_arma+ " intentará efectuar la defensa anticipada en caso de ataque en el proximo turno del rival...")
    
    aleatorio = random.randint(1, 3)
    if aleatorio == 1:
      defendido.defensa = int(1)
      defendido.puntos_bloqueo = int(7)
      print("La defensa ha sido exitosa")
    else:
      defendido.defensa = int(0)
      print("La defensa ha fracasado")



class Arma_hielo(Arma):
  def __init__(self,nombre_arma,elemento_arma,nivel_arma,daño_arma,dueño_arma): 
    self.puntos_bloqueo = 12
    self.probabilidad_bloqueo = "33.3%"
    super().__init__(nombre_arma,elemento_arma,nivel_arma,daño_arma,dueño_arma)  

  def atacar(self,objetivo):
    valor_ataque = int(0)
    self.daño_arma = int(self.daño_arma)
    print( self.dueño_arma+" ha ejecutado el ataque congelación profunda")
    print("Este ataque causa:"  +str(self.daño_arma), "puntos de daño")
    valor_ataque = self.daño_arma
    personaje.recibir_daño(objetivo,valor_ataque)
    
    
  def defenderse(self,defendido):
    print( self.dueño_arma+ " intentará efectuar la defensa anticipada en caso de ataque en el proximo turno del rival...")
    
    aleatorio = random.randint(1, 4)
    if aleatorio == 2:
      defendido.defensa = int(1)
      defendido.puntos_bloqueo = int(12)
      print("La defensa ha sido exitosa")
    else:
      defendido.defensa = int(0)
      print("La defensa ha fracasado")

class Arma_fuego(Arma):
  def __init__(self,nombre_arma,elemento_arma,nivel_arma,daño_arma,dueño_arma): 
    self.puntos_bloqueo = 14
    self.probabilidad_bloqueo = "25%"
    super().__init__(nombre_arma,elemento_arma,nivel_arma,daño_arma,dueño_arma)  

  def atacar(self,objetivo):
    valor_ataque = int(0)
    self.daño_arma = int(self.daño_arma)
    print( self.dueño_arma+" ha ejecutado el ataque onda ignea")
    print("Este ataque causa:"  +str(self.daño_arma), "puntos de daño")
    valor_ataque = self.daño_arma
    personaje.recibir_daño(objetivo,valor_ataque)
    
    
  def defenderse(self,defendido):
    print( self.dueño_arma+" intentará efectuar la defensa anticipada en caso de ataque en el proximo turno del rival...")
    
    aleatorio = random.randint(1, 5)
    if aleatorio == 2:
      defendido.defensa = int(1)
      defendido.puntos_bloqueo = int(14)
      print("La defensa ha sido exitosa")
    else:
      defendido.defensa = int(0)
      print("La defensa ha fracasado")


jugador = personaje("a",100,1,0,0,0)
rival = personaje("Jiron el destructor",100,1,0,0,0)
arma1 = Arma_toxica("Daga del veneno","toxicidad",1,20,"b")
arma2 = Arma_hielo("Hacha de la ventisca","hielo",1,24,"b")
arma3 = Arma_fuego("Espada del inframundo","fuego",1,28,"b")


def seleccion_movimiento():
  print("Que deseas hacer? ,introduce alguna de las siguientes opciones: atacar/defenderse/adquirir experiencia/afilar arma")
  opcion = input()
  if opcion == "atacar":
    arma_seleccionada.atacar(rival)
  if opcion == "defenderse":
    arma_seleccionada.defenderse(jugador)
  if opcion == "adquirir experiencia":
    jugador.adquirir_experiencia()
    jugador.subir_nivel()
  if opcion == "afilar arma":
    arma_seleccionada.afilar_arma()
  
def seleccion_rival():
  opcion_rival = random.randint(1, 5)
  if opcion_rival == 1:
    arma_rival.atacar(jugador)
  if opcion_rival == 2:
    arma_rival.defenderse(rival)
  if opcion_rival == 3:
    rival.adquirir_experiencia()
    rival.subir_nivel()
  if opcion_rival == 4:
    arma_rival.afilar_arma()



print("Bienvenido a La Guerra de los elementos, a continuacion elige el nombre de tu personaje:")
print(" ")
personaje.asignar_nombre(jugador)
print("Las siguientes armas estan disponibles en el reino de Hillowrik:")
print(" ")
print("Arma1:","Nombre del arma: "+arma1.nombre_arma)
print("Elemento del arma: "+arma1.elemento_arma)
print("El daño del arma es: "+str(arma1.daño_arma))
print("la probabilidad de bloqueo del arma es: "+str(arma1.probabilidad_bloqueo))
print("Los puntos de bloqueo del arma son: 7")
print(" ")
print("Arma2:","Nombre del arma: "+arma2.nombre_arma)
print("Elemento del arma: "+arma2.elemento_arma)
print("El daño del arma es: "+str(arma2.daño_arma))
print("la probabilidad de bloqueo del arma es: "+str(arma2.probabilidad_bloqueo))
print("Los puntos de bloqueo del arma son: 12")
print(" ")
print("Arma3:","Nombre del arma: "+arma3.nombre_arma)
print("Elemento del arma: "+arma3.elemento_arma)
print("El daño del arma es: "+str(arma3.daño_arma))
print("la probabilidad de bloqueo del arma es: "+str(arma3.probabilidad_bloqueo))
print("Los puntos de bloqueo del arma son: 14")
print(" ")
print("Por favor introduce alguna de las siguientes opciones para elegir un arma: arma1/arma2/arma3")
seleccion = input()
if seleccion == "arma1":
  arma_seleccionada = Arma_toxica("Daga del veneno","toxicidad",1,20,"b")
if seleccion == "arma2":
  arma_seleccionada = Arma_hielo("Hacha de la ventisca","hielo",1,22,"b")
if seleccion == "arma3":
  arma_seleccionada = Arma_fuego("Espada del inframundo","fuego",1,28,"b")

arma_rival = Arma_fuego("Espada del inframundo","fuego",1,28,"b")
arma_rival.dueño_arma = rival.nombre

arma_seleccionada.dueño_arma = jugador.nombre

print(" Has seleccionado: "+str(arma_seleccionada.nombre_arma))

print("El jugador: "+jugador.nombre, "se enfrentará al rey de los Orcos:" +rival.nombre)

print(" " +rival.nombre, " ha adquirirdo el arma: " +arma_rival.nombre_arma)

while jugador.puntos_vida >= 0 or rival.puntos_vida >= 0:
  print(" ")
  seleccion_movimiento()
  print(" ")
  if jugador.puntos_vida <= 0 or rival.puntos_vida <= 0:
    break
  seleccion_rival()
  print(" ")
  print(jugador.nombre, " puntos de vida: ", str(jugador.puntos_vida))
  print(rival.nombre, " puntos de vida: ", str(rival.puntos_vida))
    
if jugador.puntos_vida <= 0:
  print("El jugador: " +jugador.nombre, " ha perdido")

if rival.puntos_vida <= 0:
  print("El jugador: " +jugador.nombre, " ha vencido a: " +rival.nombre)
