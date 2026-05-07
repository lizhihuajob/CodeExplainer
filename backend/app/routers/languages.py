from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models import Language
from app.schemas import LanguageCreate, LanguageResponse

router = APIRouter(prefix="/api/languages", tags=["languages"])


@router.get("", response_model=list[LanguageResponse])
async def list_languages(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Language).options(selectinload(Language.elements)))
    languages = result.scalars().all()
    return languages


@router.get("/{language_key}", response_model=LanguageResponse)
async def get_language(language_key: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Language).where(Language.key == language_key).options(selectinload(Language.elements))
    )
    language = result.scalar_one_or_none()
    if not language:
        raise HTTPException(status_code=404, detail="Language not found")
    return language


@router.post("", response_model=LanguageResponse, status_code=201)
async def create_language(data: LanguageCreate, db: AsyncSession = Depends(get_db)):
    existing = await db.execute(select(Language).where(Language.key == data.key))
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Language already exists")
    language = Language(key=data.key, name=data.name, description=data.description)
    db.add(language)
    await db.commit()
    await db.refresh(language)
    return language


@router.delete("/{language_key}", status_code=204)
async def delete_language(language_key: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Language).where(Language.key == language_key))
    language = result.scalar_one_or_none()
    if not language:
        raise HTTPException(status_code=404, detail="Language not found")
    await db.delete(language)
    await db.commit()
