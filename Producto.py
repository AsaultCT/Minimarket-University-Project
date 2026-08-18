


import numpy as np
from Proveedor import *
from Usuario import *
from  Validaciones import *
#"""Indicare en el main, la descripcion de los pasos segun el documento de word que tenemos"""

# Clase Producto

class Producto:
    nombre:str
    codigo:int
    categoria:str
    costo_adquisicion:float
    precio_sin_iva:float                               
    porcentaje_iva:float
    stock:int
    stock_min:int
    proveedor:str
    precio_total:float
    cantidad_vendida:int = 0
    
    """
    CLASE: Producto
    DESCRIPCION:Esta clase representa en el sistema un producto de los que se venden en el minimarket.

    ATRIBUTOS: Nombre:Un dato de tipo Texto que guarda el nombre de un producto
               Codigo:Un dato de tipo Entero que almacena el codigo de identificacion de un producto
               Categoria:Un dato de tipo Texto que almacena la categoria a la que pertenece un producto
               Costo_adquisicion:Una dato de tipo Real que almacena el costo por el que fue adquirido el producto por el minimercado
               Precio_sin_IVA:Un dato de tipo Real que almacena el precio sin IVA por el que se va a vender el producto en el minimercado
               Porcentaje_IVA:Un dato de tipo Real que almacena el porcentaje de IVA que tiene el producto, que luego sera incluido
               Stock:Un dato de tipo Entero que almacena la cantidad actual de un producto en el minimercado
               Stock_min:Un dato de tipo Entero que almacena la cantidad minima de un producto que deben haber por motivos de control
               Proovedor: Un dato de tipo Proveedor que almacena los datos del Proveedor asignado a un producto del minimercado
    
    CONS:      No Aplica

    
    """
    
    
    def __init__(self):
        self.nombre = ""
        self.codigo = -1
        self.categoria = ""
        self.costo_adquisicion = 0.0
        self.precio_sin_iva = 0.0
        self.porcentaje_iva = -1
        self.stock = -1
        self.stock_min = -1
        self.precio_total = 0.0
        self.proveedor = Proveedor()
        self.cantidad_vendida = 0

    """
    Constructor clase Producto
    Descripcion:Instancia los atributos de cada objeto de tipo Producto 

    Parametros:No Aplica

    Asigna a cada atributo de la clase Producto un valor por defecto, cada uno varia dependiendo de su tipo y la validacion de cada dato que es realizada mas adelante
    
    """
    
    def pedir_datos(self,productos_registrados:int,arr_proveedores:np.ndarray,proveedores_registrados:int,) -> None:
       
        """
        Metodo:Pedir_datos de la clase Producto

        DESCRIPCION:Pide y valida los datos que tienen que ser ingresados por el usuario del minimercado
        
        PARAMETROS:
        arr_productos:Un arreglo que almacena datos de tipo Producto , este contiene en cada posicion un producto del minimercado distinto
        
        productos_registrados:Un contador de tipo entero que apunta a la posicion vacia mas cercana del arreglo arr_productos
        
        arr_proveedores:Un arreglo que almacena datos de tipo Proveedor, este contiene en cada posicion un proveedor del minimercado

        proveedores_registrados:Un contador de tipo entero que apunta a la posicion vacia mas cercana del arreglo arr_proveedores

        SALIDAS:No retorna nada
        """
       
       
       
        #_______________________________Verificacion nombre
        self.nombre = validacion_nombre()
        
        
        #_________________________________Verificacion codigo:Asigna automaticamente el codigo a un producto con la formula: codigo=productos_registrados+1
        self.codigo=asignacion_codigo(productos_registrados)

        
        

        
        #________________________________________Verificacion categoria
        self.categoria = validacion_categoria()
        
        #_________________________________________Verificacion costo adquisicion: Verifica que el costo de adquisicion del producto sea mayor a cero estrictamente
        self.costo_adquisicion=validacion_costo_adquisicion()
        
        #__________________________________Verificación Precio sin IVA:Verifica que el precio sin IVA sea mayor a cero estrictamente y que sea mayor al costo de adquisicion(O sea que un producto no puede ser vendido por un precio menor al que se compró )
        self.precio_sin_iva=validacion_precio_sin_iva(self.costo_adquisicion)

        #__________________________________Verificacion Porcentaje IVA: Verifica que el porcentaje de IVA se encuentre en un intervalo de 0 a 100
        self.porcentaje_iva=validacion_porcentaje_iva()
                    
        #_______________________________________________Verificacion stock:Verifica que el stock del producto no sea un numero negativo
        self.stock=validacion_stock()
        
        #_________________________________________________Verificacion stock minimo : Verifica que el stock minimo de un produto no sea negativo 
        self.stock_min=validacion_stock_min()
        
        #________________________________________________Verificacion proveedor: 
        
        
        """
        Este apartado del código se encarga de preguntarle al usuario
        si el proveedor que se le va a asignar al producto ya esta registrado
        o si apenas se va a registrar. Todo esto con la variable elección
        
        """

            
        
        print(Fore.BLUE + "Ahora va a ingresar los datos del proveedor del producto")
        input(Fore.WHITE + "Presione enter para continuar")
        if proveedores_registrados == 0:
            print(Fore.RED + "Actualmente no hay proveedores registrados, registre uno primero")
            return
        identificacion:int                  
        bandera:bool = True
        while(bandera):                 # pedimos la identificacion del Proveedor que ya se encuentra registrado
                       
            identificacion=validacion_identificacion()
                
            i:int
  
            for i in range(proveedores_registrados):
                if(arr_proveedores[i].identificacion == identificacion):   #Compara la identificacion ingresada con la de todos los proveedores registrados, y en caso de una coincidencia le asigna ese proveedor al producto
                    self.proveedor = arr_proveedores[i]
                    print(Fore.GREEN + "Proveedor asignado")
                    bandera = False
                    break
            if bandera ==True:
                print(Fore.RED + "No se encontro al proveedor, puede que haya ingresado los datos mal, intentelo de nuevo")


        self.precio_total = self.precio_sin_iva + ((self.porcentaje_iva/100)*self.precio_sin_iva)
