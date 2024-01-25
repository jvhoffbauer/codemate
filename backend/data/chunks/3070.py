@app.get("/callable-gen-dependency")
async def get_callable_gen_dependency(value: str = Depends(callable_gen_dependency)):
    return value