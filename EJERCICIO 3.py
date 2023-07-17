#se realizo el ejercicio 3 del taller final con el metodo adicional de mostrar boleto en pantalla
import random

vuelos = [ "vuelo1", "vuelo2", "vuelo3", "vuelo4", "vuelo5", "vuelo6", "vuelo7", "vuelo8", "vuelo9", "vuelo10", "vuelo11", "vuelo12", "vuelo13", "vuelo14", "vuelo15", "vuelo16", "vuelo17", "vuelo18", "vuelo19", "vuelo20", "vuelo21", "vuelo22", "vuelo23", "vuelo24", "vuelo25", "vuelo26", "vuelo27", "vuelo28", "vuelo29", "vuelo30", "vuelo31", "vuelo32", "vuelo33", "vuelo34", "vuelo35", "vuelo36", "vuelo37", "vuelo38", "vuelo39", "vuelo40", "vuelo41", "vuelo42"]



class vuelo:
  def __init__(self,codigo,aerolinea,aeropuerto_inicio,aeropuerto_destino,fecha,hora_salida,hora_llegada ,asiento,precio):
    self.codigo = codigo
    self.areolinea = aerolinea
    self.aeropuerto_inicio = aeropuerto_inicio
    self.aeropuerto_destino = aeropuerto_destino
    self.fecha = fecha
    self.hora_salida = hora_salida
    self.hora_llegada = hora_llegada
    self.asiento = asiento
    self.precio = precio
   
  
  def mostrardatos_vuelo(self):
    
    print("Codigo del vuelo: ", +self.codigo)
    print("Aerolinea: ", +self.aerolinea)
    print("Aeropuerto de inicio: ", +self.aeropuerto_inicio)
    print("Aeropuerto de destino: ", +self.aeropuerto_destino)
    print("Fecha del vuelo: ", +self.fecha)
    print("Hora de salida: ", +self.hora_salida)
    print("Hora de llegada: ", +self.hora_llegada)
    print("Fecha del vuelo: ", +self.fecha)
    print("precio: $", +self.precio)


    

class reserva(vuelo):
  def __init__(self,codigo,aerolinea,aeropuerto_inicio,aeropuerto_destino,fecha,hora_salida,hora_llegada ,asiento,precio): 
    super().__init__(codigo,aerolinea,aeropuerto_inicio,aeropuerto_destino,fecha,hora_salida,hora_llegada ,asiento,precio)  

  def buscar_vuelos(self):
    seleccion = "a"
    print("Por favor introduce el dia de salida el vuelo para la siguiente semana del mes de julio: (17-23)")
    self.fecha = int(input())
    print("Por favor introduce el aeropuerto de salida: (Bogota/Medellin/Bucaramanga)")
    self.aeropuerto_inicio = input()
    print("Por favor introduce el aeropuerto de destino: (Bogota/Medellin/Bucaramanga)")
    self.aeropuerto_destino = input()

    for n in vuelos:
      if ((self.fecha == int(n.fecha)) and (self.aeropuerto_inicio == str(n.aeropuerto_inicio)) and (self.aeropuerto_destino == str(n.aeropuerto_destino))):

        print("Se ha encotrado el vuelo con los siguientes datos: ")
        
        print(" ")
        n.mostrardatos_vuelo()

        print(" ")
        print("Desea efectuar el pago y continuar con la reserva del vuelo? ", "por favor, introduzca: (si/no)")
        seleccion = str(input())
        if seleccion == "si":
          self.codigo = n.codigo
          self.aerolinea = str(n.areolinea)
          self.hora_salida = str(n.hora_salida)
          self.hora_llegada = str(n.hora_llegada)
          self.precio = int(n.precio)
          print("Se esta procesando el pago.....")
          print("El pago ha sido exitoso ", "para continuar con la reserva por favor introduzca los datos del pasajero: ")
          
        
      





class pasajero:
  def __init__(self,nombre,apellido,numero_documento,telefono,correo):
    self.nombre = nombre
    self.apellido = apellido
    self.numero_documento = numero_documento
    self.telefono = telefono
    self.correo = correo
  
  def ingresardatos_pasajero(self):
    print("Por favor ingrese su nombre: ")
    self.nombre = input()
    print("Por favor ingrese su apellido: ")
    self.apellido = input()
    print("Por favor ingrese su numero de documento: ")
    self.numero_documento = int(input())
    print("Por favor ingrese su numero de telefono: ")
    self.telefono = int(input())
    print("Por favor ingrese su correo electronico: ")
    self.correo = input()


vuelo_reserva = reserva("A1", "ALW", "A", "B", 17, "06:00", "08:00", "a", 85000)

