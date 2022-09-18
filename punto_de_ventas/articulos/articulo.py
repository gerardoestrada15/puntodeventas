import sqlite3

database = sqlite3.connect('articulos.db')
cursor = database.cursor()

class Articulo:
    def __init__(self,pizza,precio,descripcion,fecha):
        self.pizza=pizza
        self.precio=precio
        self.descripcion=descripcion
        self.fecha=fecha
        
    def guardar_articulo(self):
        sql = 'INSERT INTO articulos VALUES(?,?,?,?)'
        articulo = (self.pizza,self.precio,self.descripcion,self.fecha)
        
        cursor.execute(sql,articulo)
        database.commit()
        
    def listar(self):
        sql= f"SELECT *FROM articulos"
        cursor.execute(sql)
        result =cursor.fetchall()
        
        return result
    
    def eliminar(self,pizza):
        sql = f"DELETE FROM articulos WHERE pizza ='"+str(pizza)+"'"
        cursor.execute(sql)
        database.commit()
        
    def sumar_articulos(self,pizza):
        sql = f"SELECT *FROM articulos WHERE pizza ='"+str(pizza)+"'"
        cursor.execute(sql)
        result = cursor.fetchall()
        
        return result  
      
        
        
        