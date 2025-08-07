
#Módulo que define las entidades principales del sistema de gestión de piezas artísticas y áreas del museo.

   def __init__(self, codigo, titulo, autor, origen, nacimiento, fallecimiento, tipo, anio, url_imagen):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.origen = origen
        self.nacimiento = nacimiento
        self.fallecimiento = fallecimiento
        self.tipo = tipo
        self.anio = anio
        self.url_imagen = url_imagen

   def resumen (self):
      #Escribe la informacion basica de la pieza: codigo, titulo y autor 
       return f"{self.codigo} - {self.titulo} ({self.autor})"


