

from tkinter import *
#from funciones import funciones
import ControladorDeObjeto as ControladorDeObjeto




def login():
	b=Tk()
	en1=Label(b, text="Usuario").grid(row=0,column=0)
	
	en2=Label(b, text="Contrasena").grid(row=1, column=0)
	variable=str()
	
	us1= Entry(b, text=variable).grid(row=0,column=1)
	
	variable1=int()
	pwd= Entry(b,show="*", text=variable1).grid(row=1,column=1)
	
	ce=Label(b, text="Crear cuenta").grid(row=2, column=0)
	en11=Label(b, text="usuario:").grid(row=3,column=0)
	
	en22=Label(b, text="contrasena").grid(row=4, column=0)
	variable2=str()
	
	us2=Entry(b, text=variable2).grid(row=3, column=1)
	variable3=int()
	pwd2=Entry(b,show="*",text=variable3).grid(row=4, column=1)
	
	if (variable) == (variable2) and (variable1 == variable3 ):
	
		print ("Login")

		
	else:
		j=Label(b, text="Login failed").grid(row=6,column=0)

	submit=Button(b, text="SUBMIT", command=b.destroy).grid(row=5,column=1)
	
		

	b.mainloop()

	
def batributos():
	ventana12=Toplevel()
	
	aae=Label(ventana12, text="tipo empresa, sector economico, razon social, tamano, exportaciones, importaciones, asociaciones, inversionistas, accionistas")
	aae.pack()
def buscadoratributos():
	ventana1000=Toplevel()
	bu13=Label(ventana1000, text="nombre, ubicacion, categoria,buscadorinternet, sucursales, filtros busqueda, tiempo busqueda, subempresas, historial")
	bu13.pack()
def capital():
	ventana140=Toplevel()

	v14=Label(ventana140, text="presupuesto inicial, gasto anual total, prestamos, \n recursos humanos, recursos materiales, aportaciones PIB, \n Subsidios, donativos, relaciones economicas, listar objetos")
	v14.pack()
def cliente():
	ventana150=Toplevel()
	v15=Label(ventana150, text="edad, edo socioeconomico, edo civil, intereses, genero,\n datos contacto, nombre")
	v15.pack()
def empre():
	ventana160=Toplevel()
	v16=Label(ventana160, text="nombre usuario, descripcion, departamentos, \n posiciones, productos, legal, no.empleados,\n mision, vision, recursos, capital, listar objetos")
	v16.pack()
def esta():
	ventana170=Toplevel()
	v17=Label(ventana170, text="opciones comparacion, graficos, informaciondatos, resenas, no. opiniones\n contrataciones, despidos, tamanoempresa, crecimiento, listar objetos")
	v17.pack()
def inst():
	ventana180=Toplevel()
	v18=Label(ventana180, text="centro de distribucion, centro produccion, manufactura, ensamble\n centro de investigacion y servicios, sucursales, sedes, almacenes\nlistar objetos")
	v18.pack()

def le():
	ventana1500=Toplevel()
	v15=Label(ventana1500, text="CEO, CTO, mesa directiva, jede departamento, empresa\n presidente, accionistas mayoritarios, listar objetos")
	v15.pack()

def imagenesyv():

	ventana1100=Toplevel()
	v15=Label(ventana1100, text="imagenes y video, fotos del lugar, logotipo, productos, publicidad, tipos publicidad\nsimulacion del producto, conferencias, videos informativos, listar objetos")
	v15.pack()
def infoempresa():

	ventana190=Toplevel()
	v15=Label(ventana190, text="nombre, tel, fax, carreras, foros, conferencias\n newsletter, publicaciones, politicas de privacidad, fecha de fundacion, cooreo, listar objetivos")
	v15.pack()
def ubi():

	ventana225=Toplevel()
	v225=Label(ventana225, text="pais, edo, municipio, localidad, calle, numero, CP, coordenadas, sucursales, area geografica")
	v225.pack()
def redesociales():
	ventana35=Toplevel()
	v35=Label(ventana35, text="Facebook, Twitter, Instagram, LinkedIn, Youtube,e mail, ventas en linea, Skype, listar objetos")
	v35.pack()
def fun():
	ventana35=Toplevel()
	v35=Label(ventana35, text="nombre, clave, contrasena, indentificacion seccion, puesto,codigo nivel, racha de contribucion\n, modificacion reciente, ultima sesion, usuario normal")
	v35.pack()
def depa():
	ventana35=Toplevel()
	v35=Label(ventana35, text="no. empleados, investigacion,logistica, distribucion\n recursos humanos, seguridad, finanzas, legal\n ventas, publicidad, atenciona clientes")
	v35.pack()
