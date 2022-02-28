from dataclasses import dataclass
from datetime import datetime
from fastapi import APIRouter

router = APIRouter(
    prefix='/blog',
    tags=['blog'],
    responses={404: {"description": "Not found"}}
)


@dataclass
class Item():
    meh: str
    test: int


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/meh")
async def meh(meh='', peh=''):
    return {"meh": meh, "peh": peh}


@router.get("/meh/{id}")
async def meh(id: int, meh='', peh=''):
    return {"id": id, "meh": meh, "peh": peh}


@router.post("/meh")
async def meh(item: Item):
    """
    some test of post
    """
    return {
        "meh": 12,
        "items": item
    }
