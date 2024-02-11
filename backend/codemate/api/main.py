import uvicorn
from fastapi import FastAPI

from codemate.api import schemas
from codemate.api.retrieval import retrieve

app = FastAPI()


@app.post("/suggestion")
def create_suggestion(data: schemas.SuggestionRequest) -> schemas.Suggestion:
    """Create suggestion for the current cursor location in the file."""
    result = retrieve(data.text, data.line, data.column)
    return result


def main():
    # Start the server
    uvicorn.run("codemate.api.main:app", port=8080, reload=True)


if __name__ == "__main__":
    main()
