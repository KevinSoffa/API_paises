from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, status, Depends
from service import apagar_service
from models.criar import CriaMODEL
from core.deps import get_session
from uuid import UUID

# Bypass warning SQLModel select
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True
# Fim Bypass


router = APIRouter()

@router.delete('/{id}', status_code=status.HTTP_200_OK)
async def apagar_controller(id: UUID, db: AsyncSession = Depends(get_session)):
    return await apagar_service(id, db)
