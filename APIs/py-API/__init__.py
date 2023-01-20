import uvicorn
from fastapi import FastAPI

api = FastAPI()

from py-API import security
import views
