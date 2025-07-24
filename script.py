import os
import shutil

def crear_carpeta():
    nombre = input("Nombre de la carpeta: ")

    if len(nombre.strip()) > 1:
        try:
            os.makedirs(nombre)
            print(f"Carpeta '{nombre}' creada.")

        except FileExistsError:
            print("La carpeta ya existe.")
        except Exception as e:
            print(f" Error al crear la carpeta: {e}")
    else:
        print("Nombre inválido.")

def editar_carpeta():
    nombre = input("Nombre actual de la carpeta: ")
    if os.path.isdir(nombre):
        nuevo_nombre = input("Nuevo nombre de la carpeta: ")
        try:
            os.rename(nombre, nuevo_nombre)
            print(f"Carpeta renombrada a '{nuevo_nombre}'")
        except Exception as e:
            print(f"Error al renombrar: {e}")
    else:
        print("Carpeta no encontrada.")

def borrar_carpeta():
    nombre = input("Nombre de la carpeta a borrar: ")
    if os.path.isdir(nombre):
        try:
            shutil.rmtree(nombre)
            print(f"Carpeta '{nombre}' borrada con éxito.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Carpeta no encontrada.")

def crear_archivo():
      nombre = input("Nombre del archivo: ")
      if len(nombre.strip()) > 1:
        if os.path.exists(nombre):
            print("El archivo ya existe.")
        else:
            try:
                  with open(nombre, "w") as f:
                        f.write("Archivo creado")
                  print(f"Archivo '{nombre}' creado correctamente.")
            except Exception as e:
                  print(f"Error: {e}")
      else:
            print("Nombre inválido.")

def editar_archivo():
      nombre = input("Nombre actual del archivo: ")
      if os.path.isfile(nombre):
            nuevo_nombre = input("Nuevo nombre del archivo: ")
            try:
                  os.rename(nombre, nuevo_nombre)
                  print(f"Archivo renombrado a '{nuevo_nombre}'")
            except Exception as e:
                  print(f"Error al renombrar archivo: {e}")
      else:
            print("Archivo no encontrado.")

def borrar_archivo():
      nombre = input("Nombre del archivo a borrar: ")
      if os.path.isfile(nombre):
            try:
                  os.remove(nombre)
                  print(f"🗑️ Archivo '{nombre}' eliminado.")
            except Exception as e:
                  print(f"Error: {e}")
      else:
            print("Archivo no encontrado.")

def salir():
    print("**VUELVE PRONTO**")
