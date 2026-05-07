from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import GlossaryTerm
from app.schemas import GlossaryTermCreate, GlossaryTermResponse

router = APIRouter(prefix="/api/glossary", tags=["glossary"])


@router.get("", response_model=dict[str, GlossaryTermResponse])
async def list_glossary(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(GlossaryTerm))
    terms = result.scalars().all()
    return {term.term: term for term in terms}


@router.get("/{term_name}", response_model=GlossaryTermResponse)
async def get_glossary_term(term_name: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(GlossaryTerm).where(GlossaryTerm.term == term_name))
    term = result.scalar_one_or_none()
    if not term:
        raise HTTPException(status_code=404, detail="Glossary term not found")
    return term


@router.post("", response_model=GlossaryTermResponse, status_code=201)
async def create_glossary_term(data: GlossaryTermCreate, db: AsyncSession = Depends(get_db)):
    existing = await db.execute(select(GlossaryTerm).where(GlossaryTerm.term == data.term))
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Glossary term already exists")
    term = GlossaryTerm(
        term=data.term,
        definition=data.definition,
        characteristics=data.characteristics,
        example=data.example,
        related_concepts=data.related_concepts,
    )
    db.add(term)
    await db.commit()
    await db.refresh(term)
    return term


@router.delete("/{term_name}", status_code=204)
async def delete_glossary_term(term_name: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(GlossaryTerm).where(GlossaryTerm.term == term_name))
    term = result.scalar_one_or_none()
    if not term:
        raise HTTPException(status_code=404, detail="Glossary term not found")
    await db.delete(term)
    await db.commit()
