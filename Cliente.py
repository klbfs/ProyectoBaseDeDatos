from BaseDeDatos import BaseDeDatos 

class Cliente():
    
    listaArgumentos = ['Edad','Estado Socieconomico','Estado Civil','Intereses','Genero','Datos de Contacto','Nombre']
    _listarObjetos = []

    @classmethod
    def listarObjetos(cls, self):
        cls.listarObjetos.append(self.Edad,self.EstadoSocieconomico,self.EstadoCivil,self.Intereses,self.Genero,self.DatosdeContacto,self.Nombre)

    def crearBase():
        BaseDeDatos('Cliente',listaArgumentos)

    def __init__(self):
        


        self.Edad=input('Edad', end = '')
        self.EstadoSocieconomico=input('Estado Socieconomico', end = '')
        self.EstadoCivil=input('Estado Civil', end = '')
        self.Intereses=input('Intereses', end = '')
        self.Genero=input('Genero', end = '')
        self.DatosdeContacto=input('Datos de Contacto', end = '')
        self.Nombre=input('Nombre', end = '')



        BaseDeDatos.agregarDatos('Cliente', [self.Edad,self.EstadoSocieconomico,self.EstadoCivil,self.Intereses,self.Genero,self.DatosdeContacto,self.Nombre])