def Clases():
	v3=Toplevel(root)
	
	e24=Button(v3, text="Actividad Economica", command=batributos)
	e25=Button(v3, text="Buscador", command=buscadoratributos)
	e26=Button(v3, text="Capital", command=capital)
	e2222=Button(v3,text="cliente",command=cliente)
	e2222.pack()
	e27=Button(v3, text="Departamentos", command=depa)
	e28=Button(v3, text="Empresa", command=empre)
	e29=Button(v3, text="Estadisticas", command=esta)
	e30=Button(v3, text="Cuenta administrador",command=fun)
	e31=Button(v3, text="Instalaciones", command=inst)
	e45=Button(v3, text="Lideres empresariales", command=le)
	e32=Button(v3, text="Imagenes y Video", command=imagenesyv)
	e33=Button(v3, text="Informacion de la Empresa", command=infoempresa)
	e34=Button(v3, text="Ubicacion", command=ubi)
	e35=Button(v3, text="Redes Sociales", command=redesociales)
	e24.pack()
	e25.pack()
	e45.pack()
	e26.pack()
	e27.pack()
	e28.pack()
	e29.pack()
	e30.pack()
	e31.pack()
	e32.pack()
	e33.pack()
	e34.pack()
	e35.pack()


def Atributos():
	v2=Toplevel(root)
	entradaen=Entry(v2, text="hola")
	entradaen.pack()	
	

	
def Tecnicas_Prog():

	otra_v=Toplevel(root)
	e1=Label(otra_v, text="Profesor: Emiliavo Nava")
	e1.pack()
	e2=Label(otra_v, text="Grupo 2")
	e3=Label(otra_v,text="Horario: \n Lunes: 7:00 - 9:00 \n Miercoles: 7:00 - 9:00 \n Viernes 7:00 - 9:00")
	e4=Label(otra_v, text="Semestre: 2019-1")
	e2.pack()
	e3.pack()
	e4.pack()
def Referencias():
	print("URL: http://www.beta.inegi.org.mx/temas/directorio/")

def MenuBusqueda():
	print("Clase Menu Busqueda")
def Lideres():
	print("https://www.inegi.org.mx/app/mapa/denue/")

	
root = Tk()


bienvenida= Label(root, text="Bienvenido a la Pagina Oficial del INEGI",bg="grey50",fg="white",  font='Helvetica 14 bold')
bienvenida.pack(side=TOP, fill=X)
modulo= Label(root, text="EMPRESAS",bg="white",fg="navy", font='Helvetica 18 bold')
modulo.pack(side=TOP, fill=X)

menu = Menu(root)
root.config(menu=menu)

subMenu1 = Menu(menu)


menu.add_cascade(label="Usuario", menu=subMenu1,)

subMenu1.add_command(label="Nombre", command= login)
subMenu1.add_separator()
subMenu1.add_command(label="Salir", command= root.quit)

subMenu2= Menu(menu)

menu.add_cascade(label="Informacion Proyecto", menu=subMenu2)
subMenu2.add_command(label="Clases", command= Clases )

subMenu2.add_separator()
subMenu2.add_command(label="Tecnicas de Programacion", command= Tecnicas_Prog)

subMenu3 = Menu(menu)

menu.add_cascade(label="INEGI", menu=subMenu3)
subMenu3.add_command(label="Referencias", command= Referencias)
subMenu3.add_separator()



#TOOLBAR ****

toolbar = Frame(root, bg="medium aquamarine")
insertar4=Button(toolbar, text="Imagenes y video", command=Lideres, bg="white", fg="medium aquamarine")
insertar4.pack(side=LEFT, padx=2, pady=2, ipadx=23)
toolbar.pack(side=TOP, fill=X)
#STATUS BAR***
espacio=Label(root, text="")
espacio1=Label(root, text="")
espacio2=Label(root, text="")
espacio3=Label(root, text="")
espacio4=Label(root, text="")
espacio5=Label(root, text="")
espacio6=Label(root, text="")
espacio.pack()
elegir=Label(root,text="Escriba la opcion deseada", font='Helvetica 14 bold', bg="gray80")
opcion=Entry(root)
elegir.pack(fill=X)
espacio1.pack()
opcion.pack()
espacio3.pack()
def Busqueda():
	b=Button(text="EDITAR", command=ControladorDeObjeto.editarObjeto)    #def funcion de editar
	b1= Button(text="MOSTRAR")
	b2= Button(text="ELIMINAR", command=ControladorDeObjeto.borrarObjeto)
	b3= Button(text="AGREGAR", command=ControladorDeObjeto.crearObjeto)
	b.pack()
	b1.pack()
	b2.pack()
	b3.pack()

Boton1=Button(text="Buscar",fg="white",bg="navy",font='Helvetica 14 bold', command=Busqueda)
Boton1.pack(padx=65,ipady=2)
espacio4.pack()
espacio5.pack(fill=X)
espacio6.pack()



status = Label(root, text="Todos los Derechos Reservados. Tecnicas de Programacion 2019", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()
