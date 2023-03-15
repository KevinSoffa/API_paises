from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, Depends
from models.criar import CriaMODEL
from core.deps import get_session
from sqlmodel import select
from typing import List


async def listagem_service(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CriaMODEL)
        result = await session.execute(query)
        paises: List[CriaMODEL] = result.scalars().all()
        print(paises)

        if paises:
            return paises
        
        raise HTTPException(500)
