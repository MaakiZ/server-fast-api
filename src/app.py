from fastapi import FastAPI
from src.config import settings
from src import models
from src.helpers.database import engine
from src.routers.users import router as user_router

models.Base.metadata.create_all(bind=engine)

if (settings.debugging):
    app = FastAPI(debug=True, reload=True, port=5000)
else:
    app = FastAPI(port=5000)


app.include_router(user_router)
