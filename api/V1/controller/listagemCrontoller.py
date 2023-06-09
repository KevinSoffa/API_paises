from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, status, Depends
from service import listagem_service
from models.criar import CriaMODEL
from core.deps import get_session
from typing import List

# Bypass warning SQLModel select
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True
# Fim Bypass


router = APIRouter()

@router.get('', response_model=List[CriaMODEL], status_code=status.HTTP_200_OK)
async def get_paises(db: AsyncSession = Depends(get_session)):
    return await listagem_service(db)
