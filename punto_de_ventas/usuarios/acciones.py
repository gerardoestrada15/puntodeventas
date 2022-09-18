import usuarios.usuario as modelo
import articulos.acciones

class Acciones:
    def registro(self):
      print("Crearemos tu user")
      print("Ingresa tu nombre, email y contraseña")
      nombre=(input("Nombre: "))
      email=(input("Email: "))
      password=(input("Cotraseña: "))
      
      usuario = modelo.Usuario(nombre, email, password)
      registro = usuario.registrar()
        
    def login(self):
      email=(input("Email: "))
      password=(input("Contraseña: "))
        
      usuario = modelo.Usuario('', email, password)
      login = usuario.identificar()
      
      
            
    def menu(self):
          print("Selecciona la opcion que requieres hacer:\n1:Agregar articulos\n2:Mostrar todo el inventario\n3:Borrar Articulos \n4:Cobrar una mesa\n5.Salir")
          accion = (input("Digita el numero de la opcion que quieres realizar: "))
          
          haz = articulos.acciones.Acciones()
          
          if accion == "1":
                haz.crear_articulos()
                print("Agrega los articulos")
                self.menu()
                print("Articulos agregados!")
          elif accion =="2":
                haz.mostrar()
                self.menu()
          elif accion == "3":
                print("Borrar")
                haz.borrar()
                print("Articulo eliminado correctamente")
                self.menu()
          elif accion == "4":
                print("Vamos a cobrar")
                haz.cobrar()
                self.menu()
          elif accion =="5": 
                exit()
          
        
        