from models.criar import CriaMODEL
from fastapi import HTTPException
from uuid import uuid4


def criar_service(model= CriaMODEL):
    novo_pais = CriaMODEL(
        id=str(uuid4()),
        nome=model.nome,
        habitantes=model.habitantes,
        continente=model.continente
    )

    if novo_pais:
        return novo_pais
    
    raise HTTPException(500)
