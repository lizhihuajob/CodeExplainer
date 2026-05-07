from pydantic import BaseModel


class ExampleSchema(BaseModel):
    title: str
    code: str


class ElementCreate(BaseModel):
    element_id: str
    name: str
    description: str = ""
    search_keywords: list[str] = []
    technical_explanation: str = ""
    metaphor_explanation: str = ""
    examples: list[ExampleSchema] = []
    syntax_notes: list[str] = []
    related_terms: list[str] = []
    language_key: str


class ElementResponse(BaseModel):
    id: int
    element_id: str
    name: str
    description: str
    search_keywords: list[str]
    technical_explanation: str
    metaphor_explanation: str
    examples: list[ExampleSchema]
    syntax_notes: list[str]
    related_terms: list[str]
    language_key: str

    class Config:
        from_attributes = True


class LanguageCreate(BaseModel):
    key: str
    name: str
    description: str = ""


class LanguageResponse(BaseModel):
    id: int
    key: str
    name: str
    description: str
    elements: list[ElementResponse] = []

    class Config:
        from_attributes = True


class GlossaryTermCreate(BaseModel):
    term: str
    definition: str = ""
    characteristics: list[str] = []
    example: str = ""
    related_concepts: list[str] = []


class GlossaryTermResponse(BaseModel):
    id: int
    term: str
    definition: str
    characteristics: list[str]
    example: str
    related_concepts: list[str]

    class Config:
        from_attributes = True


class SearchQuery(BaseModel):
    query: str
    language: str | None = None


class SearchResult(BaseModel):
    element_id: str
    name: str
    description: str
    language_name: str
    language_key: str
    score: float = 0.0
