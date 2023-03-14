from sqlalchemy.ext.asyncio import AsyncSession
from .database import Session
from typing import Generator


async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session

    except:
        await session.close()
