    @app.get("/model/{name}", response_model=ModelA)
    async def get_model_a(name: str, model_c=Depends(get_model_c)):
        return {"name": name, "description": "model-a-desc", "foo": model_c}