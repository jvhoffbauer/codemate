from codemate import schemas
from fastapi import FastAPI

app = FastAPI()


@app.post("/suggestion")
def echo_input(data: schemas.SuggestionRequest) -> schemas.Suggestion:
    return schemas.Suggestion(code='-' * 8 + '\n' + data.context + '\n' + '-' * 8)


def main():
    import uvicorn
    uvicorn.run("codemate.main:app", port=8080, reload=True)


if __name__ == "__main__":
    main()
