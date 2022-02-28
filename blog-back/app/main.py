from fastapi import FastAPI
from . import blog

app = FastAPI()

app.include_router(blog.router)


@app.get('/')
async def root():
    return {"": ""}
