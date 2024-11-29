from residentsapi.contrib.models import *
from datetime import datetime

from residentsapi.residente.models import ResidenteModel

class SetorModel(BaseModel):
    __tablename___ = 'setores'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String[8], nullable=False)
    diretoria: Mapped[str] = mapped_column(String[8],nullable=False)
    gerente: Mapped[str] = mapped_column(String[50], nullable=False)

    # relacionamento de time com residente
    residente: Mapped[ResidenteModel] = relationship(back_populates='setor')
    
    
    