from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import machines, maintenance, rentals, users

app = FastAPI(title="Farm Machine Manager API")

# CORS 설정 (프론트엔드와 통신을 위해 필요)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue dev server 포트
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 포함
app.include_router(machines.router, prefix="/machines", tags=["machines"])
app.include_router(maintenance.router, prefix="/maintenance", tags=["maintenance"])
app.include_router(rentals.router, prefix="/rentals", tags=["rentals"])
app.include_router(users.router, prefix="/users", tags=["users"])

# DB 초기화 (간단한 예시용 SQLite)
from .database import Base, engine

Base.metadata.create_all(bind=engine)
