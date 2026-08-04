from datetime import date

class Devolucion:
    identificacion_producto:int
    cantidad_devuelta:int
    fecha:date
    motivo_devolucion:int
    
    def __init__(self):
        self.identificacion_producto = -1
        self.cantidad_devuelta = -1
        self.fecha = date.today()
        self.motivo_devolucion = -1
    
    def pedir_datos(self):
        