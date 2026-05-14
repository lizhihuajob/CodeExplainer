from sqlalchemy import select

from app.database import async_session
from app.models import Language, Element, GlossaryTerm


async def load_data_from_dict(data: dict):
    async with async_session() as session:
        existing_langs = await session.execute(select(Language))
        if existing_langs.scalars().first():
            print("Data already exists, skipping initialization")
            return

        glossary_map = {}
        for term_name, term_data in data.get("glossary", {}).items():
            glossary = GlossaryTerm(
                term=term_name,
                definition=term_data.get("definition", ""),
                characteristics=term_data.get("characteristics", []),
                example=term_data.get("example", ""),
                related_concepts=term_data.get("related_concepts", []),
            )
            session.add(glossary)
            glossary_map[term_name] = glossary

        await session.flush()

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

                related_term_names = elem_data.get("related_terms", [])
                for term_name in related_term_names:
                    if term_name in glossary_map:
                        element.glossary_terms.append(glossary_map[term_name])

                session.add(element)

        await session.commit()
        print("Data initialization completed successfully")
