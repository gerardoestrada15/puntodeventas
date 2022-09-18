import sqlite3

database= sqlite3.connect('pizzeria.db')
print(database)

cursor=database.cursor()


class Usuario:
    def __init__(self,nombre,email,password):
        self.nombre = nombre
        self.email = email
        self.password = password
    
    def registrar(self):
        sqlite =  "INSERT INTO usuarios VALUES(?,?,?)"
        usuario = (self.nombre, self.email, self.password)
        print("Registro exitoso")


        
    def identificar(self):
        sql = "SELECT * FROM usuarios WHERE email= ? AND pass= ? "
         
         
        usuario= (self.email, self.password)
       
         
        cursor.execute(sql,usuario)
        result = cursor.fetchone()
         
        return result