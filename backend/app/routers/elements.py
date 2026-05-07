from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, or_, cast, Text
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import Element, Language
from app.schemas import ElementCreate, ElementResponse, SearchResult

router = APIRouter(prefix="/api/elements", tags=["elements"])


@router.get("", response_model=list[ElementResponse])
async def list_elements(
    language_key: str | None = Query(None, alias="language"),
    db: AsyncSession = Depends(get_db),
):
    stmt = select(Element)
    if language_key:
        stmt = stmt.where(Element.language_key == language_key)
    result = await db.execute(stmt)
    return result.scalars().all()


@router.get("/{element_id}", response_model=ElementResponse)
async def get_element(element_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Element).where(Element.element_id == element_id))
    element = result.scalar_one_or_none()
    if not element:
        raise HTTPException(status_code=404, detail="Element not found")
    return element


@router.post("", response_model=ElementResponse, status_code=201)
async def create_element(data: ElementCreate, db: AsyncSession = Depends(get_db)):
    lang_result = await db.execute(select(Language).where(Language.key == data.language_key))
    if not lang_result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Language not found")
    existing = await db.execute(select(Element).where(Element.element_id == data.element_id))
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Element already exists")
    element = Element(
        element_id=data.element_id,
        name=data.name,
        description=data.description,
        search_keywords=data.search_keywords,
        technical_explanation=data.technical_explanation,
        metaphor_explanation=data.metaphor_explanation,
        examples=[e.model_dump() for e in data.examples],
        syntax_notes=data.syntax_notes,
        related_terms=data.related_terms,
        language_key=data.language_key,
    )
    db.add(element)
    await db.commit()
    await db.refresh(element)
    return element


@router.delete("/{element_id}", status_code=204)
async def delete_element(element_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Element).where(Element.element_id == element_id))
    element = result.scalar_one_or_none()
    if not element:
        raise HTTPException(status_code=404, detail="Element not found")
    await db.delete(element)
    await db.commit()


@router.get("/search/", response_model=list[SearchResult])
async def search_elements(
    q: str = Query(..., min_length=1),
    language: str | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    stmt = select(Element, Language.name.label("language_name")).join(
        Language, Element.language_key == Language.key
    )
    if language:
        stmt = stmt.where(Element.language_key == language)

    pattern = f"%{q}%"
    stmt = stmt.where(
        or_(
            Element.name.ilike(pattern),
            Element.description.ilike(pattern),
            cast(Element.search_keywords, Text).ilike(pattern),
        )
    )
    result = await db.execute(stmt)
    rows = result.all()

    results = []
    for row in rows:
        element, lang_name = row
        results.append(
            SearchResult(
                element_id=element.element_id,
                name=element.name,
                description=element.description,
                language_name=lang_name,
                language_key=element.language_key,
            )
        )
    return results
