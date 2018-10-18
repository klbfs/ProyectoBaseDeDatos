from BaseDeDatos import BaseDeDatos 

class LideresEmpresariales():
    
    listaArgumentos = ['CEO','CTO','MesaDirectiva','JefeDepartamento','Empresa','Presidente','AccionistasMayoritarios']
    _listaObjetos = []

    @classmethod
    def regresarArgumentos(cls):
        return cls.listaArgumentos

    @classmethod
    def regresarObjeto(cls,argumento, nombreObjeto):
        for objeto in cls._listaObjetos:
            cadena = eval('objeto.'+argumento)
            if cadena == nombreObjeto: 
                return objeto

    @classmethod
    def eliminarObjeto(cls, objet):
        for objeto in cls._listaObjetos:
            if objeto == objet:
                cls._listaObjetos.remove(objet)
    
    @classmethod
    def editarArgumento(cls, argumento, objeto, dato):
       for arg in cls.listaArgumentos:
                if argumento == arg:
                    for obj in cls._listaObjetos:
                        if obj == objeto:
                            eval('cls._listaObjetos[cls._listaObjetos.index(obj)].'+argumento+' = dato')

    @staticmethod
    def crearPrevios():
        listas = BaseDeDatos.obtenerDatosTotales('LideresEmpresariales')
        for lista in listas:
            LideresEmpresariales(lista)

    @classmethod
    def listarObjetos(cls, objeto):
        cls._listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('LideresEmpresariales',self.listaArgumentos)

    def __init__(self, modo = None):
        
        if modo == 1:
            self.CEO = input('Nombre de Usuario: ')
            self.CTO = input('id: ')
            self.MesaDirectiva = input('Password: ')
            self.JefeDepartamento = input('Correo: ')
            self.Empresa = input('Intereses: ')
            self.Presidente = input('Ocupacion: ')
            self.AccionistasMayoritarios = input('Descripcion: ')
            self.listarObjetos(self)
            BaseDeDatos.agregarDatos('LideresEmpresariales', [self.CEO,self.CTO,self.MesaDirectiva,self.JefeDepartamento,self.Empresa,self.Presidente,self.AccionistasMayoritarios], self.listaArgumentos)
        elif modo != None:
            self.CEO = modo[0]
            self.CTO = modo[1]
            self.MesaDirectiva = modo[2]
            self.JefeDepartamento = modo[3]
            self.Empresa = modo[4]
            self.Presidente = modo[5]
            self.AccionistasMayoritarios = modo[6]
            self.listarObjetos(self)
        else:
            self.crearBase()
