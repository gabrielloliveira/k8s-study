import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    name = os.getenv("NAME", "NO NAME")
    secret = os.getenv("SECRET_KEY", "NO SECRET")
    return {"message": f"Hello, {name}! Your secret is {secret}."}
