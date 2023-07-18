#se realizo el ejercicio 9 del taller final con el metodo adicional de ver invitación en en pantalla
import sys

vuelos = [ "vuelo1", "vuelo2", "vuelo3", "vuelo4", "vuelo5", "vuelo6", "vuelo7", "vuelo8", "vuelo9", "vuelo10", "vuelo11", "vuelo12", "vuelo13", "vuelo14", "vuelo15", "vuelo16", "vuelo17", "vuelo18", "vuelo19", "vuelo20", "vuelo21", "vuelo22", "vuelo23", "vuelo24", "vuelo25", "vuelo26", "vuelo27", "vuelo28", "vuelo29", "vuelo30", "vuelo31", "vuelo32", "vuelo33", "vuelo34", "vuelo35", "vuelo36", "vuelo37", "vuelo38", "vuelo39", "vuelo40", "vuelo41", "vuelo42"]

participantes = []


class evento:
  def __init__(self,tipo_evento,cantidad_participantes,ciudad,precio,fecha,hora):
    self.tipo_evento = tipo_evento
    self.cantidad_participantes = cantidad_participantes
    self.ciudad = ciudad
    self.precio = precio
    self.fecha = fecha
    self.hora = hora
  

  def crear_evento(self):
    print(" ")
    print("A continuación podrá crear un evento: ")
    seleccion = "a"
    print("Por favor introduce el tipo de evento: (Boda/Quinceaños/Graduación)")
    self.tipo_evento = str(input())
    print("Por favor introduce la cantidad de participantes del evento: (1-25)")
    self.cantidad_participantes = int(input())
    if self.cantidad_participantes < 1 or self.cantidad_participantes > 25:
      print("La cantidad de participantes introducida no es valida, por favor intente nuevamente")
      sys.exit(105)
    print("Por favor introduce la ciudad en la que tendrá lugar el evento: (Bogota/Medellin/Bucaramanga)")
    self.ciudad = str(input())
    print("Por favor introduce la fecha del evento: (dia/mes/año)")
    self.fecha = str(input())
    print("Por favor introduce la hora del evento: (hora:minutos)")
    self.hora = str(input())

    if self.tipo_evento == "Boda":
      self.precio = int(50000*self.cantidad_participantes)
    if self.tipo_evento == "Quinceaños":
      self.precio = int(43000*self.cantidad_participantes)
    if self.tipo_evento == "Graduacion":
      self.precio = int(37000*self.cantidad_participantes)

    print("El precio del evento es: ", self.precio)
    print(" ")
    print("Desea crear el evento? ", "por favor, introduzca: (si/no)")
    seleccion = str(input())
    if seleccion == "si":
      print("El evento ha sido creado exitosamente")
    if seleccion == "no":
      print("El evento no ha sido creado, por favor intente nuevamente más tarde")
      sys.exit(101)
  def gestionar_logistica(self):
    seleccion_logistica1 = "a"
    seleccion_logistica2 = "a"
    valoralquiler_salon = int(0)
    valoralquiler_sillasymesas = int(0)
    valoralquiler_sonido = int(0)
    valor_comidaybebida = int(0)
    valor_meserosypersonal = int(0)

    print("Estos son los datos del evento que se ha creado:")
    print(" ")
    print("Tipo de evento: ", self.tipo_evento)
    print("Cantidad de participantes: ", str(self.cantidad_participantes))
    print("Ciudad: ", self.ciudad)
    print("Precio: ", str(self.precio))
    print(" ")
    print("El evento tiene los siguientes articipantes:")
    for n in range(0,self.cantidad_participantes):
      print("Participante: ", n+1)
      print("Nombre: ", participantes[n].nombre)
      print("Apellido: ", participantes[n].apellido)
      print("Numero de documento: ", str(participantes[n].numero_documento))
      print("Telefono: ", str(participantes[n].telefono))
      print("Correo electronico: ", participantes[n].correo)
      print(" ")
    print("Si los datos son correctos y desea proceder con la logistica del evento por favor introduzca: (si/no)")
    seleccion_logistica1 = str(input())
    if seleccion_logistica1 == "si":
      valoralquiler_salon = int(0.40 * self.precio)
      valoralquiler_sillasymesas = int(0.10 * self.precio)
      valoralquiler_sonido = int(0.10 * self.precio)
      valor_comidaybebida = int(0.20 * self.precio)
      valor_meserosypersonal = int(0.20 * self.precio)
      print("El valor del alquiler del salon es: $", str(valoralquiler_salon), "y sera gestionado con ABCEventsrooms")
      print("El valor del alquiler de sillas y mesas es: $", str(valoralquiler_sillasymesas), "y sera gestionado con FableyEventsfurniture")
      print("El valor del alquiler del sonido es: $", str(valoralquiler_sonido), "y sera gestionado con XSFSuperSound")
      print("El valor de la comida y bebida es: $", str(valor_comidaybebida), "y sera gestionado con FoodandDrinksIlowra")
      print("El valor de los meseros y personal es: $", str(valor_meserosypersonal), "y sera gestionado con Silverstaff")
      print(" ")
      print("Desea enviar las respectivas ordenes de compra a los proveedores y gestionar la logistica del evento? ", "por favor, introduzca: (si/no)")
      seleccion_logistica2 = str(input())
      if seleccion_logistica2 == "si":
        print("Las ordenes de compra han sido enviadas exitosamente,los proveedores se contactaran para ultimar detalles")
        print("La logistica del evento ha sido gestionada exitosamente")
      if seleccion_logistica2 == "no":
        print("No se ha gestionado la logistica del evento, por favor intente nuevamente más tarde")
        sys.exit(132)
      

