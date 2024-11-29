
from typing import Annotated

from pydantic import Field
from residentsapi.contrib.schemas import BaseSchema

class Setor(BaseSchema):
    nome: Annotated[str, Field(description='Nome do setor', example='GEPDI',max_length=8)]
    diretoria: Annotated[str, Field(description='Nome da diretoria', example='DOP',max_length=8)]
    gerente: Annotated[str, Field(description='Nome do gerente', example='Gabriel Cassia',max_length=50)]
    
