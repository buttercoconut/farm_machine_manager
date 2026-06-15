from fastapi import FastAPI
from .api import machines, rentals, maintenance, users

app = FastAPI(title="Farm Machine Manager API")

app.include_router(machines.router)
app.include_router(rentals.router)
app.include_router(maintenance.router)
app.include_router(users.router)
