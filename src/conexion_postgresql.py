import psycopg2
from psycopg2 import extras
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
       
        cur=conecction.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM usuario")
        for row in cur.fetchall():
            print(row["nombre"],row["apellido"])
        cur.close()

       
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
        for row in cur.fetchall():
            print(row["nombre"],row["apellido"])
        cur.close()

       
    except Exception as error: 
        print(error)
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
        
        for row in cur.fetchall():
            print(row["nombre"],row["apellido"])
        cur.close()

       
    except Exception as error: 
        print(error)
    finally:
        
        conecction.close()
        print("conexion finalizada")
        
#Crear_producto(1,"Galletas",200,"deliciosas galletas",3,1,3,100) # prueba de ingreso de datos

#  cursor.execute("SELECT * from usuario") row=cursor.fetchone() print(row)