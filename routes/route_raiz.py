from fastapi import APIRouter, status


router = APIRouter()


@router.get('/', description="Rota raiz da API", summary="Rota raiz")
async def root():
  
    return {
        "msg": "Olá eu sou uma mensagem de retorno do endpoint raiz"
    }