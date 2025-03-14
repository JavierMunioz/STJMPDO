from fastapi import FastAPI
from views.user import user_router

app = FastAPI()
app.include_router(user_router)

@app.get("/")
async def home():
    return {"":""}