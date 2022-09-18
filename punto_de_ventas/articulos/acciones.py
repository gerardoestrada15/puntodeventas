from re import I
import articulos.articulo as modelo
from datetime import datetime
import sqlite3



database = sqlite3.connect('articulos.db')
cursor = database.cursor()

class Acciones:
    
    def crear_articulos(self):
        print(f"Vamos a agregar un articulo")
        pizza=input("ïntroduce el nombre de la pizza: ")
        precio=int(input("Introduce el precio de la pizza: "))
        descripcion=input("Introduce la descripcion de la pizza: ")
        fecha = datetime.now()
        
        articulo = modelo.Articulo(pizza,precio,descripcion,fecha)
        guardar = articulo.guardar_articulo()
    
        print(f"Guardaste la pizza")
        
    def mostrar(self):
        print("Aqui estan todos los articulos")
        
        articulo = modelo.Articulo(" "," "," "," ")
        articulos=articulo.listar()
        
        for articulo in articulos:
            print("----------------------")
            print("Pizza: ", articulo[0])
            print("Precio: ",articulo[1])
            print("Descripcion:", articulo[2])
            print("Fecha en que se agrego: ", articulo[3])
            #print("-----------------------")
            
    def borrar(self):
        print("Vamos a borrar un articulo")
        
        
        pizza = input("Introduce la pizza que quieres borrar: ")
        
        articulo= modelo.Articulo(" "," "," "," ")
        eliminar= articulo.eliminar(pizza)
        
    def cobrar(self):
        print("Seleccionaste cobrar")
        
        mesa=input("Cual es la mesa que vas a cobrar?: ")
        fecha = datetime.now()
        pizza=input("Introduce la pizzas que quieres buscar para cobrar: ")
        pizza2=input("Introduce la pizzas que quieres buscar para cobrar: ")
        
         
        articulo=modelo.Articulo(" "," "," "," ")
        articulos=articulo.sumar_articulos(pizza)
      
        articulos1=articulo.sumar_articulos(pizza2)
        
        
         
        for articulo in articulos:
          print("----------------------")
          print("***IMPRIMIENDO RECIBO***")
          print("Pizza: ", articulo[0])
          print("Precio: ",articulo[1])
         

        for articulo in articulos1:
          print("Pizza: ", articulo[0])
          print("Precio: ",articulo[1])
          print("TOTAL: ",articulo[1]+articulo[1])
          print("Mesa No.:",mesa)
          print("Fecha de la compra:",fecha)
        
        
       
        
          
          
        
        ##articulo=modelo.Articulo(" "," "," "," ")
        ##sumar=articulos.sum_articulos(pizza,precio)