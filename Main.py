#pip install fastApi 
#pip install "uvicorn[standard]"  #Instalacion de fastapi y uvicorn
from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from src.conexion_postgresql import *

class Usuario(BaseModel):
    id:int 
    nombre:str 
    apellido:str 
    email:str  
    telefono:int 
    rol_id:int 

app = FastAPI()
@app.get('/')
def read_root():
    return {'Hello'' World!!!'}

@app.get('/usuario')  #Busqueda de los Usuarios
def Consultar_user():
    return Consultar_usuario()


@app.get('/producto') #Busqueda de los productos a traves de su categoria
def Consultar_produc(categoria: int):
    Consultar_produc = Consultar_producto(categoria)
    return Consultar_produc



@app.post('/producto/creacion') #Creacion de Productos
def Crear_product(id:int, nombre:str, precio:int, descripcion:str,  categoria_producto_id:int, inventario_id:int, usuario_id:int,cantidad:int):
    resultado = Crear_producto(id, nombre, precio, descripcion,  categoria_producto_id, inventario_id, usuario_id,cantidad)
    return resultado
