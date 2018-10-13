from BaseDeDatos import BaseDeDatos 

class Contacto():
    
    listaArgumentos = ['Telefono'.'Fax','CorreoElectronico'.'Whatsapp']
    _listarObjetos = []

    @classmethod
    def listarObjetos(cls, self):
        cls.listarObjetos.append(self.Telefono,self.RedesSociales,self.Fax,self.CorreoElectronico,self.Whatsapp)

    def crearBase():
        BaseDeDatos('Contacto',listaArgumentos)

    def __init__(self):
        

        self.Telefono = input('Telefono ', end = '')
        self.RedesSociales = input('Redes Sociales ', end = '')
        self.Fax = input('Fax ', end = '')
        self.CorreoElectronico= input('Correo Electronico ', end = '')
        self.Whatsapp = input('Whatsapp ', end = '')
        
        BaseDeDatos.agregarDatos('Contacto', [self.Telefono,self.RedesSociales,self.Fax,self.CorreoElectronico,self.Whatsapp])
