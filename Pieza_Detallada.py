class Pieza_Detallada:
    """
    Describe una pieza artística con todos sus detalles relevantes: título, autor, nacionalidad, fechas, tipo, año y enlace a imagen.
    """
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
        """
        Escribe la informacion basica de la pieza: codigo, titulo y autor 

        Returns: Un str con el formato "codigo - titulo (autor)"
        """
        return f"{self.codigo} - {self.titulo} ({self.autor})"


