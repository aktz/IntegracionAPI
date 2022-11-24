from pydantic import BaseModel
import Conexion


class Proveedores(BaseModel):
    Id: int
    Nit: float
    RazonSocial: str
    Telefono: str
    Contacto: str
    Email: str

    def __str__(self):
        datos=self.consulta_proveedores()        
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
        
    def consulta_proveedores(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM proveedores")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_proveedores(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM proveedores WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta_proveedores(self,Nit, RazonSocial, Telefono, Contacto, Email):
        cur = self.cnn.cursor()
        sql='''INSERT INTO proveedores (Nit, RazonSocial, Telefono, Contacto, Email) 
        VALUES('{}', '{}', '{}', '{}', '{}')'''.format(Nit, RazonSocial, Telefono, Contacto, Email)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_proveedores(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM proveedores WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_proveedores(self,Id, Nit, RazonSocial, Telefono, Contacto, Email):
        cur = self.cnn.cursor()
        sql='''UPDATE proveedores SET Nit='{}', RazonSocial='{}', Telefono='{}',
        Contacto='{}', Email='{}', where Id = {}'''.format(Nit, RazonSocial, Telefono, Contacto, Email,Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
