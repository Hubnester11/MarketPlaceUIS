#pip install fastApi 
#pip install "uvicorn[standard]"  #Instalacion de fastapi y uvicorn
from fastapi import FastAPI
from typing import Union
from src.conexion_postgresql import *

app = FastAPI()
@app.get('/')
def read_root():
    return {'Bienvenido a MarketPlace UIS'}

@app.post('/usuario/crear') #Creacion de usuario, se asume que el usuario nunca sera un moderador, asi que por default su rol sera 2
def Crear_user(id:int, nombre:str, apellido:str, email:str,  telefono:int):
    respuesta = Crear_Usuario(id, nombre, apellido, email,  telefono, 2)
    return respuesta

@app.get('/usuario')  #Busqueda de los Usuarios
def Consultar_user():
    return Consultar_usuario()

@app.put('/usuario/update') #actualizacion de dato usuario
def actualizar_user(id:int, telefono:int):
    resultado = Update_Usuario(id,telefono)
    return resultado

@app.delete('/usuario/delete') #eliminacion del usuario, se pide solo el id.
def delete_user(id:int):
    resultado = Delete_Usuario(id)
    return resultado

@app.get('/producto') #Busqueda de los productos a traves de su categoria
def Consultar_produc(categoria: int):
    Consultar_produc = Consultar_producto(categoria)
    return Consultar_produc

@app.post('/producto/creacion') #Creacion de Productos
def Crear_product(id:int, nombre:str, precio:int, descripcion:str,  categoria_producto_id:int, inventario_id:int, usuario_id:int,cantidad:int):
    resultado = Crear_producto(id, nombre, precio, descripcion,  categoria_producto_id, inventario_id, usuario_id,cantidad)
    return resultado

@app.put('/producto/update') #actualizacion de dato producto
def actualizar_producto_inventario(id:int, inventario:int):
    resultado = Update_Producto_inventario(id,inventario)
    return resultado

@app.delete('/producto/delete') #eliminacion del producto, se pide solo el id.
def delete_producto(id:int):
    resultado = Delete_Producto(id)
    return resultado

@app.post('/servicio/creacion') #Creacion de servicio
def Crear_servicio(id:int, usuario_id:int, servicioid:int, precio_hora:int, descripcion:str, nombre:str, categoria_servicio:int ):
    resultado = Crear_Servicio(id, usuario_id, servicioid, precio_hora, descripcion, nombre, categoria_servicio)
    return resultado

@app.get('/servicio') #Busqueda de los servicio a traves de su categoria
def Consultar_servicio(categoria: int):
    Consultar_produc = Consultar_Servicio(categoria)
    return Consultar_produc

@app.put('/servicio/update') #actualizacion de dato servicio
def actualizar_servicio(id:int, precio_hora:int):
    resultado = Update_Servicio(id,precio_hora)
    return resultado

@app.delete('/servicio/delete') #eliminacion de un servicio y su proovedor, se pide el id del proovedor y del servicio.
def delete_servicio(id:int, idservicio:int):
    resultado = Delete_Servicio(id, idservicio)
    return resultado

@app.post('/inmueble/creacion') #Creacion de inmueble
def Crear_inmueble(id:int, nombre:str, descripcion:str, precio:int,  estado_inmueble_id:int, ubicacion_id:int, tipo_id_inmueble:int, id_usuario:int ):
    resultado = Crear_Inmueble(id, nombre, descripcion, precio,  estado_inmueble_id, ubicacion_id, tipo_id_inmueble, id_usuario)
    return resultado

@app.get('/inmueble/busqueda') #Busqueda de los inmuebles a traves de su id
def Consultar_inmueble(id:int):
    Consultar_inmueb = Consultar_Inmueble(id)
    return Consultar_inmueb

@app.put('/inmueble/update') #actualizacion de dato inmueble, 1 para descripcion, 2 para precio, 3 para estado
def actualizar_inmueble(id:int, tipo:int, dato: int):
    resultado = Update_Inmueble(id,tipo,dato)
    return resultado

@app.delete('/inmueble/delete') #eliminacion del inmueble, se pide solo el id.
def delete_inmueble(id:int):
    resultado = Delete_Inmueble(id)
    return resultado

@app.post('/compra_producto/creacion') #Creacion de compra del producto
def Crear_compra_producto(id: int, usuario_id:int, producto_id:int, estado_id:int):
    resultado = Crear_Compra_Producto(id, usuario_id, producto_id, estado_id)
    return resultado

@app.get('/compra_producto/busqueda') #Busqueda de las compra de un producto a traves de su id
def Consultar_compra_producto(id:int):
    Consultar_compra = Consultar_Compra_Producto(id)
    return Consultar_compra

@app.put('/compra_producto/update') #actualizacion de dato servicio
def actualizar_compra_producto(id:int, estado_id:int):
    resultado = Update_Compra_Producto(id,estado_id)
    return resultado

@app.delete('/compra_producto/delete') #eliminacion de la compra, se pide solo el id.
def delete_compra_producto(id:int):
    resultado = Delete_Compra_Producto(id)
    return resultado

@app.post('/compra_servicio/creacion') #Creacion de compra del servicio
def Crear_compra_servicio(id: int, proveedor_servicio_id:int, usuario_id:int,  estado_id:int):
    resultado = Crear_Compra_Servicio(id, proveedor_servicio_id, usuario_id, estado_id)
    return resultado

@app.get('/compra_servicio/busqueda') #Busqueda de las compra de un servicio a traves de su id
def Consultar_compra_servicio(id:int):
    Consultar_compra = Consultar_Compra_Servicio(id)
    return Consultar_compra

@app.put('/compra_servicio/update') #actualizacion de dato servicio
def actualizar_compra_producto(id:int, estado_id:int):
    resultado = Update_Compra_Servicio(id,estado_id)
    return resultado

@app.delete('/compra_servicio/delete') #eliminacion de la compra, se pide solo el id.
def delete_compra_servicio(id:int):
    resultado = Delete_Compra_Servicio(id)
    return resultado

@app.post('/renta/creacion') #Creacion de la renta de un inmueble
def Crear_renta(id: int, inmueble_id:int, usuario_id:int,  estado_id:int):
    resultado = Crear_Renta(id, inmueble_id, usuario_id, estado_id)
    return resultado

@app.get('/renta/busqueda') #Busqueda de la renta a traves de su id
def Consultar_renta(id:int):
    Consultar_rentas = Consultar_Renta(id)
    return Consultar_rentas

@app.put('/renta/update') #actualizacion de estado de la renta
def actualizar_renta(id:int, estado_id:int):
    resultado = Update_Renta(id,estado_id)
    return resultado

@app.delete('/renta/delete') #eliminacion de la renta, se pide solo el id.
def delete_renta(id:int):
    resultado = Delete_Renta(id)
    return resultado

