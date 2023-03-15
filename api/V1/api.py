from api.V1.controller import (
    criarController, 
    listagemCrontoller, 
    listagemIdController,
    atualizarController
)

from fastapi import APIRouter


api_router = APIRouter()

# POST
api_router.include_router(criarController.router, prefix='/paises', tags=["paises"])

# GET
api_router.include_router(listagemCrontoller.router, prefix='/paises', tags=["paises"])

# GET ID
api_router.include_router(listagemIdController.router,  prefix='/pais', tags=["paises"])

# PUT
api_router.include_router(atualizarController.router, prefix='/pais-update', tags=["paises"])
