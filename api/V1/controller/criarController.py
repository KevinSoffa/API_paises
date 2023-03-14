from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, status, Depends
from models.criar import CriaMODEL
from core.deps import get_session
from service import criar_service

# Bypass warning SQLModel select
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True
# Fim Bypass

router = APIRouter()

@router.post('', status_code=status.HTTP_201_CREATED, response_model=CriaMODEL)
async def criar_controller(model: CriaMODEL, db: AsyncSession = Depends(get_session)):
    db.add(criar_service(model))

    await db.commit()

    return criar_service(model)
