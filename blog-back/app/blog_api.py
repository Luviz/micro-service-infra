from dataclasses import dataclass
from fastapi import APIRouter, HTTPException, Response, responses, status
from os import environ
import app.blog.Apis as blogApis
from app.modals.Blog import Blog, RequestBlog

router = APIRouter(
    prefix='/blog',
    tags=['blog'],
    responses={404: {"description": "Not found"}}
)

awsConfigs = {
    'region_name': '',
    'endpoint_url': environ['DB_URL'],
    'aws_access_key_id': 'local',
    'aws_secret_access_key': 'local',
}


@dataclass
class Item():
    meh: str
    test: int


@router.get("/", description="get list of all the blogs")
async def list():
    list = blogApis.list()
    return list


@router.get("/{id}")
async def get(id: str):
    res = blogApis.get(id)
    if "Item" in res:
        return res
    raise HTTPException(status.HTTP_404_NOT_FOUND,
                        detail='Could not find the item')


@router.post("/", status_code=status.HTTP_202_ACCEPTED)
async def add(blog: RequestBlog, res: Response):
    blogApis.new(Blog(**blog.asDict()))


@router.post("/initblog")
async def initBlog():
    try:
        table = blogApis.init_blog_table()
        return {
            "tablesName": table.name
        }

    except ValueError as e:
        raise HTTPException(
            status_code=503, detail={"type": "ValueError", "message": e.args})
    except blogApis.TableExistitExpection:
        return responses.JSONResponse(
            status_code=312,
            content={
                "info": "table is already initialized"
            }
        )
    except Exception as e:
        return {
            'Error': type(e)
        }
