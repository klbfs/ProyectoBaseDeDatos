from BaseDeDatos import BaseDeDatos 

class RazonSocial():
    
    listaArgumentos = ['Individual','SociedadColectiva','SociedadAnonima','SociedadResponsable','SociedadComandataria','EmpresaUnipersonal','SociedadAnonimaCerrada']
    _listarObjetos = []

    @classmethod
    def listarObjetos(cls, self):
        cls.listarObjetos.append(self.Individual,self.SociedadColectiva,self.SociedadAnonima,self.SociedadResponsable,self.SociedadComandataria, self.EmpresaUnipersonal,self.corporativo,self.SociedadAnonimaCerrada)

    def crearBase():
        BaseDeDatos('RazonSocial',listaArgumentos)

    def __init__(self):
        


        self.Individual=input('Empresa Individual', end = '')
        self.SociedadColectiva=input('Sociedad Colectiva ', end = '')
        self.SociedadAnonima=input('Sociedad Anonima ', end = '')
        self.SociedadResponsable=input('Sociedad Responsable ', end = '')
        self.SociedadComanditaria=input('Sociedad Comanditaria ', end = '')
        self.SociedadAnonimaCerrada=input('Sociedad Anonima Cerrada ', end = '')
        self.EmpresaUnipersonal=input('Empresa Unipersonal', end = '')

        BaseDeDatos.agregarDatos('RazonSocial', [self.Individual,self.SociedadColectiva,self.SociedadAnonima,self.SociedadResponsable,self.SociedadComandataria, self.EmpresaUnipersonal,self.corporativo,self.SociedadAnonimaCerrada])
