from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, Depends
from models.criar import CriaMODEL
from core.deps import get_session
from sqlmodel import select
from fastapi import status
from uuid import UUID


async def listagem_id_service(id: UUID, db:AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(CriaMODEL).filter(CriaMODEL.id == id)
        result = await session.execute(query)
        pais: CriaMODEL = result.scalar_one_or_none()
        print(pais)

        if pais:
            return pais
        
        if pais is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='ID não encontrado!'
            )
        
        else:
            raise HTTPException(500)
