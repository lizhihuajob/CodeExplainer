from sqlalchemy import Column, Integer, String, Text, ForeignKey, JSON, TypeDecorator, Table
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from app.database import Base


element_glossary_terms = Table(
    "element_glossary_terms",
    Base.metadata,
    Column("element_id", Integer, ForeignKey("elements.id"), primary_key=True),
    Column("glossary_term_id", Integer, ForeignKey("glossary_terms.id"), primary_key=True),
)


class ExamplesJSON(TypeDecorator):
    impl = JSON
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is None:
            return []
        if not isinstance(value, list):
            raise ValueError("examples must be a list")
        for item in value:
            if not isinstance(item, dict):
                raise ValueError("Each example must be a dictionary")
            if "title" not in item:
                raise ValueError("Each example must have a 'title' key")
            if "code" not in item:
                raise ValueError("Each example must have a 'code' key")
            if not isinstance(item["title"], str):
                raise ValueError("'title' must be a string")
            if not isinstance(item["code"], str):
                raise ValueError("'code' must be a string")
        return value


class Language(Base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(50), unique=True, nullable=False, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, default="")

    elements = relationship("Element", back_populates="language", cascade="all, delete-orphan")


class Element(Base):
    __tablename__ = "elements"

    id = Column(Integer, primary_key=True, index=True)
    element_id = Column(String(100), unique=True, nullable=False, index=True)
    name = Column(String(200), nullable=False)
    description = Column(Text, default="")
    search_keywords = Column(JSON, default=list)
    technical_explanation = Column(Text, default="")
    metaphor_explanation = Column(Text, default="")
    examples = Column(ExamplesJSON, default=list)
    syntax_notes = Column(JSON, default=list)
    related_terms = Column(JSON, default=list)
    language_key = Column(String(50), ForeignKey("languages.key"), nullable=False)

    language = relationship("Language", back_populates="elements")
    glossary_terms = relationship(
        "GlossaryTerm",
        secondary=element_glossary_terms,
        back_populates="elements",
    )


class GlossaryTerm(Base):
    __tablename__ = "glossary_terms"

    id = Column(Integer, primary_key=True, index=True)
    term = Column(String(100), unique=True, nullable=False, index=True)
    definition = Column(Text, default="")
    characteristics = Column(JSON, default=list)
    example = Column(Text, default="")
    related_concepts = Column(JSON, default=list)

    elements = relationship(
        "Element",
        secondary=element_glossary_terms,
        back_populates="glossary_terms",
    )
