from typing import List

from fastapi_camelcase import CamelModel


class SuggestionRequest(CamelModel):
    text: str
    line: int
    column: int


class Example(CamelModel):
    text: str
    source: str


class Suggestion(CamelModel):
    examples: List[Example]
