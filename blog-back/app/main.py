from fastapi import FastAPI
from app import blog_api

app = FastAPI()
app.include_router(blog_api.router)


@app.get('/')
async def root():
    return {"": ""}
