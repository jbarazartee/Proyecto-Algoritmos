
#Modulo donde se encuentran las solicitudes a la API para el menu

import requests
from Departamento import Departamento
from Pieza_Detallada import Pieza_Detallada
from nacionalidades_disponibles import obtener_nacionalidades

class ConsultasMuseo:
    def __init__(self):
        pass

    def obtener_departamentos(self):
        url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
        departamentos = []
        try:
            respuesta = requests.get(url)
            datos = respuesta.json().get("departments", [])
            for dep in datos:
                departamentos.append(Departamento(dep.get("departmentId", 0), dep.get("displayName", "")))
        except Exception as e:
            print(f"Error al obtener departamentos: {e}")
        return departamentos

    def mostrar_departamentos(self):
        departamentos = self.obtener_departamentos()
        print("Departamentos disponibles:")
        for d in departamentos:
            print(d)

    def buscar_pieza_basica(self, object_id):
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
        try:
            resp = requests.get(url)
            if resp.status_code != 200 or not resp.content or resp.text.strip() == '':
                print(f"No se encontró la pieza con ID {object_id}, error: {resp.status_code}.")
                return None
            data = resp.json()
            return PiezaDetallada(
                codigo=object_id,
                titulo=data.get("title", "No encontrado"),
                autor=data.get("artistDisplayName", "No encontrado"),
                origen=data.get("artistNationality", "No encontrado"),
                nacimiento=data.get("artistBeginDate", "No encontrado"),
                fallecimiento=data.get("artistEndDate", "No encontrado"),
                tipo=data.get("classification", "No encontrado"),
                anio=data.get("objectDate", "No encontrado") 
            )
        except Exception:
            return None

    def buscar_por_departamento(self, id_departamento):
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds={id_departamento}"
        piezas = []
        error_mostrado = False
        try:
            resp = requests.get(url)
            ids = resp.json().get("objectIDs", [])
            for oid in ids:
                try:
                    pieza = self.buscar_pieza_basica(oid)
                    if pieza:
                        print(pieza.resumen())
                        piezas.append(pieza)
                except Exception:
                    if not error_mostrado:
                        print("Algunas piezas no pudieron ser recuperadas o no existen. Se omiten del listado.")
                        error_mostrado = True
        except Exception:
            print("No se pudo obtener la lista de piezas para este departamento.")
        return piezas

