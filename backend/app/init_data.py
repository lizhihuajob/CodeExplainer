import json
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import async_session, engine, Base
from app.models import Language, Element, GlossaryTerm


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def load_data_from_json(json_path: str):
    path = Path(json_path)
    if not path.exists():
        print(f"Data file not found: {json_path}")
        return

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    async with async_session() as session:
        existing_langs = await session.execute(select(Language))
        if existing_langs.scalars().first():
            print("Data already exists, skipping initialization")
            return

        for term_name, term_data in data.get("glossary", {}).items():
            glossary = GlossaryTerm(
                term=term_name,
                definition=term_data.get("definition", ""),
                characteristics=term_data.get("characteristics", []),
                example=term_data.get("example", ""),
                related_concepts=term_data.get("related_concepts", []),
            )
            session.add(glossary)

        for lang_key, lang_data in data.get("languages", {}).items():
            language = Language(
                key=lang_key,
                name=lang_data.get("name", ""),
                description=lang_data.get("description", ""),
            )
            session.add(language)
            await session.flush()

            for elem_data in lang_data.get("elements", []):
                element = Element(
                    element_id=elem_data.get("id", ""),
                    name=elem_data.get("name", ""),
                    description=elem_data.get("description", ""),
                    search_keywords=elem_data.get("search_keywords", []),
                    technical_explanation=elem_data.get("technical_explanation", ""),
                    metaphor_explanation=elem_data.get("metaphor_explanation", ""),
                    examples=elem_data.get("examples", []),
                    syntax_notes=elem_data.get("syntax_notes", []),
                    related_terms=elem_data.get("related_terms", []),
                    language_key=lang_key,
                )
                session.add(element)

        await session.commit()
        print("Data initialization completed successfully")
