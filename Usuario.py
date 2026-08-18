#Este archivo fue trabajado por todos los integrantes del grupo en conjunto por medio de la extension de Visual Studio Code "Live Share"
# Juan Pablo Arruba
# Tomas Castaño Taborda
# Israel Cañizalez Mongua

import numpy as np
from colorama import Fore
from Validaciones import *


class Usuario:
    tipo_usuario:int
    contrasena:str
    identificacion:int
    CAJERO:int = 2
    ADMIN:int= 1
    
    """
    Descripción: Esta clase representa a la persona que va a usar la aplicación, cliente, cajero o administrador. Su constructor esta enfocado
    solamente en cajejro y administrador, cliente tiene su propia clase.
    
    ATRIBUTOS:
    
    tipo_usuario: Un dato de tipo entero que almacena el tipo de usuario, 1 para admnistrador, 2 para cajero y 3 para cliente
    contrasena: Un dato de tipo texto que alcamena la contraseña del usuario
    identificacion: Un dato de tipo entero que almacena la identificación del usuario
    
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
        
        self.tipo_usuario = self.CAJERO
        self.contrasena = ""
        self.identificacion = -1  

    def pedir_datos(self, arr_usuarios:np.ndarray,usuarios_registrados:int) -> None:
        """
        Descripión: Este metodo pide los datos del usuario, realizando verificaciones y validaciones de los datos que ingresa el usuario
        
        PARAM:
        
        lista_usuarios: El arreglo que contiene a todos los usuarios registrados en el sistema, se usa en este metodo para recorrelo y 
        validar y verificar los datos ingresados por el usuario
        
        usuarios_registrados: Un dato de tipo entero que se encarga apuntar a la primera casilla vacia del arreglo de usuario
        
        RETURN:
        
        No aplica
        
        """

        

        #_________________________________Verificacion contraseña
        self.contrasena=validacion_contrasena()

        #___________________________________Verificacion identificacion
        bandera:bool
        bandera=False
        
        cont:int
        cont=0
        
        duplicado:bool
        duplicado=False
        
        while (bandera == False):
            self.identificacion = validacion_identificacion()
            
            duplicado:bool
            duplicado=False
            while duplicado ==False:
                cont=0
                for i in range (usuarios_registrados):
                    if (self.identificacion == arr_usuarios[i].identificacion ):
                        cont+=1
                        break
                if cont ==1 :
                    duplicado=True
                    print(Fore.RED + "Su número de identificación ya esta registrado")
                    self.identificacion=-1
                    break
                
                elif cont ==0:
                    bandera = True
                    print(Fore.GREEN + "\nIdentificación válida\n")
                    break
        
        
    def cambiar_tipo(self,nuevo_tipo:int):
        
        self.tipo_usuario=nuevo_tipo    
    
    
    
    
    #-----reigtrar_proveedor ya se paso, lo borre que aca----#
    
    
    
    
    
    
   
    def modificar_cliente(self,arr_clientes:np.ndarray,clientes_registrados:int) -> bool:
        identificacion:int = -1
        i:int
        while (len(str(identificacion)) > 10 or identificacion < 0 ):
            try:
                identificacion=int(input(Fore.BLUE + "Identificación: "))
                if (len(str(identificacion)) > 10):
                    print(Fore.RED + "La identificación puede tener una longitud máxima de 10 dígitos, intentelo de nuevo")
                if (identificacion < 0):
                    print(Fore.RED + "La identificación debe de ser positiva, intentelo de nuevo de nuevo")
            except ValueError:
                print(Fore.RED + "Usted ingresó un carácter inválido")
        print(Fore.GREEN + "\nIdentificación valida\n")
        for i in range(clientes_registrados):
            if(arr_clientes[i].identificacion == identificacion):
                bandera:bool = True
                while (bandera): 
                    opc:int = 0
                    print(Fore.WHITE + f"""
                    Ingrese una opción entre 1 y 7 para modificar el atributo que desea, ingrese 8 para dejar de modificar
                        
                    1. Nombre: {arr_clientes[i].nombre}
                    2. Tipo de identificación: {arr_clientes[i].tipo_identificacion}
                    3. Identificación: {arr_clientes[i].identificacion}
                    4. Teléfono: {arr_clientes[i].telefono}
                    5. Dirección: {arr_clientes[i].direccion}
                    6. Correo eléctronico: {arr_clientes[i].correo}
                    7. Contraseña: {arr_clientes[i].contrasena}
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
                            arr_clientes[i].nombre = input(Fore.BLUE + "Nombre del cliente: ")
                            print(Fore.GREEN + f"\nNombre del cliente actualizado: {arr_clientes[i].nombre}\n")
                        
                        
                         
                        case 2:
                            while (True):
                                arr_clientes[i].tipo_identificacion = input("Ingrese el nuevo tipo de identificación del cliente").lower().strip()
                                if (arr_clientes[i].tipo_identificacion == "cc" or arr_clientes[i].tipo_identificacion == "ti"):
                                    break
                                else:
                                    print(Fore.RED + "El tipo de identificacion ingresado es invalido, recuerde que debe de ser 'cc' o 'ti', intentelo de nuevo")
                            print(Fore.GREEN + f"\nNuevo tipo de identificación: {arr_clientes[i].tipo_identificacion}\n")
                        
                        
                        
                        case 3:
                            id:int = -1
                            while (id < 0):
                                try:
                                    id=int(input(Fore.BLUE + "Identificación del cliente: "))
                                    if (id < 0):
                                        print(Fore.RED + "La identificación del cliente tiene que ser positiva, intentelo de nuevo")

                                except ValueError:
                                    print(Fore.RED + "la identificación tiene que ser un número entero, intentelo de nuevo")
                                    id= -1
                            arr_clientes[i].identificacion = id
                            print(Fore.GREEN + f"\nLa nueva identificación es {arr_clientes[i].identificacion}\n")
                        
                        
                        case 4:
                            telefono:int = -1 
                            while (telefono < 0):
                                try:
                                    telefono=int(input(Fore.BLUE + "Ingrese el número de teléfono del cliente"))
                                    if (telefono < 0):
                                        print(Fore.RED + "El número de teléfono tiene que ser positivo, intentelo de nuevo")
                                    telefono = str(telefono)
                                    if( len(telefono)>10 or len(telefono)<10):
                                        print(Fore.RED + "El número de teléfono debe tener exactamente 10 dígitos, ingreselo de nuevo")
                                        telefono=-1
                                    telefono=int(telefono)
                                    
                                except ValueError:
                                    print(Fore.RED + "Usted no ingresó un número, intentelo de nuevo")
                                    telefono = -1
                            arr_clientes[i].telefono = telefono
                            print(Fore.GREEN + f"\nEl nuevo número de teléfono del cliente es {arr_clientes[i].telefono}\n")
                            
                        
                        case 5:
                            arr_clientes[i].direccion = input(Fore.BLUE + "Ingrese la nueva dirección del Cliente")
                            print(Fore.GREEN + f"\nLa nueva dirreción del cliente es {arr_clientes[i].direccion}\n")
                        
                        
                        case 6:
                            correo=""
                            while ("@" not in correo) or (".co" not in correo):
                                correo = input(Fore.BLUE + "Por favor ingrese el correo eléctronico del cliente: ")
                                if ("@" not in correo) or (".co" not in correo):
                                    print(Fore.RED + "correo eléctronico debe de tener estrictamente @ y terminar en .co")
                            arr_clientes[i].correo=correo
                            print(Fore.GREEN + f"\nLa nueva dirección de correo del cliente es {correo}\n")
                        
                        
                        case 7:
                            contrasena:str = ""
                            while ( (len(contrasena) <8 or len(contrasena)> 15) or (" " in contrasena) ):
                                contrasena=input(Fore.BLUE + "Ingrese la nueva contraseña, esta debe tener mínimo 8 carácteres y máximo 15 carácteres, además la contraseña no debe tener ningún espacio: ")
                                if ( len(contrasena) < 8 ):
                                    print(Fore.RED + "La contraseña debe tener una lontitud mínima de 8 carácteres, intentelo de nuevo")
                                elif (len(contrasena) > 15):
                                    print(Fore.RED + "La contraseña puede tener una longitud máxima de 15 carácteres, intentelo de nuevo")
                                
                                if (" " in contrasena):
                                    print(Fore.RED + ("La contraseña no puede tener espacios, intentelo de nuevo"))
                            arr_clientes[i].contrasena=contrasena
                            print(Fore.GREEN + f"\nLa nueva contraseña del cliente es {arr_clientes[i].contrasena}\n")
                        case 8:
                            bandera=False
                            
                return True
        return False