from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, status, Depends
from service import listagem_id_service
from models.criar import CriaMODEL
from uuid import UUID
from core.deps import get_session
from typing import List

# Bypass warning SQLModel select
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True
# Fim Bypass


router = APIRouter()

@router.get('/{id}',response_model=CriaMODEL, status_code=status.HTTP_200_OK)
async def get_id_pais(id: UUID, db:AsyncSession=Depends(get_session)):
    return await listagem_id_service(id, db)
