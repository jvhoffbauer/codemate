@app.get("/callable-dependency")
async def get_callable_dependency(value: str = Depends(callable_dependency)):
    return value