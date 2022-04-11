peticion = [
    'Crea tu nombre de perfil: ', 
    'ingresa tu carrera: ', 
    'ingresa tu email: ', 
    'ingresa tu contraseña: '
]  

# funcion para registrarse al iniciar
def registrarse(): 
    nombre = str(input(peticion[0]))
    carrera = str(input(peticion[1]))
    email = str(input(peticion[2]))
    contraseña = str(input(peticion[3]))

    class User:
        def __init__(self, name, career, email, contraseña):
            self.name = name
            self.career = career
            self.email = email
            self.password = contraseña
        
        def saludar(self):
            print('Hola, soy ' + self.name + ' y estudio ' + self.career)
            print(self.email, self.password)

    diego = User(nombre, carrera, email, contraseña)
    diego.saludar()
        
registrarse()


# def iniciarSesion():
#     email = str(input(peticion[2]))
#     contraseña = str(input(peticion[3]))

#     if (email == user.mail and contraseña == user.contraseña):
#         print('bienvenido')    
#     else:
#         print('error')

# iniciarSesion()
    
# print(p1.nombre)
# print(p1.carrera)
# print(p1.email)
# print(p1.contraseña)