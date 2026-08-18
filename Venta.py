import numpy as np
from Cliente import *
from Validaciones import *
from datetime import date
from colorama import Fore
from Producto import *


class Venta:

    fecha:date
    cliente:Cliente
    precio_total:float
    saldo_pendiente:float
    arr_cantidad_productos:np.ndarray
    arr_productos_venta:np.ndarray
    venta_credito:bool
    identificador:int

    
    def __init__(self):

        self.fecha = date.today()
        self.cliente = Cliente()
        self.precio_total = 0.0
        self.saldo_pendiente = 0.0
        self.arr_cantidad_productos = np.full(50,fill_value = 0,dtype = int)
        self.arr_productos_venta = np.full(50,fill_value = None,dtype = object)
        self.venta_credito = False
        self.identificador = 0




    def pedir_datos(self,arr_clientes:np.ndarray,arr_productos:np.ndarray,clientes_registrados:int,productos_registrados:int,ventas_registradas:int) -> None:
        
        identificacion:int
        bandera_cliente_pedir_datos:bool =True

        #__________________________________Asignando un cliente a la venta

        while (bandera_cliente_pedir_datos):

            identificacion=validacion_identificacion()
            
            for i in range(clientes_registrados):

                if (arr_clientes[i].identificacion == identificacion):

                    self.cliente=arr_clientes[i] #Guardamos el cliente encontrado, en self.cliente
                    self.cliente.cantidad_compras +=1 #El cliente ha hecho una compra más
                    bandera_cliente_pedir_datos=False
                    break  
            if(bandera_cliente_pedir_datos == True):
                print(Fore.RED + "\nNo se pudo encontrar un cliente con la identificación ingresada, intentelo de nuevo")




        #_________________________________Ingresando los productos a la venta_____________________
        
        if len(self.arr_productos_venta) == 0:
            print(Fore.RED + "No hay productos disponibles para vender")
            return
        
        j:int
        k:int
        opc:int
        codigo:int
        cantidad:int


        for j in range(len(self.arr_cantidad_productos)): 


            if (j == 0):
                opc = 1
            else:
                opc = validacion_opcion_venta()


            match (opc):
                case 1:
                    
                    #_______________Buscar el Producto____________
                    producto_encontrado = False
                    while(not producto_encontrado):
                    
                        codigo = validacion_codigo(productos_registrados)   #Valida de que el código cumpla con el formato

                    
                        for k in range(productos_registrados):     #Recorre el arreglo de los productos registrados en busca de un código que coincida
                            if(arr_productos[k].codigo == codigo):
                                self.arr_productos_venta[j] = arr_productos[k] 
                                producto_encontrado = True 
                                break

                        if (not producto_encontrado):
                            print(Fore.RED + "\nProducto no encontrado, verifique el código e intente nuevamente")
                    

                    #_____________Validar la cantidad disponible______________

                    while (True):

                        cantidad = validacion_cantidad()

                        if(cantidad > arr_productos[k].stock):
                            print(Fore.RED + "La cantidad ingresada excede el stock del producto")
                        else:

                            self.arr_cantidad_productos[j] = cantidad
                            arr_productos[k].stock -= cantidad
                            arr_productos[k].cantidad_vendida += cantidad
                            print(Fore.GREEN + "Producto registrado")
                            break               
                case 2:
                    break
        print(Fore.GREEN + "Productos registrados en la venta exitosamente")
        #________________________________Asignando un identificador a la venta
        self.identificador = asignacion_identificador(ventas_registradas)
        
        #_______________________________Calculando el precio total
        h:int
        for h in range(j+1):
            if (self.arr_productos_venta[h] != None):
                self.precio_total += (self.arr_cantidad_productos[h] * self.arr_productos_venta[h].precio_total)
        #_______________________________Venta credito
        opcion_venta:bool
        
        
        if(self.cliente.cont_credito == 2):
            print(Fore.RED + "Usted tiene 2 ventas a creditos, por lo que no puede hacer ninguna otra ")
            return
        
        opcion_venta = validacion_opcion_venta2()
        if(opcion_venta):
            self.venta_credito = True
            self.cliente.cont_credito += 1
        
        #_______________________________Saldo pendiente
        if(self.venta_credito == True):
            self.saldo_pendiente = self.precio_total + (0.05*self.precio_total)
    
    def generar_factura(self)->None:
        i:int
        print(Fore.WHITE + f"****************Factura****************\nFecha: {self.fecha}\nNombre del cliente: {self.cliente.nombre}\nIdentificacion del cliente: {self.cliente.identificacion}")
        for i in range(len(self.arr_productos_venta)):
            if self.arr_productos_venta[i] == None or self.arr_cantidad_productos[i] == 0:
                break
            else:
                print(Fore.WHITE + f"Producto #{i+1}: {self.arr_productos_venta[i].nombre}\t Cantidad: {self.arr_cantidad_productos[i]}\n")
        print(Fore.WHITE + f"Precio de la compra: {self.precio_total}")
    
    def realizar_abono(self,abono:float) -> bool:
        if(self.venta_credito == True):
            if(abono > self.saldo_pendiente):
                print(f"El abono ingresado excede el saldo pendiente, el cual es {self.saldo_pendiente}")
                return False
            else:
                self.saldo_pendiente -= abono
                print(Fore.GREEN + "El abono se ha registrado exitosamente: ")
                return True
        else:
            print("La venta no es acredito, por lo tanto no se pueden realizar abonos")
            return False
        
        



        
        

            
                    