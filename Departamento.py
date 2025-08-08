"""
Módulo que define las entidades principales del sistema de gestión de piezas artísticas y áreas del museo.
"""
class Departamento:
        
    def __init__(self, id_departamento, nombre_departamento):
        self.id_departamento = id_departamento
        self.nombre_departamento = nombre_departamento

    def descripcion(self):
        """
        Devuelve una cadena que tiene id - nombre
        """
        return f"{self.id_departamento} - {self.nombre_departamento}"
