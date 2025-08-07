from solicitudes_api import ConsultasMuseo

def mostrar_menu():
  """
  Muestra el menú principal y gestiona la navegación del usuario.
  """
  consultas = ConsultasMuseo()
  while True:
    print("\n=== Menu Principal ===")
    print("1. Ver obras por departamento")
    print("2. Ver obras por nacionalidad de autor")
    print("3. Ver obras por nombre de autor")
    print("4. Ver detalles de una obra")
    print("5. Salir")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
      consultas.mostrar_departamentos()
      try:
        dep_id = int(input("Ingrese el ID del departamento: "))
        consultas.buscar_por_departamento(dep_id)
      except Exception:
        print("ID inválido.")
              
    elif opcion == "2":
      consultas.buscar_por_nacionalidad()
      
    elif opcion == "3":
      nombre = input("Ingrese nombre del autor: ")
      consultas.buscar_por_autor(nombre)
      
    elif opcion == "4":
        try:
          obra_id = int(input("Ingrese el ID de la obra: "))
          consultas.detalles_pieza(obra_id)
        except Exception:
          print("ID inválido.")
              
    elif opcion == "5":
      print("Hasta luego")
      break
      
    else:
      print("Opcion no valida")
