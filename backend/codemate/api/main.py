import uvicorn
from fastapi import FastAPI

from codemate.api import schemas
from codemate.api.retrieval import retrieve

app = FastAPI()


@app.post("/suggestion")
def echo_input(data: schemas.SuggestionRequest) -> schemas.Suggestion:
    result = retrieve(data.text, data.line, data.column)
    return result


def main():
    uvicorn.run("codemate.api.main:app", port=8080, reload=True)


if __name__ == "__main__":
    main()
