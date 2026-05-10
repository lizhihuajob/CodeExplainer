from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.config import settings
from app.database import engine, Base
from app.data_service import get_combined_data
from app.init_data import load_data_from_dict
from app.routers import languages, elements, glossary


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    data = await get_combined_data()
    await load_data_from_dict(data)

    yield


app = FastAPI(
    title="CodeExplain API",
    description="代码解释器后端服务",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(languages.router)
app.include_router(elements.router)
app.include_router(glossary.router)

frontend_dir = None
if settings.FRONTEND_DIR:
    frontend_dir = Path(settings.FRONTEND_DIR)
else:
    frontend_dir = Path(__file__).parent.parent / "frontend"

if frontend_dir.exists():
    app.mount("/", StaticFiles(directory=str(frontend_dir), html=True), name="frontend")
