import uvicorn
from fastapi import FastAPI

from codemate import schemas
from codemate.retrieval import retrieve

app = FastAPI()


@app.post("/suggestion")
def echo_input(data: schemas.SuggestionRequest) -> schemas.Suggestion:
    result = retrieve(data.context, data.cursor_line, data.cursor_column)
    return result


def main():
    uvicorn.run("codemate.main:app", port=8080, reload=True)


if __name__ == "__main__":
    main()
