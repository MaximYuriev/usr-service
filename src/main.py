from fastapi import FastAPI

from src.user.router import user_router

app = FastAPI(title="User Service")

app.include_router(user_router)
