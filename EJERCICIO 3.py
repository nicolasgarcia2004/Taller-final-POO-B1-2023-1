#se realizo el ejercicio 3 del taller final con el metodo adicional de mostrar boleto en pantalla
import sys

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
    print(" ")
    print("Codigo del vuelo: ", str(self.codigo))
    print("Aerolinea: ", self.areolinea)
    print("Aeropuerto de inicio: ", self.aeropuerto_inicio)
    print("Aeropuerto de destino: ", self.aeropuerto_destino)
    print("Hora de salida: ", self.hora_salida)
    print("Hora de llegada: ", self.hora_llegada)
    print("Fecha del vuelo: julio ", str(self.fecha), " de 2023")
    print("precio: $", self.precio)
    print(" ")


    

class reserva(vuelo):
  def __init__(self,codigo,aerolinea,aeropuerto_inicio,aeropuerto_destino,fecha,hora_salida,hora_llegada ,asiento,precio): 
    super().__init__(codigo,aerolinea,aeropuerto_inicio,aeropuerto_destino,fecha,hora_salida,hora_llegada ,asiento,precio)  

  def buscar_vuelos(self):
    print(" ")
    seleccion = "a"
    print("Por favor introduce el dia de salida el vuelo para la siguiente semana del mes de julio: (17-23)")
    self.fecha = int(input())
    if self.fecha < 17 or self.fecha > 23:
      print("La fecha introducida no es valida, por favor intente nuevamente")
      sys.exit(105)
    print("Por favor introduce el aeropuerto de salida: (Bogota/Medellin/Bucaramanga)")
    self.aeropuerto_inicio = input()
    print("Por favor introduce el aeropuerto de destino: (Bogota/Medellin/Bucaramanga)")
    self.aeropuerto_destino = input()
    print(" ")
    if self.aeropuerto_inicio == self.aeropuerto_destino:
      print("El aeropuerto de destino no puede ser el mismo que el de salida, por favor intente nuevamente")
      sys.exit(525)

    for n in range(0,42):
      if ((self.fecha == int(vuelos[n].fecha)) and (self.aeropuerto_inicio == vuelos[n].aeropuerto_inicio) and (self.aeropuerto_destino == vuelos[n].aeropuerto_destino)):

        print("Se ha encotrado el vuelo con los siguientes datos: ")
        
        print(" ")
        vuelos[n].mostrardatos_vuelo()

        print(" ")
        print("Desea efectuar el pago y continuar con la reserva del vuelo? ", "por favor, introduzca: (si/no)")
        seleccion = str(input())
        if seleccion == "si":
          self.codigo = vuelos[n].codigo
          self.aerolinea = str(vuelos[n].areolinea)
          self.hora_salida = str(vuelos[n].hora_salida)
          self.hora_llegada = str(vuelos[n].hora_llegada)
          self.precio = int(vuelos[n].precio)
          print("Se esta procesando el pago.....")
          print("El pago ha sido exitoso ", "para continuar con la reserva por favor introduzca los datos del pasajero: ")
        else:
          print("La reserva no ha podido ser efectuada, por favor intente nuevamente después")
          break 
  def gestionar_asientos(self):
    print(" ")
    print("introduzca la fila del asiento: (a,b,c,d)")
    self.asiento = str(input())
    if self.asiento != "a" and self.asiento != "b" and self.asiento != "c" and self.asiento != "d":
      print("La fila introducida no es valida, por favor intente nuevamente")
      sys.exit(205)
    print("introduzca el numero del asiento: (1,15)")
    temp_asiento = str(input())
    if temp_asiento != "1" and temp_asiento != "2" and temp_asiento != "3" and temp_asiento != "4" and temp_asiento != "5" and temp_asiento != "6" and temp_asiento != "7" and temp_asiento != "8" and temp_asiento != "9" and temp_asiento != "10" and temp_asiento != "11" and temp_asiento != "12" and temp_asiento != "13" and temp_asiento != "14" and temp_asiento != "15":
      print("El numero del asiento introducido no es valido, por favor intente nuevamente")
      sys.exit(305)
    self.asiento = self.asiento + temp_asiento
    print("El asiento ha sido asignado correctamente")
    print("El asiento seleccionado es: " +self.asiento)
    print(" ")

          


  def mostrar_boleto(self, passenger):
    print(" ")
    print("El boleto ha sido reservado exitosamente, a continuación podrá ver el boleto del vuelo reservado previamente, recurde llevarlo en digital o impreso al momento del abordaje: ")
    print(" ")
    print("                                         ",str(self.aerolinea),"                                     ")

    print("  Nombre del pasajero: ",str(passenger.nombre),"/",str(passenger.apellido), "          Vuelo: ", str(self.codigo))
    print("  Origen: ",str(self.aeropuerto_inicio), "             Asiento: ",str(self.asiento))
    print("  Destino: ",str(self.aeropuerto_destino),"        Fecha: ", " Julio ",str(self.fecha), " de 2023")
    print("  Hora de salida:", self.hora_salida,"     Hora de llegada:", self.hora_llegada)
    print("  ║▌║█║▌│║▌║▌█║▌║█║▌│║▌║▌█║▌║█║▌│║▌║▌█║▌║█║▌│║▌║▌█║▌║█║▌│║▌║▌█║▌║█║▌│║▌║▌█║▌║█║▌│║▌║▌█║▌║█║▌│║▌║▌█║▌║█║▌")
    print("")





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
pasajero1 = pasajero("A", "B", 123, 123,"@mail" )



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


vuelos = [ vuelo1, vuelo2, vuelo3, vuelo4, vuelo5, vuelo6, vuelo7, vuelo8, vuelo9, vuelo10, vuelo11, vuelo12, vuelo13, vuelo14, vuelo15, vuelo16, vuelo17, vuelo18, vuelo19, vuelo20, vuelo21, vuelo22, vuelo23, vuelo24, vuelo25, vuelo26, vuelo27, vuelo28, vuelo29, vuelo30, vuelo31, vuelo32, vuelo33, vuelo34, vuelo35, vuelo36, vuelo37, vuelo38, vuelo39, vuelo40, vuelo41, vuelo42]


print("Bienvenido a la agencia de viajes FindMyflightNow.com, desea buscar un vuelo?, por favor introduzca: (si/no)")
opcion_vuelo = str(input())
if opcion_vuelo == "si":
  vuelo_reserva.buscar_vuelos()
  pasajero1.ingresardatos_pasajero()
  print("A continución podrá seleccionar su asiento:")
  vuelo_reserva.gestionar_asientos()
  vuelo_reserva.mostrar_boleto(pasajero1)
  print("Gracias por comprar su vuelo con nosotros, esperamos que disfrute su viaje")
else:
  print("Gracias por visitar nuestra plataforma de busqueda de vuelos, esperamos poder servirle en otra ocasión")
