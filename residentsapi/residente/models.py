from residentsapi.contrib.models import *
from datetime import datetime

from residentsapi.setor.models import SetorModel
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

    # evita importacao circular?
    # relacionamento de residente com time
    time: Mapped[TimeModel] = relationship(back_populates='residente')
    time_id : Mapped[int] = mapped_column(ForeignKey('times.pk_id'))

    # relacionamento de residente com setor
    setor: Mapped[SetorModel] = relationship(back_populates='residente')
    setor_id : Mapped[int] = mapped_column(ForeignKey('setores.pk_id'))
    
    
    
    
    