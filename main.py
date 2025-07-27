import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    name = os.getenv("NAME", "NO NAME")
    return {"message": f"Hello, {name}!"}
