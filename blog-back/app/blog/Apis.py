from app.modals.Blog import Blog
from os import environ
import boto3

awsConfigs = {
    'region_name': '',
    'endpoint_url': environ['DB_URL'],
    'aws_access_key_id': 'local',
    'aws_secret_access_key': 'local',
}


class TableExistitExpection(Exception):
    pass


def get_table():
    dynamodb = boto3.resource('dynamodb', **awsConfigs)
    return dynamodb.Table(environ['TABLE_NAME'])


def list():
    table = get_table()
    return table.scan()


def get(id: str):
    table = get_table()
    return table.get_item(Key={"id": id})


def update(id: str, data):
    pass


def new(data: Blog):
    table = get_table()
    # print(data, data.asDict(), data.to_json())
    table.put_item(
        Item=data.asDict()
    )


def delete(id: str):
    pass


def init_blog_table():
    dynamodb = boto3.resource(
        'dynamodb', **awsConfigs)

    tables_name = [table.name for table in dynamodb.tables.all()]

    if (environ['TABLE_NAME'] in tables_name):
        raise TableExistitExpection from None

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
    return table
