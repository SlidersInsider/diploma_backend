from fastapi import FastAPI
from db.db import init_db

app = FastAPI()

init_db()

@app.get("/")
def read_root():
    return {"message": "FastAPI работает!"}
