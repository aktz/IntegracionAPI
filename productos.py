import pymysql
import os


class App:

	def __init__(self):
		self.conn = pymysql.connect(
			host='localhost',
			user='root',
			password = "",
			db='integracionapi',
			)
		self.cursor = self.conn.cursor()

	def Insertar(self):
		Codigo = input("Ingrese el código del producto: \n")
		Descripcion = input("Ingrese una descripción del producto, por favor no utilice carateres especiales: \n")
		PrecioCompra = input("Ingrese el precio del producto: \n")
		PrecioVenta = input("Ingrese el precio de venta del producto: \n")
		Inventario = input("Ingrese el número de inventario del producto: \n")
		Categoria = input("Ingrese el ID de la categoría del producto: \n")
		Proveedor = input("Ingrese el ID del proveedor: \n")

		sql = "insert into productos(Codigo,Descripcion,PrecioCompra,PrecioVenta,Inventario,Categoria,Proveedor) values('{}','{}','{}','{}','{}','{}','{}')".format(Codigo,Descripcion,PrecioCompra,PrecioVenta,Inventario,Categoria,Proveedor)
		self.cursor.execute(sql)
		print("Datos del producto ingresados correctamente")
		self.conn.commit()
		os.system('pause')

aplication = App()
aplication.Insertar()


