from pydantic import BaseModel
import Conexion


class Facturas(BaseModel):
    Id: int
    Fecha: int
    Consecutivo: str
    Cliente: str
    Documento: str
    ValorTotal: int

    def __str__(self):
        datos=self.consulta_facturas()        
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
        
    def consulta_facturas(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM facturas")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_facturas(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM facturas WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta_facturas(self,Fecha, Consecutivo, Cliente, Documento, ValorTotal):
        cur = self.cnn.cursor()
        sql='''INSERT INTO facturas (Fecha, Consecutivo, Cliente, Documento, ValorTotal) 
        VALUES('{}', '{}', '{}', '{}', '{}')'''.format(Fecha, Consecutivo, Cliente, Documento, ValorTotal)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_facturas(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM facturas WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_facturas(self,Id, Fecha, Consecutivo, Cliente, Documento, ValorTotal):
        cur = self.cnn.cursor()
        sql='''UPDATE facturas SET Fecha='{}', Consecutivo='{}', Cliente='{}',
        Documento='{}', ValorTotal='{}', where Id = {}'''.format(Fecha, Consecutivo, Cliente, Documento, ValorTotal,Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
