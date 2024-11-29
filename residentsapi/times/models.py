
from residentsapi.contrib.models import BaseModel
from datetime import datetime

#from residentsapi.residente.models import ResidenteModel
import residentsapi.residente.models

from sqlalchemy import Integer, String, DateTime, ForeignKey
from uuid import uuid4
from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

class TimeModel(BaseModel):
    __tablename__ = 'times'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)

    residentes: Mapped[list['residentsapi.residente.models.ResidenteModel']] = relationship('ResidenteModel', back_populates='time')

    
    