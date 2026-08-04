#Este archivo fue trabajado por todos los integrantes del grupo en conjunto por medio de la extension de Visual Studio Code "Live Share"
# Juan Pablo Arruba
# Tomas Castaño Taborda
# Israel Cañizalez Mongua

from colorama import Fore
from Usuario import Usuario
import numpy as np
from Validaciones import *
class Cliente(Usuario):
    
    nombre:str
    tipo_identificacion:str 
    telefono:int
    direccion:str
    correo:str       
    cont_credito:int
    cantidad_compras:int = 0
    

    """
    Descripción: Esta clase representa a cada uno de los clientes del minimarket que se registra en el sistema
    
    ATRIBUTOS:
    
    nombre: Un dato de tipo texto que almacena el nombre del cliente
    tipo_identificacion: Un dato de tipo texto que almacena el tipo de identificación del cliente
    telefono: Un dato de tipo entero que almacena el telefono del cliente
    direccion: Un dato de tipo texto que almacena la dirrección del cliente
    correo: Un dato de tipo texto que almacena el correo del cliente    
    cont_credito: Un dato de tipo entero que almacena el número de ventas a credito que tiene el cliente
    saldo_pendiente: Un dato de tipo real que almacena el dinero que debe el cliente al minimarket
    
    CONS:
    
    No aplica
    
    """
    def __init__(self):
        """
        Descripción: Este metodo instancia los atributos del objeto
        asignandole valores por defecto, ademas llama al constructor de la clase padre
        
        PARAM:
        
        No aplica
        
        RETURN:
        
        No aplica
        
        """
        
        super().__init__()
        self.tipo_usuario=3
        self.nombre=""
        self.tipo_identificacion=""
        self.identificacion=-1
        self.telefono=-1
        self.direccion=""
        self.correo=""
        self.cont_credito=0
        self.contrasena=""
        self.cantidad_compras=0
    
    def pedir_datos(self,arr_clientes:np.ndarray,clientes_registrados:int) -> None:
        """
        Descripción: Este metodo pide los datos del cliente, realizando verificaciones y validaciones de
        los datos que ingresa el usuario
        
        PARAM:
        arr_clientes Un arreglo con un tamano maximo de 100, que en cada posicion almacena los objetos de tipo cliente, se usa
        en este metodo para verificar que los datos que ingresa el usuario no esten ya almacenados en el sistema 
        
        proveedores_registrados:int Una variable de tipo entero que apunta a la primera casilla libre del arreglo de clientes, se usa en este metodo para
        recorrer el arreglo y verificar datos 
        
        RETURN:
        No aplica 
        """
        #___________________________________________________________Verificacion nombre
        self.nombre=validacion_nombre()
        #___________________________________________________________Verificacion tipo de identificacion
        self.tipo_identificacion=validacion_tipo_identificacion()
       #____________________________________________________________Verificacion identificacion
        bandera:bool
        bandera=False
        cont:int
        cont=0
        duplicado:bool
        duplicado=False
        while (bandera == False):
            self.identificacion=validacion_identificacion()
            while duplicado ==False:
                cont=0               #Esta parte del codigo verifica si ya hay un cliente con la misma identificacion
                for i in range (clientes_registrados):
                    if (self.identificacion == arr_clientes[i].identificacion ):
                        cont+=1
                        break
                if cont ==1 :
                    duplicado=True
                    print(Fore.RED + "La identificación ya está registrada")
                    self.identificacion=-1
                    break
                
                elif cont ==0:
                    bandera = True
                    print(Fore.GREEN + "\nIdentificación válida\n")
                    break
        #________________________________________________________Verificacion telefono
        self.telefono=validacion_telefono()
        #________________________________________________________Verificacion direccion
        self.direccion = validacion_direccion()
        #________________________________________________________Verificacion correo
        self.correo=validacion_correo()
        #_________________________________________________________Verificacion contrasena
        self.contrasena=validacion_contrasena()