from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, status, Depends
from service import atualizar_service
from models.criar import CriaMODEL
from core.deps import get_session
from uuid import UUID

# Bypass warning SQLModel select
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True
# Fim Bypass


router = APIRouter()

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=CriaMODEL)
async def put_pais(id: UUID, model: CriaMODEL, db: AsyncSession=Depends(get_session)):
    return await atualizar_service(id, model, db)
