from residentsapi.contrib.models import *
from datetime import datetime

from residentsapi.times.models import TimeModel

class ResidenteModel(BaseModel):
    __tablename___ = 'residentes'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String[50], nullable=False)
    cpf: Mapped[str] = mapped_column(String[50], nullable=False)
    formacao: Mapped[str] = mapped_column(String[50], nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    genero: Mapped[str] = mapped_column(String[1], nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    
    
    
    
    
    