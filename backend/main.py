# Main FastAPI application
from fastapi import FastAPI
from .api import machines, maintenance, rentals, users

app = FastAPI(title="Farm Machine Manager API")

app.include_router(machines.router, prefix="/machines", tags=["machines"])
app.include_router(maintenance.router, prefix="/maintenance", tags=["maintenance"])
app.include_router(rentals.router, prefix="/rentals", tags=["rentals"])
app.include_router(users.router, prefix="/users", tags=["users"])

# Simple health check
@app.get("/health")
async def health_check():
    return {"status": "ok"}
