from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, Depends
from models.criar import CriaMODEL
from core.deps import get_session
from sqlmodel import select
from fastapi import status
from uuid import UUID


async def atualizar_service(id: UUID, model: CriaMODEL, db: AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(CriaMODEL).filter(CriaMODEL.id == id)
        result = await session.execute(query)
        pais_up: CriaMODEL = result.scalar_one_or_none()

        if pais_up:
            pais_up.nome = model.nome
            pais_up.habitantes = model.habitantes
            pais_up.continente = model.continente

            await session.commit()

            return pais_up
        
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='ID não encontrado'
            )
