from BaseDeDatos import BaseDeDatos 

class ActividadEconomica():
    
    listaArgumentos = ['TipodeEmpresa', 'SectorEconomico', 'RazonSocial', 'Exportaciones','Tamano','Importaciones','Asociaciones','Inversionistas','Accionistas']
    _listarObjetos = []

    @classmethod

    def regresarArgumentos(cls):
        return cls.listaArgumentos

    @classmethod
    def regresarObjeto(cls, nombreObjeto):
        for objeto in cls._listaObjetos:
            if objeto.TipodeEmpresa == nombreObjeto:
                return objeto

    @classmethod
    def eliminarObjeto(cls, objet):
        for objeto in cls._listaObjetos:
            if objeto == objet:
                cls._listaObjetos.remove(objet)
    
    @classmethod
    def editarArgumento(cls, argumento, objeto, dato):
        if argumento == 'TipodeEmpresa':
            for obj in cls._listaObjetos:
                if obj == objeto:
                    cls._listaObjetos[cls._listaObjetos.index(obj)].TipodeEmpresa = dato

    @staticmethod
    def crearPrevios():
        listas = BaseDeDatos.obtenerDatosTotales('TipodeEmpresa')
        for lista in listas:
            ActividadEconomica(lista)

    def listarObjetos(cls, objeto):
        cls.listarObjetos.append(objeto)

    def crearBase():
        BaseDeDatos('ActividadEconomica',self.listaArgumentos)

    def __init__(self, modo = None):

        if modo == 1;
        


            self.TipodeEmpresa=input('Tipo de Empresa')
            self.SectorEconomico=input('Sector Economico ')
            self.RazonSocial=input('Razon Social')
            self.Tamano=input('Tamano de le Empresa')
            self.Exportaciones=input('Numero de Exportaciones')
            self.Importaciones=input('Numero de Importaciones ')
            self.Asociaciones=input('Asociaciones')
            self.Inversionistas=input('Inversionistas')
            self.Accionistas=input('Accionistas')

            BaseDeDatos.agregarDatos('ActividadEconomica', [self.TipodeEmpresa,self.SectorEconomico,self.RazonSocial,self.Exportaciones,self.Importaciones, self.Tamano,self.Asociaciones,self.Inversionistas,self.Accionistas], self.listaArgumentos)
       

        else modo != None:

            self.TipodeEmpresa= modo[0]
            self.SectorEconomico= modo[1]
            self.RazonSocial= modo[2]
            self.Tamano= modo[3]
            self.Exportaciones= modo[4]
            self.Importaciones= modo[5]
            self.Asociaciones= modo[6]
            self.Inversionistas= modo[7]
            self.Accionistas= modo[8]
            self.listarObjetos(self)

            
        else:
            self.crearBase()
