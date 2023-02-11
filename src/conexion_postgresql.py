import psycopg2
from psycopg2 import extras
import numpy as np


def Conexion_base(): #Funcion Para Realizar la conexion de la base de datos.
    try: 
        conecction=psycopg2.connect(
            host="localhost",
            user="postgres",
            password="12345",
            database="MarketPlaceUIS"
            )
        print("conexion exitosa") #verificar que la conexion se realizo
        cursor=conecction.cursor()
       
    except Exception as error: 
        print(error)
    finally:
        
        conecction.close()
        print("conexion finalizada")


def Consultar_usuario(): #funcion para consultar los usuarios
    
    try: 
        conecction=psycopg2.connect(
            host="localhost",
            user="postgres",
            password="12345",
            database="MarketPlaceUIS"
            )
        datos = []
        cur=conecction.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM usuario")
        for row in cur.fetchall():
           x = (row["nombre"],row["apellido"])
           datos.append(x)
           
        cur.close()
        return datos

       
    except Exception as error: 
        print(error)
    finally:
        
        conecction.close()
        print("conexion finalizada")

def Crear_Usuario(id, nombre, apellido, email,  telefono, rol_id ): #pide los datos para crear un nuevo usuario
    
    try: 
        conecction=psycopg2.connect(
            host="localhost",
            user="postgres",
            password="12345",
            database="MarketPlaceUIS"
            )
        cursor=conecction.cursor()
        cur=conecction.cursor(cursor_factory=psycopg2.extras.DictCursor)
        insertquery = "insert into usuario  (id, nombre, apellido, email, telefono, rol_id) values (%s,%s,%s,%s,%s,%s)"
        cursor.execute(insertquery,(id, nombre, apellido, email, telefono, rol_id))
        conecction.commit()
        cur.close()
        return ("usuario registrado de forma correcta")

       
    except Exception as error: 
        return ("error al registrar el usuario :   " + error)
    finally:
        
        conecction.close()
        print("conexion finalizada")


def Crear_producto(id, nombre, precio, descripcion,  categoria_producto_id, inventario_id, usuario_id,cantidad ): #pide los datos para crear un nuevo producto y asu vez para crear el inventario de este
    try: 
        conecction=psycopg2.connect(
            host="localhost",
            user="postgres",
            password="12345",
            database="MarketPlaceUIS"
            )
        cursor=conecction.cursor()
        cur=conecction.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("insert into inventario (id, cantidad) values (%s,%s)",(inventario_id, cantidad))
        conecction.commit()
        insertquery = "insert into producto  (id, nombre, precio, descripcion,  categoria_producto_id, inventario_id, usuario_id) values (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(insertquery,(id, nombre, precio, descripcion,  categoria_producto_id, inventario_id, usuario_id))
        conecction.commit()
        cur.close()
        return("registro realizado de forma satisfactoria")

       
    except Exception as error: 
        print(error)
    finally:
        
        conecction.close()
        print("conexion finalizada")

def Update_Usuario(id,telefono): #Pide el dato a cambiar de usuario, plantilla de update
    try: 
        conecction=psycopg2.connect(
            host="localhost",
            user="postgres",
            password="12345",
            database="MarketPlaceUIS"
            )
        cursor=conecction.cursor()
        cur=conecction.cursor(cursor_factory=psycopg2.extras.DictCursor)
        insertquery = "update usuario set telefono = %s where id = %s"
        cursor.execute(insertquery,(telefono,id))
        conecction.commit()
        cur.close()
        return ("Datos Actualizados correctamente")

       
    except Exception as error: 
        return ("error al actualizar el usuario :   " + error)
    finally:
        
        conecction.close()
        print("conexion finalizada")


def Delete_Usuario(id): #Pide el dato para eliminar un usuario mediante el id, plantilla de delete
    try: 
        conecction=psycopg2.connect(
            host="localhost",
            user="postgres",
            password="12345",
            database="MarketPlaceUIS"
            )
        ids= str(id)
        cursor=conecction.cursor()
        cur=conecction.cursor(cursor_factory=psycopg2.extras.DictCursor)
        insertquery = "Delete from usuario WHERE id = %s"
        cursor.execute(insertquery,ids)
        conecction.commit()
        cur.close()
        return("usuario eliminado con exito")

       
    except Exception as error: 
        return ("error al eliminar el usuario :   " + error)
    finally:
        conecction.close()
        

def Consultar_producto(id_categoria): #funcion para consultar los usuarios
    
    try: 
        conecction=psycopg2.connect(
            host="localhost",
            user="postgres",
            password="12345",
            database="MarketPlaceUIS"
            )
       
        cur=conecction.cursor(cursor_factory=psycopg2.extras.DictCursor)
        ids= str(id_categoria)
        cur.execute("select * from producto where categoria_producto_id = %s",(ids))
        datos = []
        for row in cur.fetchall():
            datos.append(row)
        cur.close()
        return datos  
        

       
    except Exception as error: 
        print(error)
    finally:
        
        conecction.close()
        print("conexion finalizada")
print(Consultar_producto(3))
#Crear_Usuario(4, 'Juan', 'Aguila', 'juanaguila',  123654, 2 )


#Crear_producto(3,"mora",200,"deliciosas moras",3,3,3,100) # prueba de ingreso de datos

#  cursor.execute("SELECT * from usuario") row=cursor.fetchone() print(row)