from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, Depends
from models.criar import CriaMODEL
from core.deps import get_session
from sqlmodel import select
from fastapi import status, Response
from uuid import UUID


async def apagar_service(id: UUID, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CriaMODEL).filter(CriaMODEL.id == id)
        result = await session.execute(query)
        pais_del: CriaMODEL = result.scalar_one_or_none()

        if pais_del:
            await session.delete(pais_del)
            await session.commit()

            return Response(
                status_code=status.HTTP_200_OK
            )
        
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='ID não encontrado'
            )
