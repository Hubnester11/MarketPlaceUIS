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

@app.delete('/producto/delete') #eliminacion del usuario, se pide solo el id.
def delete_producto(id:int):
    resultado = Delete_Producto(id)
    return resultado

@app.post('/servicio/creacion') #Creacion de Productos
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
