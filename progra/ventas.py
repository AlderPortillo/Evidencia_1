ventas = {}


respuesta="Si"
while respuesta=="Si":
  print("Menu de opciones")
  print("1 - Registrar una venta")
  print("2 - Consultar una venta")
  print("3 - Salir")

  opcion = input ("¿Que opción desea elegir?")
    
  if ventas:
     clave = max(ventas) + 1
  else:
     clave = 1
        
  if opcion =="1":
     print("Registrar una venta")
     DescripcionArticulo = input ("Describa el articulo a vender: ")
     CantPiezas = float(input("Cual es la cantidad de piezas: "))
     PrecioVenta = float(input("Cual es el precio: "))
     registro = [DescripcionArticulo, CantPiezas, PrecioVenta]
     ventas[clave] = registro
     #Venta registrada
     total=(PrecioVenta * CantPiezas)
     print(f"\nSe agregó la venta con la clave: {clave}")
     print("Total a pagar: ", total)
    
         
  elif opcion == "2":
     print("Consulta una venta")
     clave_buscar =int(input("Ingrese la clave de la venta que desea consular: "))
     if clave_buscar in ventas.keys():
         print(ventas[clave_buscar])

     else:
         print("Venta no registrada")
      
  elif opcion == "3":
     print("Programa finalizado")
  else:
     print("Opción no valida")
respuesta=input("desea repetir una opcion Si/No")  
    