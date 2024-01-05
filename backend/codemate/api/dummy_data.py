from codemate import schemas

suggestions = schemas.Suggestion(
    examples=[
        schemas.Example(
            text="""
import numpy as np
        
def foo():
    return np.zeros(10)
        """,
            source="https://github.com/example1",
            stars=1012,
        ),
        schemas.Example(
            text="""
import pandas as pd

def foo():
    return pd.DataFrame()
        """,
            source="https://github.com/example2",
            stars=107,
        ),
        schemas.Example(
            text="""
import fastapi

def foo():
    return fastapi.FastAPI()
        """,
            source="https://github.com/example3",
            stars=512,
        ),
    ]
)
