#Modulo para manejar la lista de nacionalidades validas para autores de obras. Incluye agrupaciones y acceso a todas las nacionalidades.

def obtener_nacionalidades(ruta_csv="CH_Nationality_List_20171130_v1.csv"):
    
    #Devuelve una lista con todas las nacionalidades leídas del archivo CSV.
  
    nacionalidades = []
    try:
        with open(ruta_csv, encoding="utf-8") as archivo:
            next(archivo)  
            for linea in archivo:
                nombre = linea.strip()
                if nombre:
                    nacionalidades.append(nombre)
    except Exception as e:
        print(f"No se pudo leer el archivo de nacionalidades: {e}")
    return nacionalidades
