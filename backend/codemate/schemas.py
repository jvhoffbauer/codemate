from fastapi_camelcase import CamelModel


class SuggestionRequest(CamelModel):
    context: str


class Suggestion(CamelModel):
    code: str