class participante:
  def __init__(self,nombre,apellido,numero_documento,telefono,correo):
    self.nombre = nombre
    self.apellido = apellido
    self.numero_documento = numero_documento
    self.telefono = telefono
    self.correo = correo

  def ingresardatos_participante(self):
    print("Por favor ingrese el nombre del participante: ")
    self.nombre = input()
    print("Por favor ingrese el apellido: ")
    self.apellido = input()
    print("Por favor ingrese el numero de documento: ")
    self.numero_documento = int(input())
    print("Por favor ingrese el numero de telefono: ")
    self.telefono = int(input())
    print("Por favor ingrese el correo electronico: ")
    self.correo = input()
  
class notificacion(participante,evento):
  def __init__(self,nombre,apellido,numero_documento,telefono,correo): 
    super().__init__(nombre,apellido,numero_documento,telefono,correo)

  def enviar_notificacion(self,participante,evento):
    print(" ")
    print("Se ha enviado una notificación al correo: ", str(participante.correo), "y al celular: ", str(participante.telefono))
    print(" ")
    print("La notificación dice el siguiente mensaje: ")
    print("Estimado: ", str(participante.nombre), " ", str(participante.apellido))
    print(" ")
    print("Usted ha sido invitado al evento: ", str(evento.tipo_evento))
    print(" ")
    print("El evento se llevará a cabo en la ciudad de: ", str(evento.ciudad))
    print(" ")
    print("La fecha del evento es: ", "Julio ", str(evento.fecha), " de 2023")
    print("La hora del evento es: ", str(evento.hora))
    print(" ")

  def mostrar_invitaciondigital(self,evento):
    print("La invitación digital generada para el evento es la siguiente: ")
    print(" ")
    print(" ")
    print(" ")
    print("✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧")
    print("        <................................................................................>")
    print("Es un honor para mi anunciar e invitar a todos mis amigos y familiares a mi " )
    print(" ")
    print("Estoy seguro/a que será un dia inolvidable y espero cuente con tu presencia: ", str(evento.ciudad))
    print("Ciudad: ", str(evento.ciudad))
    print("Fecha: ",  str(evento.fecha))
    print("Hora: ", str(evento.hora))
    print(" ")
    print("                             ♡ ♥ ❤♡ ♥ ❤♡ ♥ ❤                          ")
    print("                             ♕ ♛♕ ♛♕ ♛♕ ♛♕                        ")
    print("✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧")

evento1 = evento("A", 123, "A", 123, "01/01/2001", "01:01")

participante1 = participante("A", "B", 123, 123,"@mail" )
participante2 = participante("A", "B", 123, 123,"@mail" )
participante3 = participante("A", "B", 123, 123,"@mail" )
participante4 = participante("A", "B", 123, 123,"@mail" )
participante5 = participante("A", "B", 123, 123,"@mail" )
participante6 = participante("A", "B", 123, 123,"@mail" )
participante7 = participante("A", "B", 123, 123,"@mail" )
participante8 = participante("A", "B", 123, 123,"@mail" )
participante9 = participante("A", "B", 123, 123,"@mail" )
participante10 = participante("A", "B", 123, 123,"@mail" )
participante11 = participante("A", "B", 123, 123,"@mail" )
participante12 = participante("A", "B", 123, 123,"@mail" )
participante13 = participante("A", "B", 123, 123,"@mail" )
participante14 = participante("A", "B", 123, 123,"@mail" )
participante15 = participante("A", "B", 123, 123,"@mail" )
participante16 = participante("A", "B", 123, 123,"@mail" )
participante17 = participante("A", "B", 123, 123,"@mail" )
participante18 = participante("A", "B", 123, 123,"@mail" )
participante19 = participante("A", "B", 123, 123,"@mail" )
participante20 = participante("A", "B", 123, 123,"@mail" )
participante21 = participante("A", "B", 123, 123,"@mail" )
participante22 = participante("A", "B", 123, 123,"@mail" )
participante23 = participante("A", "B", 123, 123,"@mail" )
participante24 = participante("A", "B", 123, 123,"@mail" )
participante25 = participante("A", "B", 123, 123,"@mail" )

participantes = [participante1, participante2, participante3, participante4, participante5, participante6, participante7, participante8, participante9, participante10, participante11, participante12, participante13, participante14, participante15, participante16, participante17, participante18, participante19, participante20, participante21, participante22, participante23, participante24, participante25]

print("Bienvenido al software de eventosPLus34 , por favor introduzca: (si/no)")
opcion_evento = str(input())
if opcion_evento == "si":
  evento1.crear_evento()
  print("A continuación podrá registrar los participantes del evento: ")
  for n in range(0,evento1.cantidad_participantes):
    print("Participante: ", n+1)
    participantes[n].ingresardatos_participante()
    print(" ")
  print(" ")
  print("A continuación podra gestionar la logistica del evento: ")
  evento1.gestionar_logistica()
  print(" ")
  print("A continuación podra enviar las notificaciones a los participantes del evento: ")
  for n in range(0,evento1.cantidad_participantes): 
    notificacion1 = notificacion(participantes[n].nombre,participantes[n].apellido,participantes[n].numero_documento,participantes[n].telefono,participantes[n].correo)
    notificacion1.enviar_notificacion(participantes[n],evento1)
  print("Se han enviado las notificaciones del evento correctamente")
  print(" ")
  print("A continuación podra ver la invitación digital del evento: ")
  notificacion1.mostrar_invitaciondigital(evento1)
  print(" ")
  print("Gracias por gestionar su evento con nosotros, esperamos que sea un dia inolvidable")
else:
  print("Gracias por visitar nuestra plataforma de gestión de eventos, esperamos poder ayudarle con su evento en el futuro")
