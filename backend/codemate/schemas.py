from fastapi_camelcase import CamelModel
from typing import List


class SuggestionRequest(CamelModel):
    editor_text: str
    cursor_line: int
    cursor_column: int


class Example(CamelModel):
    text: str
    source: str
    stars: int


class Suggestion(CamelModel):
    examples: List[Example]