vuelo1 = vuelo("BOME017","Avianca","Bogota","Medellin",17,"12:00","14:00","a",100000)
vuelo2 = vuelo("BOME018","LATAM","Bogota","Medellin",18,"09:30","11:15","a",110000)
vuelo3 = vuelo("BOME019","Wingo","Bogota","Medellin",19,"07:00","08:00","a",130000)
vuelo4 = vuelo("BOME020","Avianca","Bogota","Medellin",20,"12:00","14:00","a",140000)
vuelo5 = vuelo("BOME021","LATAM","Bogota","Medellin",21,"08:40","10:30","a",138000)
vuelo6 = vuelo("BOME022","LATAM","Bogota","Medellin",22,"15:00","16:30","a",112000)
vuelo7 = vuelo("BOME023","Avianca","Bogota","Medellin",23,"16:00","18:00","a",105000)

vuelo8 = vuelo("MEBO017","Avianca","Medellin","Bogota",17,"12:00","14:00","a",100000)
vuelo9 = vuelo("MEBO018","wingo","Medellin","Bogota",18,"09:00","10:30","a",92000)
vuelo10 = vuelo("MEBO019","LATAM","Medellin","Bogota",19,"18:00","20:00","a",99000)
vuelo11 = vuelo("MEBO020","Wingo","Medellin","Bogota",20,"19:00","21:00","a",93000)
vuelo12 = vuelo("MEBO021","Wingo","Medellin","Bogota",21,"20:00","21:30","a",90000)
vuelo13 = vuelo("MEBO022","LATAM","Medellin","Bogota",22,"08:00","09:30","a",87000)
vuelo14 = vuelo("MEBO023","LATAM","Medellin","Bogota",23,"10:00","11:30","a",111000)

vuelo15 = vuelo("MEBU017","Avianca","Medellin","Bucaramanga",17,"06:00","07:00","a",95000)
vuelo16 = vuelo("MEBU018","LATAM","Medellin","Bucaramanga",18,"11:00","12:00","a",88000)
vuelo17 = vuelo("MEBU019","Avianca","Medellin","Bucaramanga",19,"15:00","16:30","a",100000)
vuelo18 = vuelo("MEBU020","LATAM","Medellin","Bucaramanga",20,"16:30","18:00","a",93000)
vuelo19 = vuelo("MEBU021","wingo","Medellin","Bucaramanga",21,"12:00","14:00","a",100000)
vuelo20 = vuelo("MEBU022","Wingo","Medellin","Bucaramanga",22,"09:00","10:00","a",112000)
vuelo21 = vuelo("MEBU023","Wingo","Medellin","Bucaramanga",23,"20:00","21:00","a",110000)

vuelo22 = vuelo("BUME017","Avianca","Bucaramanga","Medellin",17,"10:00","11:00","a",115000)
vuelo23 = vuelo("BUME018","LATAM","Bucaramanga","Medellin",18,"20:00","21:00","a",118000)
vuelo24 = vuelo("BUME019","LATAM","Bucaramanga","Medellin",19,"06:00","08:00","a",82000)
vuelo25 = vuelo("BUME020","Avianca","Bucaramanga","Medellin",20,"09:00","10:30","a",85000)
vuelo26 = vuelo("BUME021","Avianca","Bucaramanga","Medellin",21,"12:00","14:00","a",130000)
vuelo27 = vuelo("BUME022","Avianca","Bucaramanga","Medellin",22,"13:00","14:30","a",140000)
vuelo28 = vuelo("BUME023","LATAM","Bucaramanga","Medellin",23,"08:00","10:00","a",100000)

vuelo29 = vuelo("BUBO017","Avianca","Bucaramanga","Bogota",17,"08:00","10:00","a",100000)
vuelo30 = vuelo("BUBO018","Wingo","Bucaramanga","Bogota",18,"09:00","10:30","a",111000)
vuelo31 = vuelo("BUBO019","LATAM","Bucaramanga","Bogota",19,"12:00","14:00","a",131000)
vuelo32 = vuelo("BUBO020","Avianca","Bucaramanga","Bogota",20,"10:00","11:00","a",120000)
vuelo33 = vuelo("BUBO021","Avianca","Bucaramanga","Bogota",21,"06:00","08:00","a",105000)
vuelo34 = vuelo("BUBO022","Wingo","Bucaramanga","Bogota",22,"19:00","20:30","a",90000)
vuelo35 = vuelo("BUBO023","Wingo","Bucaramanga","Bogota",23,"18:00","20:00","a",91000)

vuelo36 = vuelo("BOBU017","LATAM","Bogota","Bucaramanga",17,"21:00","22:00","a",94000)
vuelo37 = vuelo("BOBU018","Wingo","Bogota","Bucaramanga",18,"22:00","23:00","a",130000)
vuelo38 = vuelo("BOBU019","LATAM","Bogota","Bucaramanga",19,"09:00","10:30","a",115000)
vuelo39 = vuelo("BOBU020","Wingo","Bogota","Bucaramanga",20,"08:00","09:00","a",85000)
vuelo40 = vuelo("BOBU021","Avianca","Bogota","Bucaramanga",21,"14:00","16:00","a",95000)
vuelo41 = vuelo("BOBU022","LATAM","Bogota","Bucaramanga",22,"15:00","16:30","a",98000)
vuelo42 = vuelo("BOBU023","Avianca","Bogota","Bucaramanga",23,"18:00","20:00","a",99000)









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
