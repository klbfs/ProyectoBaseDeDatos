from BaseDeDatos import BaseDeDatos 

class Menu():
    
    listaArgumentos = ['Empresas','Sectores','BusquedaEmpresarial','BusquedaEspecializada','CalificaciondeServicios','IniciarSesion', 'MasBuscados', 'BusquedaGeografica','Imagenes']
    _listarObjetos = []

    @classmethod
    def listarObjetos(cls, self):
        cls.listarObjetos.append(self.Empresas,self.Sectores,self.BusquedaEmpresarial,self.BusquedaEspecializada,self.CalificaciondeServicios,self.IniciarSesion,self.MasBuscados,self.BusquedaGeografica,self.Imagenes)

    def crearBase():
        BaseDeDatos('Menu',listaArgumentos)

    def __init__(self):
        

        self.Empresas = input('Listado de Empresas', end = '')
        self.Sectores = input('Empresas por Sector Economico', end = '')
        self.BusquedaEmpresarial = input('Busqueda Empresarial', end = '')
        self.BusquedaEspecializada = input('Busqueda Especializada', end = '')
        self.CalificaciondeServicios = input('Listado de Calificacion de Servicios', end = '')
        self.IniciarSesion = input('Inicio de Sesion', end = '')
        self.MasBuscados = input('Mas Buscados', end = '')
        self.Busquedageografica = input('Busqueda Geografica', end = '')
        self.Imagenes = input('Imagenes', end = '')

        
        BaseDeDatos.agregarDatos('Menu', [self.Empresas,self.Sectores,self.BusquedaEmpresarial,self.BusquedaEspecializada,self.CalificaciondeServicios,self.IniciarSesion,self.MasBuscados,self.BusquedaGeografica,self.Imagenes])
