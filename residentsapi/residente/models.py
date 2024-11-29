from residentsapi.contrib.models import *
from residentsapi.contrib.models import BaseModel

from datetime import datetime

#from residentsapi.setor.models import SetorModel
#from residentsapi.times.models import TimeModel
import residentsapi.times.models
import residentsapi.setor.models


from sqlalchemy import Integer, String, DateTime, ForeignKey
from uuid import uuid4
from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

class ResidenteModel(BaseModel):
    __tablename__ = 'residentes'
    

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    formacao: Mapped[str] = mapped_column(String(50), nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    genero: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    # Relacionamento com Time
    time_id: Mapped[int] = mapped_column(ForeignKey('times.pk_id'))
    time: Mapped['residentsapi.times.models.TimeModel'] = relationship('TimeModel', back_populates='residente')

    # Relacionamento com Setor
    setor_id: Mapped[int] = mapped_column(ForeignKey('setores.pk_id'))
    setor: Mapped['residentsapi.setor.models.SetorModel'] = relationship('SetorModel', back_populates='residente')
