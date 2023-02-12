import psycopg2
from psycopg2 import extras

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
        return ("error al registrar el usuario, error :   " + error)
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
        print("error al consutar los usuarios" + error)
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
        return ("error al actualizar el usuario, error :   " + error)
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
        return ("error al eliminar el usuario, error :   " + error)
    finally:
        conecction.close()

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
        return ("error al crear el producto, error :   " + error)
    finally:
        
        conecction.close()
        print("conexion finalizada")

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
        return ("error al consultar los productos, error :   " + error)
    finally:
        
        conecction.close()
        print("conexion finalizada")

def Update_Producto_inventario(id, inventario): #Pide el id del producto y la cantidad para añadir al inventario.
    try: 
        conecction=psycopg2.connect(
            host="localhost",
            user="postgres",
            password="12345",
            database="MarketPlaceUIS"
            )
        ids = str(id)
        inventarios = str(inventario)
        id_inventario = 0
        cursor=conecction.cursor()
        cur=conecction.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM producto where id=%s", (ids))
        for row in cur.fetchall():
            id_inventario = str(row["inventario_id"])
        insertquery = "update inventario set cantidad = %s where id = %s"
        cur.execute(insertquery,(inventarios, id_inventario ))
        conecction.commit()
        cur.close()
        return ("Datos Actualizados correctamente")

       
    except Exception as error: 
        return ("error al actualizar el usuario, error :   " + error)
    finally:
        
        conecction.close()
        print("conexion finalizada")

def Delete_Producto(id): #Pide el dato para eliminar un producto mediante el id, tambien elimina su inventario 
    try: 
        conecction=psycopg2.connect(
            host="localhost",
            user="postgres",
            password="12345",
            database="MarketPlaceUIS"
            )
        ids= str(id)
        id_inventario = 0
        cursor=conecction.cursor()
        cur=conecction.cursor(cursor_factory=psycopg2.extras.DictCursor)
        insertquery = "Delete from producto WHERE id = %s"
        insertquery1 = "Delete from inventario Where id= %s"
        cur.execute("SELECT * FROM producto where id=%s", (ids))
        for row in cur.fetchall():
           id_inventario = str((row["inventario_id"]))
        cursor.execute(insertquery,ids)
        conecction.commit()
        cursor.execute(insertquery1,id_inventario)
        conecction.commit()
        cur.close()
        return("producto eliminado con exito")

       
    except Exception as error: 
        return ("error al eliminar el producto, error :   " + error)
    finally:
        conecction.close()

def Crear_Servicio(id, usuario_id, servicioid, precio_hora, descripcion, nombre, categoria_servicio ): #pide los datos para crear un nuevo servicio y asu vez para crear el proovedor de este
    try: 
        conecction=psycopg2.connect(
            host="localhost",
            user="postgres",
            password="12345",
            database="MarketPlaceUIS"
            )
        cursor=conecction.cursor()
        cur=conecction.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("insert into servicio (id, nombre, categoria_servicio_id) values (%s,%s,%s)",(servicioid, nombre, categoria_servicio)) #insert del servicio
        conecction.commit()
        insertquery = "insert into proveedor_servicio (id, usuario_id, servicio_id, precio_hora, descripcion) values (%s,%s,%s,%s,%s)"
        cursor.execute(insertquery,(id, usuario_id, servicioid, precio_hora, descripcion))
        conecction.commit()
        cur.close()
        return("registro realizado de forma satisfactoria")

       
    except Exception as error: 
        return ("error al crear el producto, error :   " + error)
    finally:
        
        conecction.close()
        print("conexion finalizada")

def Consultar_Servicio(id_servicio): #funcion para consultar los usuarios
    
    try: 
        conecction=psycopg2.connect(
            host="localhost",
            user="postgres",
            password="12345",
            database="MarketPlaceUIS"
            )
       
        cur=conecction.cursor(cursor_factory=psycopg2.extras.DictCursor)
        ids= str(id_servicio)
        cur.execute("select * from servicio where categoria_servicio_id = %s",(ids))
        datos = []
        for row in cur.fetchall():
            datos.append(row)
        cur.close()
        return datos 
    except Exception as error: 
        return ("error al consultar los productos, error :   " + error)
    finally:
        
        conecction.close()
        print("conexion finalizada")

def Update_Servicio(id,precio_hora): #Pide el precio a cambiar de servicio proveedor, plantilla de update
    try: 
        conecction=psycopg2.connect(
            host="localhost",
            user="postgres",
            password="12345",
            database="MarketPlaceUIS"
            )
        cursor=conecction.cursor()
        cur=conecction.cursor(cursor_factory=psycopg2.extras.DictCursor)
        insertquery = "update proveedor_servicio set precio_hora = %s where id = %s"
        cursor.execute(insertquery,(precio_hora,id))
        conecction.commit()
        cur.close()
        return ("Datos Actualizados correctamente")

       
    except Exception as error: 
        return ("error al actualizar el usuario, error :   " + error)
    finally:
        conecction.close()

def Delete_Servicio(id,id_servicio): #Pide el dato para eliminar un producto mediante el id, tambien elimina su inventario 
    try: 
        conecction=psycopg2.connect(
            host="localhost",
            user="postgres",
            password="12345",
            database="MarketPlaceUIS"
            )
        ids= str(id)
        ids1=str(id_servicio)
        
        cursor=conecction.cursor()
        cur=conecction.cursor(cursor_factory=psycopg2.extras.DictCursor)
        insertquery = "Delete from proveedor_servicio WHERE servicio_id = %s"
        insertquery1 = "Delete from servicio Where id= %s"
        cur.execute("SELECT * FROM proveedor_servicio where id=%s", (ids))
        cursor.execute(insertquery,ids1)
        conecction.commit()
        cursor.execute(insertquery1,ids1)
        conecction.commit()
        cur.close()
        return("servicio eliminado con exito")
    except Exception as error: 
        return ("error al eliminar el producto, error :   " + error)
    finally:
        conecction.close()

