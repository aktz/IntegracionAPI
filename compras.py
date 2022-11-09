from pydantic import BaseModel
import Conexion


class Compras(BaseModel):
    Id: int
    Fecha: float
    Producto: int
    Cantidad: int
    Precio: int
    ValorTotal: int

    def __str__(self):
        datos=self.consulta_compras()        
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
        
    def consulta_compras(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM compras")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_compras(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM compras WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta_compras(self,Fecha, Producto, Cantidad, Precio, ValorTotal):
        cur = self.cnn.cursor()
        sql='''INSERT INTO compras (Fecha, Producto, Cantidad, Precio, ValorTotal) 
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(Fecha, Producto, Cantidad, Precio, ValorTotal)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_compras(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM compras WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_compras(self,Id, Fecha, Producto, Cantidad, Precio, ValorTotal):
        cur = self.cnn.cursor()
        sql='''UPDATE compras SET Fecha='{}', Producto='{}', Cantidad='{}',
        Precio='{}', ValorTotal='{}', where Id = {}'''.format(Fecha, Producto, Cantidad, Precio, ValorTotal,Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
