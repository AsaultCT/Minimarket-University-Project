# By: Tomas Castaño Taborda

import numpy as np
from colorama import Fore
from Usuario import *
from Producto import *
from Cliente import *
from Proveedor import *
from Validaciones import *
from Venta import *

class Minimarket:
    
    MAXIMO_USUARIOS:int =100
    arr_usuarios:np.ndarray =np.full(MAXIMO_USUARIOS, fill_value=None,dtype=object)
    arr_productos:np.ndarray =np.full(MAXIMO_USUARIOS, fill_value=None,dtype=object)
    arr_clientes:np.ndarray =np.full(MAXIMO_USUARIOS, fill_value=None,dtype=object)
    arr_proveedores:np.ndarray =np.full(MAXIMO_USUARIOS, fill_value=None,dtype=object)
    arr_ventas:np.ndarray =np.full(MAXIMO_USUARIOS, fill_value=None,dtype=object)
    arr_devoluciones:np.ndarray =np.full(MAXIMO_USUARIOS, fill_value=None,dtype=object)


    usuarios_registrados:int =0
    productos_registrados:int =0
    clientes_registrados:int =0
    proveedores_registrados:int =0
    ventas_registradas:int =0
    devoluciones_registradas:int =0

    usuario_autenticado:Usuario
    usuario_autenticado = None




    
    
    def __init__(self):
        
        #Este constructor carga los archivos
        self.arr_usuarios, self.usuarios_registrados = self.cargar_datos("Usuarios.npy",self.MAXIMO_USUARIOS)
        if (self.usuarios_registrados == 0):
            #Si el arreglo esta vacio se crea un administrador por defecto
            
            admin:Usuario                           
            admin = Usuario()                       
            admin.tipo_usuario = 1
            admin.contrasena = "AGUACATE"
            admin.identificacion = 12345678
            self.arr_usuarios[0] = admin
            
            if (not self.guardar_datos(self.arr_usuarios,"Usuarios.npy")):
                print(Fore.RED + "No se pudieron guardar los datos del archivo")
            else:
                print(Fore.GREEN + "Datos guardados exitosamente")
            
            
            self.usuarios_registrados=1

        self.arr_productos,self.productos_registrados = self.cargar_datos("Productos.npy",self.MAXIMO_USUARIOS)
        self.arr_clientes,self.clientes_registrados = self.cargar_datos("Clientes.npy",self.MAXIMO_USUARIOS)

        self.arr_proveedores,self.proveedores_registrados = self.cargar_datos("Proveedores.npy",self.MAXIMO_USUARIOS)
        self.arr_ventas,self.ventas_registradas = self.cargar_datos("Ventas.npy",self.MAXIMO_USUARIOS)





        
        
    def guardar_datos(self, arreglo_de_datos: np.ndarray, URL_archivo: str) -> bool:
        """ Este método almacena los datos de un arreglo en un archivo

            PARAMS
                arreglo_de_datos = arreglo Numpy con los datos a almacenar
                archivo = URL relativa del archivo en el que se almacenarán los datos

            RETURNS
                True sí almacena los datos correctamente en el archivo
                False sí no logra almacenar los datos en el archivo
        """
        try:
            np.save(URL_archivo, arreglo_de_datos)
            return True
        except (FileNotFoundError, EOFError):
            print (f"Error: no se pudieron almacenar los datos en el archivo {URL_archivo}.")
            return False





    
    
    def cargar_datos(self, URL_archivo: str, num_max_datos: int) -> tuple[np.ndarray, int]:
        """ Este método carga los datos de un archivo, en un arreglo específico

            PARAMS
                archivo = URL relativa del archivo a abrir                                       
                num_max_datos = indica el tamaño máximo de datos que almacena el arreglo

            RETURNS
                arreglo_de_datos = arreglo con los datos cargados
                num_datos = cantidad de datos cargados en el arreglo
        """
        try:
            arreglo_de_datos = np.load(URL_archivo, allow_pickle=True)
            i = 0
            while (arreglo_de_datos[i] != None):
                i += 1
            return arreglo_de_datos, i
        except (FileNotFoundError, EOFError):
            print (f"No se pudo cargar el archivo {URL_archivo}. Se creó un arreglo de datos vacío!")
            arreglo_de_datos = np.full((num_max_datos), fill_value=None, dtype=object)
            return arreglo_de_datos, 0
    





    
    
    
    def menu_inicial(self) -> None:
        """
        Descripción: Este metodo muestra en la terminal la pantalla de bienvenida al sistema del minimarket
        
        PARAM:
        
        No aplica
        
        RETURN:
        
        No aplica
        
        """
        
        print(Fore.BLUE + """
        ╔══════════════════════════════════════════════════════════╗
        ║                                                          ║
        ║        🛒  Bienvenido a M I N I M A R K E T  🛒         ║
        ║                                                          ║
        ║       "Tu tienda de confianza, siempre cerca"            ║
        ║                                                          ║
        ╠══════════════════════════════════════════════════════════╣
        ║                                                          ║
        ║   🥛 Lácteos      🍞 Panadería     🧴 Aseo              ║
        ║   🥩 Carnes       🍎 Frutas        📒 Papelería         ║
        ║   🥤 Bebidas      🍫 Dulces        🏠 Hogar             ║
        ║                                                          ║
        ╚══════════════════════════════════════════════════════════║
              """)
        


    #_______________________________________MENÚS_____________________________________________________      
    
    def menu_administrador(self)->int: 
        opcion_administrador:int = 0
        print(Fore.WHITE + "///// Bienvenido Administrador //////")  
        while (opcion_administrador < 1 or opcion_administrador > 10): #Menú se repite mientras que la opción ingresada esté fuera del rango de las opciones del menú
            try:
                opcion_administrador = int(input(Fore.BLUE + "¿Que acción desea realizar? \n 1. Registrar Usuario\n 2. Registrar Cliente \n 3. Consultar cliente \n 4. Modificar Cliente \n 5. Registrar Productos \n 6. Modificar Producto \n 7. Registrar Proveedor \n 8. Modificar Proveedor \n 9. Actualizar inventario \n 10. Productos más vendidos \n 11. Productos con menor rotación \n 12. Productos debajo del stock mínimo \n 13. Salir \n : "))
                if(opcion_administrador < 1 or opcion_administrador > 13):
                    print(Fore.RED + "Error, debes de ingresar una opción entre 1 y 10, intentelo de nuevo: ")
            except ValueError:
                print("Opción inválida, intentelo de nuevo: ")
        return opcion_administrador
    
    
    
    def menu_cajero(self)->int:
        opcion:int=0
        while opcion <1 or opcion >7:
            try:
                opcion=int(input(Fore.BLUE + "¿Que acción desea realizar? \n 1. Registrar venta \n 2. Consultar producto \n 3. Verificar disponibilidad en inventario \n 4. Gestionar devoluciones \n 5. Consultar información básica de los clientes \n 6. Registrar abono\n7. Cerrar sesion \n :"))
                if opcion <1 or opcion >7:
                    print(Fore.RED + f"La opción {opcion}no esta dentro del interválo permitido, intente de nuevo")
            except ValueError:
                print(Fore.RED + f"La opcion no es valida, intente de nuevo")
        print(Fore.GREEN + "La opción ha sido guardada correctamente")
        return opcion

    def menu_cliente(self)->int:
        opcion:int=0
        while opcion <1 or opcion >4:
            try:
                opcion=int(input(Fore.WHITE + f"¿Que acción desea realizar? \n 1. Consultar el historial de compras \n 2. Ver una factura especifica \n 3. Ver facturas con saldo pendiente \n 4. Gerrar sesion"))
                if opcion <1 or opcion>4:
                    print(Fore.RED + "Su opcion no esta dentro del intervalo permitido, intentelo de nuevo")
            except ValueError:
                print(Fore.RED + "Su opcion no es valida, intentelo de nuevo")
        print(Fore.GREEN + "La opción ha sido guardada correctamente")
        return opcion
    #________________________________________________________________________________________________
    
    def registrar_abono(self) -> bool:
        identificacion:int
        i:int
        identificacion = validacion_identificacion()
        
        for i in range(len(self.arr_ventas)):
            if(self.arr[i] != None):
                if(self.arr_venta[i].cliente.identificacion == identificacion):
                    self.arr_venta[i].realizar_abono()
            
                
                
    
    def registrar_usuario(self,usuario:Usuario)->bool:
        if self.usuarios_registrados>=100:
            print("Arreglo de usuarios lleno")
            return False
        else:
            self.arr_usuarios[self.usuarios_registrados]=usuario
            self.arr_usuarios[self.usuarios_registrados].pedir_datos(self.arr_usuarios,self.usuarios_registrados)
            self.usuarios_registrados+=1
            if not(self.guardar_datos(self.arr_usuarios,"Usuarios.npy")):
                print(Fore.RED + "El archivo de usuarios no pudo ser actualizado")

            else:
                print(Fore.GREEN + "El archivo de usuarios fue actualizado exitosamente")
                return True






    #_______________________________RF21 VERIFICAR DISPONIBILIDAD___________________________________  

    def verificar_disponibilidad_en_inventario(self)->None:

        codigo:int
        bandera_disponibilidad:bool=True

        print(Fore.WHITE + "Lista de productos junto a la cantidad disponible")
        input(Fore.WHITE + "Presione enter para continuar")
        
        for i in range(self.productos_registrados):
            print(Fore.WHITE + f"Producto #{i +1}:{self.arr_productos[i].nombre} \t Código: {self.arr_productos[i].codigo}  \n")
        





    def consultar_producto(self)->None:
        codigo:int
        i:int
        j:int
        print(Fore.WHITE + "Usted ha seleccionado consultar producto")
        print(Fore.WHITE + "A continuacion se le va a mostrar la lista de productos junto a la cantidad disponible de ellos")
        input(Fore.WHITE + "Presione enter para continuar")
        for i in range(self.productos_registrados):
            print(Fore.WHITE + f"Producto #{i +1}:{self.arr_productos[i].nombre} \t Codigo: {self.arr_productos[i].codigo}  \n")
        codigo= validacion_codigo(self.productos_registrados)
        for j in range (self.productos_registrados):
            if (self.arr_productos[j].codigo == codigo):
                print(Fore.WHITE + f"Usted ha decidido consultar el producto: {self.arr_productos[j].nombre}")
                print(Fore.WHITE + f"El nombre del producto es : {self.arr_productos[j].nombre}\n El codigo del producto es :{self.arr_productos[j].codigo}\nLa categoria del producto es: {self.arr_productos[j].categoria}\nEl costo de adquisicion es :{self.arr_productos[j].costo_adquisicion}\nEl precio sin IVA del producto es :{self.arr_productos[j].precio_sin_iva}")
                
    #_________________________________RF12 MODIFICAR PRODUCTO____________________________________

    def modificar_producto(self)->None:
        codigo:int
        identificacion:int
        bandera:bool=True
        
        print(Fore.WHITE + "A continuacion se le van a mostrar todos los productos con sus respectivos codigos: ")
        
        for i in range(self.productos_registrados):
            print(Fore.WHITE + f"Producto #{i +1}:{self.arr_productos[i].nombre} \t Codigo: {self.arr_productos[i].codigo}  \n")
        input(Fore.WHITE + "Ahora va a ingresar el codigo del producto que desea modificar, presione enter para continuar")
        
        codigo=validacion_codigo(self.productos_registrados)
        
        for j in range(self.productos_registrados):
            if self.arr_productos[j].codigo==codigo:
                
                while (bandera): 
                    opc:int = 0
                    print(Fore.WHITE + f"""
                    Ingrese una opción entre 1 y 8 para modificar el atributo que desea, ingrese 9 para dejar de modificar productos
                    1. Nombre: {self.arr_productos[j].nombre}
                    2. Categoria: {self.arr_productos[j].categoria}
                    3. Costo de adquisicion: {self.arr_productos[j].costo_adquisicion}
                    4. Precio sin IVA: {self.arr_productos[j].precio_sin_iva}
                    5. Porcentaje de IVA: {self.arr_productos[j].porcentaje_iva}
                    6. Stock: {self.arr_productos[j].stock}
                    7. Stock Minimo: {self.arr_productos[j].stock_min}
                    8. Proveedor: {self.arr_productos[j].proveedor.nombre}
                    --------------------------------------------
                    9. Dejar de modificar\n""")
                    
                    #Validacion de opcion____________________________________________
                    while (opc < 1 or opc > 9):
                                try:
                                    opc = int(input("¿Que atributo desea modificar? : "))
                                    if (opc < 1 or opc > 9):
                                        print(Fore.RED + "Debe de ingresar una opción entre 1 y 9, intentelo de nuevo")
                                except ValueError:
                                    print(Fore.RED + "Opción inválida, intentelo de nuevo")
                    match (opc):
                        
                        
                        case 1:#Nombre
                            
                            self.arr_productos[j].nombre = validacion_nombre()
                            print(Fore.GREEN + f"\nNombre del producto actualizado: {self.arr_productos[j].nombre}\n")
                        
                        
                        case 2:#Categoria
                            
                            self.arr_productos[j].categoria = validacion_categoria()
                            print(Fore.GREEN + f"\nLa nueva categoria del producto es: {self.arr_productos[j].categoria}\n")
                        
                        
                        case 3:#Costo adquisicion
                            
                            self.arr_productos[j].costo_adquisicion = validacion_costo_adquisicion()
                            print(Fore.GREEN + f"\nEl nuevo costo de adquisicion del producto es : {self.arr_productos[j].costo_adquisicion}\n")
                            
                        
                        case 4:#Precio sin IVA
                            self.arr_productos[j].precio_sin_iva = validacion_precio_sin_iva(self.arr_productos[j].costo_adquisicion)
                            print(Fore.GREEN + f"\nEl nuevo precio sin IVA del producto es: {self.arr_productos[j].precio_sin_iva}\n")
                        
                        
                        case 5: #Porcentaje IVA
                            
                            self.arr_productos[j].porcentaje_iva=validacion_porcentaje_iva()
                            print(Fore.GREEN + f"\nEl nuevo porcentaje de IVA del producto es {self.arr_productos[j].porcentaje_iva}\n")
                        
                        
                        case 6:#Stock
                        
                            self.arr_productos[j].stock=validacion_stock()
                            print(Fore.GREEN + f"\nEl nuevo stock del producto es {self.arr_productos[j].stock}\n")
                        
                        case 7:#Stock minimo
                            
                            self.arr_productos[j].stock_min=validacion_stock_min()
                            print(Fore.GREEN + f"\nEl nuevo stock minimo del producto es {self.arr_productos[j].stock_min}\n")
                            
                        case 8: #Proveedor
                            input(Fore.WHITE + "Ahora se van a mostrar todos los proveedores con sus identificaciones,presione enter para continuar")
                            for k in range(self.proveedores_registrados):
                                
                                print(Fore.WHITE + f"Proveedor #{k +1}:{self.arr_proveedores[k].nombre} \t Identificacion: {self.arr_proveedores[k].identificacion}  \n")
                            
                            bandera_proveedor:bool=True
                            while bandera_proveedor:
                                input(Fore.WHITE + "Ahora va a ingresar la identificacion del proveedor que desea que sea el nuevo proveedor del producto")
                                identificacion=validacion_identificacion()

                                for l in range (self.proveedores_registrados):
                                    if self.arr_proveedores[l].identificacion == identificacion:
                                        self.arr_productos[j].proveedor=self.arr_proveedores[l]
                                        print(Fore.GREEN + "El proveedor del producto fue actualizado exitosamente")
                                        bandera_proveedor=False
                                        break
                                if bandera_proveedor:
                                    print(Fore.RED + "La identificacion que ingreso no corresponde a la de ningun proveedor, intente de nuevo")
                            
                        case 9:
                            bandera=False
                            if not(self.guardar_datos(self.arr_productos,"Productos.npy")):
                                print(Fore.RED + "El archivo de productos no se pudo modificar")
                            else:
                                print(Fore.GREEN + "El archivo de productos se ha guardado exitosamente!")
                            return 
        print(Fore.RED + "El producto no fue encontrado")






    #________________________________RF16 PRODUCTOS MÁS VENDIDOS (Tomas)________________________________


    def productos_mas_vendidos(self) -> np.ndarray: #bookmark3

        arr_productos_temp:np.ndarray = self.arr_productos.copy()  # Copia del arreglo para evitar modificar el original y causar confusión/errores al operar después en otras funciones
        longitud:int = len(arr_productos_temp)


        #Organizamos los productos, de mayor a menor cantidad_vendida

        for i in range(longitud - 1):

            for j in range(longitud - i - 1):

                if (arr_productos_temp[j].cantidad_vendida < arr_productos_temp[j + 1].cantidad_vendida):

                    var_auxiliar = arr_productos_temp[j]
                    arr_productos_temp[j] = arr_productos_temp[j + 1]
                    arr_productos_temp[j + 1] = var_auxiliar

        mas_vendidos = arr_productos_temp[:3]


        return mas_vendidos
    


    
    #________________________________RF17 PRODUCTOS CON MENOR ROTACIÓN (Tomas)___________________________________

    def productos_menor_rotacion(self) -> np.ndarray:

        arr_productos_temp:np.ndarray = self.arr_productos.copy()  # Copia del arreglo para evitar modificar el original y causar confusión/errores al operar después en otras funciones
        longitud:int = len(arr_productos_temp)


        #Organizamos los productos, de menor a mayor cantidad_vendida

        for i in range(longitud - 1):

            for j in range(longitud - i - 1):

                if (arr_productos_temp[j].cantidad_vendida > arr_productos_temp[j + 1].cantidad_vendida):

                    var_auxiliar = arr_productos_temp[j]
                    arr_productos_temp[j] = arr_productos_temp[j + 1]
                    arr_productos_temp[j + 1] = var_auxiliar

        menos_rotacion = arr_productos_temp[:3]


        return menos_rotacion
    

    #______________________________RF18 PRODUCTOS DEBAJO DEL STOCK MINIMO (Tomas)_________________________


    def productos_bajo_stock(self) -> np.ndarray:

        debajo = 0

        #Conteo de cuantos productos están debajo del stock mínimo
        for i in range(self.productos_registrados):

            if (self.arr_productos[i].stock < self.arr_productos[i].stock_min):

                debajo += 1

        productos_debajo: np.ndarray = np.full(debajo, fill_value=None, dtype=object) #Arreglo de los productos debajo de stock mínimo

        j = 0

        #Llenamos el arreglo con los productos debajo del stock mínimo, no se organiza en función a que producto está más por debajo del stock mínimo que otro

        for i in range(self.productos_registrados):

            if (self.arr_productos[i].stock < self.arr_productos[i].stock_min):

                productos_debajo[j] = self.arr_productos[i]

                j += 1

        return productos_debajo


    #______________________________RF1 REGISTRAR PRODUCTO_________________________


    def registrar_producto(self,producto:object) -> bool:

        if (self.productos_registrados >= 100):
            return False
        
        producto.pedir_datos(self.productos_registrados,self.arr_proveedores,self.proveedores_registrados)
        self.arr_productos[self.productos_registrados] = producto
        self.productos_registrados += 1
        if (not self.guardar_datos(self.arr_productos,"Productos.npy")):
            print(Fore.RED + "El archivo producto no pudo ser actualizado")
        else:
            print(Fore.GREEN + "El archivo producto fue actualizado exitosamente")
        return True
    





    #_______________________________RF9 AUTENTICAR USUARIO___________________________________

        
    def autentificar_usuario(self,tipo_usuario:int,identificacion:int,contrasena:str) -> bool:
        """"
        Descripción: Este metodo se encarga de autentificar el usuario, verificando que existan en los arreglos correspondientes dando aviso por medio de
        su retorno del tipo de usuario que esta en presencia del sistema
        
        PARAM:
        
        tipo_usuario: Un dato de tipo entero que almacena el tipo de usuario que se esta intentando autentificar, se utiliza para verificar
        si el tipo de usuario del usuario que se esta autentificando es igual al tipo de usuario del usuario registrado identificado en el arreglo de usuarios
        
        identificacion: Un dato de tipo entero que almacena la identificación del usuario que se esta intentando autentificar, se usa para
        recorrer el arreglo respectivo de su tipo de usuario y verificar si existe
        
        contrasena: Un dato de tipo texto que almacena la contraseña que ingreso el usuario que se esta autentificando, se utiliza para ver si coincide con la
        contraseña del usuario registrardo que coincidio con la identificación
        
        usuarios_registrados: Un dato de tipo entero que apunta a la primera casilla libre del arreglo de usuarios
        
        arr_usuarios: Un arreglo con un tamaño maximo de 100 que almacena a los usuarios registrados en la plataforma, se utiliza en este meotodo
        para recorrerlo y verificar datos, en caso de que el usuario a autentificar sea de tipo cajero o administrador
        
        arr_clientes: Un arreglo con un tamaño maximo de 100 que almacena a los clientes registrados en la plataforma, se utiliza en este meotodo
        para recorrerlo y verificar datos, en caso de que el usuario a autentificar sea de tipo cliente
        
        clientes_registrados: Un dato de tipo entero que apunta a la primera casilla libre del arreglo de clientes
        
        
        RETURN:
        El metodo retorna un valor entero indicando si la autentificación fue existosa o no, devolviendo el número 0 si el proceso no fue exitoso
        el 1 si el proceso fue exitoso y se autentifico un administrador, el 2 si la verificación fue existosa y se autentico un cajero
        y 3 si el proceso fue exitoso y se autentiifco un cliente.
        
        """
        
        #Tipo_usuario es un parámetro que tiene solamente puede tener como valores 1,2 o 3
        
        
        
        if (tipo_usuario == 1 or tipo_usuario == 2):  #Si tipo usuario es 1 o 2, significa que estamos en presencia de un admin o un cajero
            i:int                                     
            for i in range(self.usuarios_registrados):      #Buscamos en el arreglo de admins y cajeros , que en este caso comparten el mismo, arr_usuarios                 
                if (self.arr_usuarios[i].identificacion ==  identificacion):    #Con ayuda del parametro identificacion, buscamos un usuario ya registrado con la misma identificacion       
                    if(self.arr_usuarios[i].contrasena == contrasena):
                        if(self.arr_usuarios[i].tipo_usuario==tipo_usuario):
                            self.usuario_autenticado = self.arr_usuarios[i]
                            return True        #En caso de que se encuentre se retorna el tipo de usuario que se autenticó, esto para solo mostrarle las funciones exclusivas de ese perfil
            return False #Este return False significa que no se pudo autentificar el usuario, porque no encontro coincidencias
        else:
            j:int
            for j in range(self.clientes_registrados):
                if(self.arr_clientes[j].identificacion == identificacion):
                    if(self.arr_clientes[j].contrasena == contrasena):
                        self.usuario_autenticado=self.arr_clientes[j]
                        return True
            return False






    #___________________________RF5 REGISTRAR CLIENTE________________________________   
               
    def registrar_cliente(self,cliente:object) -> bool:
        if (self.clientes_registrados >= 100):
            return False
        cliente.pedir_datos(self.arr_clientes,self.clientes_registrados)
        self.arr_clientes[self.clientes_registrados] = cliente
        self.clientes_registrados+=1
        if (not self.guardar_datos(self.arr_clientes,"Clientes.npy")):
            print(Fore.RED + "El archivo producto no pudo ser actualizado")
        else:
            print(Fore.GREEN + "El archivo producto fue actualizado exitosamente")
        return True





    #__________________________RF2 REGISTRAR PROVEEDOR__________________________________
     
    def registrar_proveedor(self,proveedor:object) -> bool:
        if(self.proveedores_registrados >= 100):
            return False
        proveedor.pedir_datos(self.arr_proveedores,self.proveedores_registrados)
        self.arr_proveedores[self.proveedores_registrados] = proveedor
        self.proveedores_registrados+=1
        if (not self.guardar_datos(self.arr_proveedores,"Proveedores.npy")):
            print(Fore.RED + "El archivo proveedores no pudo ser actualizado")
        else:
            print(Fore.GREEN + "El archivo proveedores fue actualizado exitosamente")
        return True









    #______________________________RF4 REGISTRAR VENTA_______________________________________________
    
    def registrar_venta(self,venta:object) -> bool:
        if (self.ventas_registradas >= 100):
            return False
        venta.pedir_datos(self.arr_clientes,self.arr_productos,self.clientes_registrados,self.productos_registrados,self.ventas_registradas)
        self.arr_ventas[self.ventas_registradas] = venta
        self.ventas_registradas += 1
        print(self.arr_ventas)
        if (not self.guardar_datos(self.arr_ventas,"Ventas.npy")):
            print(Fore.RED + "El archivo venta no pudo ser actualizado")
        else:
            print(Fore.GREEN + "El archivo venta fue actualizado exitosamente")
        return True
    
    


    def consultar_historial(self)->None:
        input(Fore.WHITE + "Ahora se le van a mostrar todas las compras que ha hecho, presione enter para continuar")
        identificacion:int

        identificacion=validacion_identificacion()

        for i in range(self.ventas_registradas):
            if self.arr_ventas[i].cliente.identificacion == identificacion:
                self.arr_ventas[i].generar_factura()
                
    #_____________________________RF3 ACTUALIZAR INVENTARIO_______________________________________

    def actualizar_inventario(self)->None:
        i:int
        j:int
        codigo:int
        
        print(Fore.WHITE + "A continuacion se le va a mostrar la lista de productos junto a la cantidad disponible de ellos")
        input(Fore.WHITE + "Presione enter para continuar")
        for i in range(self.productos_registrados):
            print(Fore.WHITE + f"Producto #{i +1}:{self.arr_productos[i].nombre} \t Codigo: {self.arr_productos[i].codigo} \tCantidad:{self.arr_productos[i].stock} \n")
        print(Fore.BLUE + "Ahora seleccione el codigo del producto al cual desea agregarle mas existencias ")

        
        while True:
           
            codigo=validacion_codigo(self.productos_registrados)
            for j in range(self.productos_registrados):
                if (codigo== self.arr_productos[j].codigo):
                    
                    print(Fore.WHITE + f"Usted ha decidido modificar el stock del producto: {self.arr_productos[j].nombre}")
                    print(Fore.WHITE + "Recuerde que el nuevo numero que ingrese a continuacion se va a sumar al stock previamente existente")
                    self.arr_productos[j].stock+=validacion_stock ()
                    print(Fore.GREEN + f"El stock del producto {self.arr_productos[j].nombre} ha sido modificado a {self.arr_productos[j].stock} exitosamente! ")
                    if not(self.guardar_datos(self.arr_productos,"Productos.npy")):
                        print(Fore.RED + "El archivo de productos no pudo ser actualizado...")
                    else:
                        print(Fore.GREEN + "El archivo de productos fue actualizado correctamente")
                    return
            print(Fore.RED + "El codigo del producto no se ha encontrado...Ingrese otro codigo")



                    
    #___________________________RF14 MODIFICAR CLIENTE______________________________

    def modificar_cliente(self) -> bool:
        
        identificacion:int = -1
        i:int
        identificacion=validacion_identificacion()
        print(Fore.GREEN + "\nIdentificación valida\n")
    
        for i in range(self.clientes_registrados):
            if(self.arr_clientes[i].identificacion == identificacion):
                bandera:bool = True
                while (bandera): 
                    opc:int = 0
                    print(Fore.WHITE + f"""
                    Ingrese una opción entre 1 y 7 para modificar el atributo que desea, ingrese 8 para dejar de modificar
                        
                    1. Nombre: {self.arr_clientes[i].nombre}
                    2. Tipo de identificación: {self.arr_clientes[i].tipo_identificacion}
                    3. Identificación: {self.arr_clientes[i].identificacion}
                    4. Teléfono: {self.arr_clientes[i].telefono}
                    5. Dirección: {self.arr_clientes[i].direccion}
                    6. Correo eléctronico: {self.arr_clientes[i].correo}
                    7. Contraseña: {self.arr_clientes[i].contrasena}
                    --------------------------------------------
                    8. Dejar de modificar\n""")
                    while (opc < 1 or opc > 8):
                                try:
                                    opc = int(input("¿Que atributo desea modificar? : "))
                                    if (opc < 1 or opc > 8):
                                        print(Fore.RED + "Debe de ingresar una opción entre 1 y 8, intentelo de nuevo")
                                except ValueError:
                                    print(Fore.RED + "Opción inválida, intentelo de nuevo")
                    match (opc):
                        
                        
                        case 1:
                            self.arr_clientes[i].nombre = input(Fore.BLUE + "Nombre del cliente: ")
                            print(Fore.GREEN + f"\nNombre del cliente actualizado: {self.arr_clientes[i].nombre}\n")
                        
                        
                         
                        case 2:
                            
                            self.arr_clientes[i].tipo_identificacion = validacion_tipo_identificacion()
                            print(Fore.GREEN + f"\nNuevo tipo de identificación: {self.arr_clientes[i].tipo_identificacion}\n")
                        
                        
                        
                        case 3:
                            
                            self.arr_clientes[i].identificacion = validacion_identificacion()
                            print(Fore.GREEN + f"\nLa nueva identificación es {self.arr_clientes[i].identificacion}\n")
                        
                        
                        case 4:
                            
                            self.arr_clientes[i].telefono = validacion_telefono()
                            print(Fore.GREEN + f"\nEl nuevo número de teléfono del cliente es {self.arr_clientes[i].telefono}\n")
                            
                        
                        case 5:
                            self.arr_clientes[i].direccion = input(Fore.BLUE + "Ingrese la nueva dirección del Cliente")
                            print(Fore.GREEN + f"\nLa nueva dirreción del cliente es {self.arr_clientes[i].direccion}\n")
                        
                        
                        case 6:
                            
                            self.arr_clientes[i].correo=validacion_correo()
                            print(Fore.GREEN + f"\nLa nueva dirección de correo del cliente es {self.arr_clientes[i].correo}\n")
                        
                        
                        case 7:
                            
                            self.arr_clientes[i].contrasena=validacion_contrasena()
                            print(Fore.GREEN + f"\nLa nueva contraseña del cliente es {self.arr_clientes[i].contrasena}\n")
                        case 8:
                            bandera=False
                            if not(self.guardar_datos(self.arr_clientes,"Clientes.npy")):
                                print(Fore.RED + "El archivo de clientes no se pudo modificar")
                            else:
                                print(Fore.GREEN + "El archivo de clientes se ha guardado exitosamente!")
                            
                return True
        return False
    



    #_________________________RF11 CONSULTAR CLIENTE_________________________

    def consultar_cliente(self) -> None:
        id:int
        i:int
        id = validacion_identificacion()
        if(self.usuario_autenticado.tipo_usuario == 2):
            for i in range(self.clientes_registrados):
                if(self.arr_clientes[i].identificacion == id):
                    print(f"Información basica - Cliente - ID:{self.arr_clientes[i].identificacion} \n - Nombre: {self.arr_clientes[i].nombre} \n - Tipo de identificación: {self.arr_clientes[i].tipo_identificacion} \n  - Número de facturas pendientes: {self.arr_clientes[i].cont_credito} \n - Saldo pendiente: {self.arr_clientes[i].saldo_pendiente}")
                    input(Fore.WHITE + "Presione enter para continuar...")
                    return   
            print(Fore.RED + "El cliente no fue encontrado")      
        else:
            if(self.usuario_autenticado.tipo_usuario == 1):
                for i in range(self.clientes_registrados):
                    if(self.arr_clientes[i].identificacion == id):
                        print(f"Información Completa - Cliente \n - ID:{self.arr_clientes[i].identificacion} \n - Nombre: {self.arr_clientes[i].nombre} \n - Tipo de identificación: {self.arr_clientes[i].tipo_identificacion} \n - Telefono: {self.arr_clientes[i].telefono} \n - Dirección: {self.arr_clientes[i].direccion} \n - Correo eléctronico: {self.arr_clientes[i].correo} \n - Número de facturas pendientes: {self.arr_clientes[i].cont_credito} \n - Saldo pendiente: {self.arr_clientes[i].saldo_pendiente}")
                        input(Fore.WHITE + "Presione enter para continuar...")
                        return
                print(Fore.RED + "El cliente no fue encontrado")  

                
    #__________________________RF20 CLIENTES MÁS FRECUENTES (Tomas)_____________________________
    
        
    def clientes_mas_frecuentes(self) -> np.ndarray:


        arr_clientes_temp:np.ndarray = self.arr_clientes.copy()  # Copia del arreglo para evitar modificar el original y causar confusión/errores al operar después en otras funciones
        longitud:int = len(arr_clientes_temp)


        #Se organiza el arreglo temporal de clientes, de tal forma que los clientes con más cantidad de compras irán al inicio del arreglo

        for i in range(longitud - 1):

            for j in range(longitud - i - 1):

                if (arr_clientes_temp[j].cantidad_compras < arr_clientes_temp[j + 1].cantidad_compras):

                    var_auxiliar = arr_clientes_temp[j]
                    arr_clientes_temp[j] = arr_clientes_temp[j + 1]
                    arr_clientes_temp[j + 1] = var_auxiliar

        mas_frecuentes = arr_clientes_temp[:5]


        return mas_frecuentes


      

        
    #__________________________RF13 MODIFICAR PROVEEDOR____________________________

    def modificar_proveedor(self) -> bool:
        identificacion:int = -1
        i:int
        identificacion=validacion_identificacion()
        print(Fore.GREEN + "\nIdentificación valida\n")
        
        for i in range(self.proveedores_registrados):                            
            if(self.arr_proveedores[i].identificacion == identificacion):
                bandera:bool = True
                while (bandera): 
                    opc:int = 0
                    print(Fore.WHITE + f"""
                    Ingrese una opción entre 1 y 5 para modificar el atributo que desea, ingrese 6 para dejar de modificar
                        
                    1. Nombre: {self.arr_proveedores[i].nombre}
                    2. Identificación: {self.arr_proveedores[i].identificacion}
                    3. Teléfono: {self.arr_proveedores[i].telefono}
                    4. Correo eléctronico: {self.arr_proveedores[i].correo}
                    5. Dirección: {self.arr_proveedores[i].direccion}
                    --------------------------------------------
                    6. Dejar de modificar\n""")
                    while (opc < 1 or opc > 6):
                                try:
                                    opc = int(input("¿Que atributo desea modificar? : "))
                                    if (opc < 1 or opc > 6):
                                        print(Fore.RED + "Debe de ingresar una opción entre 1 y 6, intentelo de nuevo")
                                except ValueError:
                                    print(Fore.RED + "Opción inválida, intentelo de nuevo")
                    match (opc):
                        
                        
                        case 1:
                            self.arr_proveedores[i].nombre = input(Fore.BLUE + "Nombre del Proveedor: ")
                            print(Fore.GREEN + f"\nNombre del proveedor actualizado: {self.arr_proveedores[i].nombre}\n")    
                        
                        case 2:
                            
                            self.arr_proveedores[i].identificacion = validacion_identificacion()
                            print(Fore.GREEN + f"\nLa nueva identificación es {self.arr_proveedores[i].identificacion}\n")
                        
                        
                        case 3:
                            
                            self.arr_proveedores[i].telefono = validacion_telefono()
                            print(Fore.GREEN + f"\nEl nuevo número de teléfono del Proveedor es {self.arr_proveedores[i].telefono}\n")
                            
                        
                        case 4:
                            self.arr_proveedores[i].direccion = input(Fore.BLUE + "Ingrese la nueva dirección del Proveedor")
                            print(Fore.GREEN + f"\nLa nueva dirreción del Proveedor es {self.arr_proveedores[i].direccion}\n")
                        
                        
                        case 5:
                            
                            self.arr_proveedores[i].correo=validacion_correo()
                            print(Fore.GREEN + f"\nLa nueva dirección de correo del Proveedor es {self.arr_proveedores[i].correo}\n")

                        case 6:
                            bandera=False
                            if not(self.guardar_datos(self.arr_proveedores,"Proveedores.npy")):
                                print(Fore.RED + "El archivo de proveedores no se pudo modificar")
                            else:
                                print(Fore.GREEN + "El archivo de proveedores se ha guardado exitosamente!")
                return True
        return False
    













    

    def main(self) -> None:
        """
        Descripción: Este metodo se encarga de iniciar la aplicación del sistema del minimarket
        
        PARAM:
        
        No aplica
        
        RETURN:
        
        No aplica
        
        """

        
        self.menu_inicial()
        identificacion:int = -1
        contrasena:str = ""
        opcion1:int = 0
        tipo_usuario:int = 0
        

        """
        Aqui empieza el bucle principal del codigo.
        Este bucle principal se compone por varios menus de opciones,
        cada uno con la opc de devolverse al bucle anterior,
        Así que implementamos bucles While identados
        """
       
        
        while (opcion1 != 3) :     
            opcion1 = validacion_opcion_1()
            if (opcion1 ==1):       #Opcion1=1 es iniciar sesion
                tipo_usuario=validacion_tipo_usuario()
                
                
                #__________
                identificacion=validacion_identificacion()
                
                
                #__________________________________Verificación Contraseña
                contrasena=validacion_contrasena()
                
                   
                
                #______________________________Autentificacion
                autenticado:bool
                autenticado = self.autentificar_usuario(tipo_usuario,identificacion,contrasena)
               
                if (autenticado==False):
                    print(Fore.RED + "No se ha podido encontrar el usuario, porfavor intentelo de nuevo")
                    continue
                
 #______________________________________________________________________    Menu administrador       
                match (self.usuario_autenticado.tipo_usuario): #
                    case 1: #En este caso se ejecuta el menú del administrador, con todas sus funcionalidades
                        
                        opc:int=0
                        while (opc !=10):           #Ciclo con opciones de administrador
                            opc= self.menu_administrador()
                            
                                
                            match opc:
                                
                                case 1: #Reigstrar Usuario
                                    usuario_nuevo:Usuario
                                    usuario_nuevo = Usuario()
                                    usuario_registrado:bool
                                    
                                    usuario_registrado = self.registrar_usuario(usuario_nuevo)
                                    if(usuario_registrado):
                                        print(Fore.GREEN + "Usuario registrado")
                                    else:
                                        print(Fore.RED + "No se pudo registrar al Usuario")
                                case 2:  #Registrar cliente
                                    
                                    cliente_nuevo:Cliente
                                    cliente_nuevo=Cliente()
                                    cliente_registrado:bool
                                    
                                    cliente_registrado =self.registrar_cliente(cliente_nuevo)
                                    if(cliente_registrado):
                                        print(Fore.GREEN + "Cliente registrado")
                                        
                                            
                                    else:
                                        print(Fore.RED + "No se pudo registrar al cliente")
                                        
                                case 3: #Consultar Cliente
                                    self.consultar_cliente()
                                case 4: #Modificar cliente
                                    
                                    if self.clientes_registrados ==0:
                                        print("No hay ningun cliente existente, por favor registre uno para empezar")
                                        continue

                                    modificado:bool
                                    
                                    modificado = self.modificar_cliente()
                                    if(modificado):
                                        print(Fore.GREEN + "Cliente modificado")
                                    else:
                                        print(Fore.RED + "No se encontró al cliente")
                                            
                                    

                                case 5:  #Registrar producto
                                    
                                    registrado_producto:bool
                                    producto:Producto
                                    producto = Producto()

                                    registrado_producto = self.registrar_producto(producto)
                                    if (registrado_producto):
                                        print(Fore.GREEN + "Producto registrado")
                                        
                                    else:
                                        print(Fore.RED + "No se registró al producto")

                                #Modificar producto
                                case 6:
                                    self.modificar_producto()
                        
                                case 7: #Registrar Proveedor
                                    
                                    proveedor:Proveedor
                                    proveedor = Proveedor()
                                    registrado_proveedor:bool

                                    registrado_proveedor = self.registrar_proveedor(proveedor)
                                    if(registrado_proveedor):
                                        print(Fore.GREEN + "Proveedor registrado")
                                        
                                    else:
                                        print(Fore.RED + "No se pudo registrar al proveedor")
                                
                                
                                case 8: #Modificar proveedores
                                    self.modificar_proveedor()
                                case 9:  #Actualizar inventario
                                    self.actualizar_inventario()



                                    
                                case 10: #productos más vendidos
                                    
                                    mas_vendidos = self.productos_mas_vendidos()


                                    print(Fore.YELLOW + "\n--------Productos Más Vendidos--------\n")
                                    print("Nombre\t|\tCódigo\t|\tCantidad\t|")

                                    for i in range (len(mas_vendidos)):
                                        print(Fore.WHITE + f"{mas_vendidos[i].nombre}\t\t{mas_vendidos[i].codigo}\t\t{mas_vendidos[i].cantidad_vendida}")
                                        
                                        

                                    
                                case 11:#Productos con menor rotación
                                    
                                    menos_rotacion = self.productos_menor_rotacion()


                                    print(Fore.YELLOW + "\n--------Productos Con Menor Rotación--------\n")
                                    print("Nombre\t|\tCódigo\t|\tCantidad\t|")

                                    for i in range (len(menos_rotacion)):
                                        print(Fore.WHITE + "{menos_rotacion[i].nombre}\t\t{menos_rotacion[i].codigo}\t\t{menos_rotacion[i].cantidad_vendida}")
                                        
                                        

                                
                                case 12:#Productos debajo del stock mínimo
                                    
                                    bajo_stock = self.productos_bajo_stock()


                                    print(Fore.YELLOW + "\n--------Productos Debajo Del Stock Mínimo--------\n")
                                    print("Nombre\t|\tCódigo\t|\tCantidad\t|")

                                    for i in range (len(bajo_stock)):
                                        print(Fore.WHITE + f"{bajo_stock[i].nombre}\t\t{bajo_stock[i].codigo}\t\t{bajo_stock[i].cantidad_vendida}")

                                    

                                #Cerrando sesión.
                                case 13:
                                    print(Fore.WHITE + "...Sesion Cerrada...")
                                    self.usuario_autenticado=None  

                                #Consultar reportes
                    case 2:
                        opcion_cajero:int=0
                        while (opcion_cajero != 7):
                            
                            print(Fore.WHITE + "/////Bienvenido cajero/////")
                            opcion_cajero=self.menu_cajero()
                            
                            match (opcion_cajero):
                                
                                case 1:#Registrar venta
                                    venta_nueva:Venta
                                    venta_nueva = Venta()
                                    venta_registrada:bool
                                    
                                    venta_registrada = self.registrar_venta(venta_nueva)
                                    if (venta_registrada):
                                        print(Fore.GREEN + "Venta registrada")
                                    else:
                                        print(Fore.RED + "No se puedo registrar la venta")
                                        

                                case 2: #Consultar producto
                                    self.consultar_producto()
                                
                                case 3:#Verificar diponibilidad en inventario
                                    self.verificar_disponibilidad_en_inventario()
                                
                                case 4:#Gestionar devoluciones
                                    print("Sin implementar aun")
                                
                                case 5: #Consultar informacion basica de los clientes
                                    self.consultar_cliente()
                                
                                case 6: # Registrar abono
                                    pass
                                    
                                case 7: #Cerrar sesion
                                    print(Fore.WHITE + "...Sesion Cerrada...")
                                    self.usuario_autenticado=None  
                                    
                        self.usuario_autenticado=None

                        #Registrar venta
                        #Consultar producto
                        #Verificar disponibilidad en el inventario
                        #Gestionar devoluciones
                        #Consultar información basica de los clientes
                    case 3:
                        print(Fore.WHITE  + "/////Bienvenido cliente////")
                        opcion_cliente=self.menu_cliente()
                        input("Presione enter para continuar")
                        match opcion_cliente:
                            case 1:
                                self.consultar_historial()
                            case 2:
                                pass
                            case 3:
                                pass
                            case 4:
                                print(Fore.WHITE + "...Sesion Cerrada...")
                                self.usuario_autenticado=None 
                                
                            
                                
                        opcion1=-1
                        self.usuario_autenticado=None

                        #Consultar el histrorial de compras
                        #Ver la factura de una compra especifica
                        #Consultar facturas con saldo pendiente


                #1-Registrar cliente, 2-modificar cliente, 3-Registrar Producto producto, 4-Modificar Producto, 5-Salir
                #Si la opcion es registrarse significa que estamos en presencia de un cliente
                
            if (opcion1 == 2):
                registrado:bool
                cliente:Cliente
                cliente = Cliente()
                registrado = self.registrar_cliente(cliente)
                if(registrado):
                    print(Fore.GREEN + "Cliente registrado")
                    
                else:
                    print(Fore.RED + "No se pudo registrar al cliente")
                    
            
minimarket:Minimarket
minimarket = Minimarket()
minimarket.main()