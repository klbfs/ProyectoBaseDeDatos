from BaseDeDatos import BaseDeDatos 

class ActividadEconomica():
    
    listaArgumentos = ['Tipo de Empresa', 'Sector Economico', 'Razon Social', 'Exportaciones','Tamano','Importaciones','Asociaciones','Inversionistas','Accionistas (Socios Comerciales)']
    _listarObjetos = []

    @classmethod
    def listarObjetos(cls, self):
        cls.listarObjetos.append(self.TipodeEmpresa,self.SectorEconomico,self.RazonSocial,self.Exportaciones,self.Importaciones, self.Tamano,self.Asociaciones,self.Inversionistas,self.Accionistas)

    def crearBase():
        BaseDeDatos('ActividadEconomica',listaArgumentos)

    def __init__(self):
        


        self.TipodeEmpresa=input('Tipo de Empresa', end = '')
        self.SectorEconomico=input('Sector Economico ', end = '')
        self.RazonSocial=input('Razon Social', end = '')
        self.Tamano=input('Tamano de le Empresa', end = '')
        self.Exportaciones=input('Numero de Exportaciones', end = '')
        self.Importaciones=input('Numero de Importaciones ', end = '')
        self.Asociaciones=input('Asociaciones', end = '')
        self.Inversionistas=input('Inversionistas', end = '')
        self.Accionistas=input('Accionistas', end = '')

        BaseDeDatos.agregarDatos('ActividadEconomica', [self.TipodeEmpresa,self.SectorEconomico,self.RazonSocial,self.Exportaciones,self.Importaciones, self.Tamano,self.Asociaciones,self.Inversionistas,self.Accionistas])
