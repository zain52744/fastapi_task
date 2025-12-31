from fastapi import FastAPI
from app.routers import users, age,jokes


app = FastAPI()
app.include_router(users.router)
app.include_router(age.router)
app.include_router(jokes.router)

@app.get("/")
async def root():
    return {"message": "Welcome, this is FastApi"}
