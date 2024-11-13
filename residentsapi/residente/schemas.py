"""
responsaveis por validações e serializações de dados
"""
from typing import Annotated
from pydantic import  Field, PositiveInt

from residentsapi.contrib.schemas import BaseSchema

class Residente(BaseSchema):
    nome: Annotated[str, Field(description='Nome do residente', examples='Vitor',max_length=50)]
    # validar cpf depois
    cpf: Annotated[str, Field(description='cpf do residente', examples='02609455547',max_length=50)]
    formacao: Annotated[str, Field(description='formação do residente', examples='Oceanografo',max_length=50)]    
    idade: Annotated[PositiveInt, Field(description='idade do residente', examples='27')]
    genero: Annotated[str,Field(description='sexo do residente', examples='M or F',max_length=1)]
