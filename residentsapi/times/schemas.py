
from typing import Annotated

from pydantic import Field
from residentsapi.contrib.schemas import BaseSchema

class Time(BaseSchema):
    nome: Annotated[str, Field(description='Nome do time', examples='Dados e Desenvolvimento',max_length=50)]
    
