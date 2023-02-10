#pip install fastApi 
#pip install "uvicorn[standard]"  #Instalacion de fastapi y uvicorn
from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from conexion_postgresql import *


app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello': 'World!!!'}

    
