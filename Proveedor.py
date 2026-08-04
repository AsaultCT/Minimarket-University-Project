#Este archivo fue trabajado por todos los integrantes del grupo en conjunto por medio de la extension de Visual Studio Code "Live Share"
# Juan Pablo Arruba
# Tomas Castaño Taborda
# Israel Cañizalez Mongua

from colorama import Fore
import numpy as np
from Validaciones import *

class Proveedor:
    nombre:str
    identificacion:int
    telefono:int
    correo:str
    direccion:str
    """
    Descripción: Esta clase representa en el sistema un proveedor de la tienda.
    
    ATRIBUTOS:
    
    nombre: Una cadena de texto que contiene el nombre del proveedor
    identificacion: Un número entero no negativo de máximo 10 dígitos que guarda la identificación del proveedor
    telefono: Un número entero no negativo de exactamente 10 dígitos que guarda el telefono del proveedor
    correo: Una cadena de texto que contenga un “@” y un “.com” o “.co” que almacena el correo del proveedor
    direccion: Una cadena de texto que almacena la dirreción del proveedor

    
    CONS:
    
    No aplica
    
    """
    def __init__(self):
        """
        Descripción: Este metodo instancia los atributos del objeto
        asignandole valores por defecto 
        
        PARAM:
        
        No aplica
        
        RETURN:
        
        No aplica
        """
        
        self.nombre = ""
        self.identificacion = -1
        self.telefono = -1
        self.correo = ""
        self.direccion = ""
    
    def pedir_datos(self, arr_proveedores:np.ndarray,proveedores_registrados:int) -> None:
        """
        Descripción: Este metodo pide los datos del proveedor, realizando verificaciones y validaciones de
        los datos que ingresa el usuario
        
        PARAM:
        arr_proveedores: Un arreglo con un tamano maximo de 100, que en cada posicion almacena los objetos de tipo proveedor, se usa
        en este metodo para verificar que los datos que ingresa el usuario no esten ya almacenados en el sistema 
        
        proveedores_registrados:int Una variable de tipo entero que apunta a la casilla del arreglo de proveedores, se usa en este metodo para
        recorrer el arreglo y verificar datos
        
        RETURN:
        
        No aplica 
        
        """
        
        #_____________________________________________________Verificacion nombre
        self.nombre=validacion_nombre()

        #_______________________________________________________Verificacion identificacion
        """
        Este apartado de codigo se encarga de verificar la identificacion que se le va a asignar al proveedor,
        con 2 bucles while anidados hacemos lo siguiente:
        En el bucle while interno realizamos la validacion de la identificacion ingresada, asegurandonos de que su longitud sea menor a 10 y de que no sea negativa
        Al terminar ese bucle, buscamos en la lista de proveedores buscando que la identificacion no haya sido registrada antes por otro proveedor.
        El papel del bucle mas externo, es que si se encuentra una coincidencia de identificaciones, el bucle haga que el proveedor deba ingresar otra identificacion
        
        """

        bandera:bool
        bandera=False
        cont:int
        cont=0
        duplicado:bool
        duplicado=False
        while (bandera == False):
            self.identificacion= validacion_identificacion()
            
            while duplicado ==False:
                cont=0
                for i in range (proveedores_registrados):
                    if (self.identificacion == arr_proveedores[i].identificacion ):     #Y este es el apartado que se encarga de verificar que la identificacion ingresada no haya sido registrada antes por otro proveedor
                        cont+=1         #Se verifica recorriendo el arreglo de proveedores y en caso de que estemos en presencia de una coincidencia, cont se suma 1 
                        break
                if cont ==1 :     #Cuando cont es 1, avisamos al usuario y con el break salimos del bucle mas interno, por lo que se vuelvea pedir y validar la identificacion
                    duplicado=True           
                    print(Fore.RED + "El número de identificación del proveedor ya esta registrado")
                    self.identificacion=-1
                    break
                
                elif cont ==0:
                    bandera = True
                    print(Fore.GREEN + "Su identificación es válida")
                    break
        


        #__________________________________________________Verificacion telefono: Una validacion que se encarga de que el telefono tenga una longitud exacta de 10 y de que no sea negativo
        self.telefono=validacion_telefono()
        
        #__________________________________________________Verificacion correo
        self.correo=validacion_correo()
        #______________________________________________________Verificacion direccion
        self.direccion=input(Fore.BLUE + "Ingrese la direccion del Proveedor")