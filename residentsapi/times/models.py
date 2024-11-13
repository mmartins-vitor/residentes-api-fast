from residentsapi.contrib.models import *
from datetime import datetime

class TimeModel(BaseModel):
    __tablename___ = 'times'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String[50], nullable=False)

    
    
    
    
    