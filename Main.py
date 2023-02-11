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

@app.get('/producto')
def Consultar():
    
    return Consultar_usuario()
#@app.post('/')
#async def Crear_Usuario(user: Usuario):
#    return user