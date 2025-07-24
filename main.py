from script import *


def mostrar_menu():
      print("1. CREAR CARPETA")
      print("2. EDITAR CARPETA")
      print("3. BORRAR CARPETA")
      print("4. CREAR ARCHIVO")
      print("5. EDITAR ARCHIVO")
      print("6. BORRAR ARCHIVO")
      print("7. SALIR")



while(True):
      mostrar_menu()

      opcion = input("Que tarea desea realizar: ")

      if opcion == "1":
            crear_carpeta()
      elif opcion == "2":
            editar_carpeta()
      elif opcion == "3":
            borrar_carpeta()
      elif opcion == "4":
            crear_archivo()
      elif opcion == "5":
            editar_archivo()
      elif opcion == "6":
            borrar_archivo()
      elif opcion == "7":
            salir()
            break
      
      else:
           print("OPCION NO VALIDA")