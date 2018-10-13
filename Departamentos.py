from BaseDeDatos import BaseDeDatos 

class Departamentos():
    
    listaArgumentos = ['']
    _listarObjetos = []

    @classmethod
    def listarObjetos(cls, self):
        cls.listarObjetos.append(self.NumerodeEmpleados,self.Investigacion,self.Logistica,self.Distribucion,self.RecursosHumanos,self.Publicidad,self.Seguridad,self.Finanzas,self.Legal,self.Ventas,self.AtencionCliente)

    def crearBase():
        BaseDeDatos('Departamentos',listaArgumentos)

    def __init__(self):
        


        self.NumerodeEmpleados=input('Numero de Empleados', end = '')
        self.Investigacion=input('Departamento de Investigacion', end = '')
        self.Logistica=input('Departamento de Logistica', end = '')
        self.Distribucion=input('Departamento de Distribucion', end = '')
        self.RecursosHumanos=input('Departamento de Recursos Humanos', end = '')
        self.Seguridad=input('Departamento de'Seguridad, end = '')
        self.Finanzas=input('Departamento de'Finanzas, end = '')
        self.Legal=input('Area Legal', end = '')
        self.Ventas=input('Departamento de Ventas', end = '')
        self.Publicidad=input('Departamento de Publicidad', end = '')
        self.AtencionaCliente=input('Atencion al ClienteCliente', end = '')


        BaseDeDatos.agregarDatos('Departamentos', [self.NumerodeEmpleados,self.Investigacion,self.Logistica,self.Distribucion,self.Recursos Humanos,self.Publicidad,self.Seguridad,self.Finanzas,self.Legal,self.Ventas,self.AtencionCliente])
