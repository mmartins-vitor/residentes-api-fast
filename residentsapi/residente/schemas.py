"""
responsaveis por validações e serializações de dados
"""
from typing import Annotated
from pydantic import  Field, PositiveInt

from residentsapi.contrib.schemas import BaseSchema

class Residente(BaseSchema):
    nome: Annotated[str, Field(description='Nome do residente', example='Vitor',max_length=50)]
    # validar cpf depois
    cpf: Annotated[str, Field(description='cpf do residente', example='02609455547',max_length=50)]
    formacao: Annotated[str, Field(description='formação do residente', example='Oceanografo',max_length=50)]    
    idade: Annotated[PositiveInt, Field(description='idade do residente', example='27')]
    genero: Annotated[str,Field(description='sexo do residente', example='M or F',max_length=1)]
