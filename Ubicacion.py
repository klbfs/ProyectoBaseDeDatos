from BaseDeDatos import BaseDeDatos 

class Ubicacion():
    
    listaArgumentos = ['Pais', 'Estado', 'Municipio', 'Localidad', 'Calle', 'Numero', 'CodigoPostal', 'CoordenadasGeograficas','Sucursales','AreaGeografica']
    _listarObjetos = []

    @classmethod
    def listarObjetos(cls, self):
        cls.listarObjetos.append(self.Pais,self.Estado,self.Municipio,self.Localidad,self.Calle,self.Numero,self.CodigoPostal,self.CoordenadasGeograficas,self.Sucursales,self.AreaGeografica )

    def crearBase():
        BaseDeDatos('Ubicacion',self.listaArgumentos)

    def __init__(self):
        

        self.Pais = input('Pais de Origen ', end = '')
        self.Estado = input('Estado ', end = '')
        self.Municipio = input('Municipio ', end = '')
        self.Localidad = input('Localidad ', end = '')
        self.Calle = input('Calle ', end = '')
        self.Numero = input('Numero Exterior ', end = '')
        self.CodigoPostal = input('Codigo Postal ', end = '')
        self.CoordenadasGeograficas = input('Coordenada Geograficas de Sede ', end = '')
        self.Sucursales = input('Direccion de Sucursales ', end = '')
        self.AreaGeografica = input('Area Geografica comercial ', end = '')
        
        BaseDeDatos.agregarDatos('Ubicacion', [self.Pais,self.Estado,self.Municipio,self.Localidad,self.Calle,self.Numero,self.CodigoPostal,self.CoordenadasGeograficas,self.Sucursales,self.AreaGeografica])
