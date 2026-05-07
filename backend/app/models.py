from sqlalchemy import Column, Integer, String, Text, ForeignKey, JSON
from sqlalchemy.orm import relationship

from app.database import Base


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
    examples = Column(JSON, default=list)
    syntax_notes = Column(JSON, default=list)
    related_terms = Column(JSON, default=list)
    language_key = Column(String(50), ForeignKey("languages.key"), nullable=False)

    language = relationship("Language", back_populates="elements")


class GlossaryTerm(Base):
    __tablename__ = "glossary_terms"

    id = Column(Integer, primary_key=True, index=True)
    term = Column(String(100), unique=True, nullable=False, index=True)
    definition = Column(Text, default="")
    characteristics = Column(JSON, default=list)
    example = Column(Text, default="")
    related_concepts = Column(JSON, default=list)
