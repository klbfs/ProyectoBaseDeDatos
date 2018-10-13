from BaseDeDatos import BaseDeDatos 

class RedesSociales():
    
    listaArgumentos = ['Facebook'.'Twitter','Instagram','Youtube','LinkedIn','CorreoElectronico','VentasenLinea','Skype']
    _listarObjetos = []

    @classmethod
    def listarObjetos(cls, self):
        cls.listarObjetos.append(self.Facebook,self.Twitter,self.Instagram,self.LinkedIn,self.Youtube,self.CorreoElectronico,self.VentasenLinea,self.Skype)

    def crearBase():
        BaseDeDatos('RedesSociales',listaArgumentos)

    def __init__(self):
        
        self.Facebook = input('Perfil de Facebook ', end = '')
        self.Twitter = input('Usuario de Twitter', end = '')
        self.Instagram = input('Cuenta de Instagram ', end = '')
        self.LinkedIn = input('Nombre de Empresa en LinkedIn ', end = '')
        self.Youtube = input('Canal de Youtube ', end = '')
        self.CorreoElectronico = input('Correo Electronico de Contacto ', end = '')
        self.VentasenLinea = input('Pagina WEB de ventas en linea ', end = '')
        self.Skype = input('Nombre de Usuario de Skype', end = '')

        
        BaseDeDatos.agregarDatos('RedesSociales', [self.Facebook,self.Twitter,self.Instagram,self.LinkedIn,self.Youtube,self.CorreoElectronico,self.VentasenLinea,self.Skype])
