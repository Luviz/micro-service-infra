from dataclasses import dataclass
from fastapi import APIRouter, HTTPException, Response, responses, status
import boto3
from boto3 import exceptions
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
        dynamodb = boto3.resource(
            'dynamodb', **awsConfigs)
        tables_name = [table.name for table in dynamodb.tables.all()]
        if (environ['TABLE_NAME'] in tables_name):
            return responses.JSONResponse(status_code=312, content={"info": "table is already initialized"})

        table = dynamodb.create_table(
            TableName=environ['TABLE_NAME'],
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        table.wait_until_exists()

        return {
            "tablesName": table.name
        }

    except ValueError as e:
        raise HTTPException(
            status_code=503, detail={"type": "ValueError", "message": e.args})
    except exceptions.EndpointConnectionError as e:
        raise HTTPException(
            status_code=503, detail={"type": "EndpointConnectionError", "message": dict(e)})
    except Exception as e:
        return {
            'Error': type(e)
        }
