from usuarios import acciones

print("***Bienvenido al punto de ventas,seleccina la opcion que requieres***********")
print("1.Iniciar sesion\n2.Registrar usuario")

opcion= (input(" "))

haz=acciones.Acciones()

if opcion=="1":
    haz.login()
    haz.menu()

elif opcion=="2":
    haz.registro()
    print("Inicia Sesion")
    haz.login()
    haz.menu()
   
    
    