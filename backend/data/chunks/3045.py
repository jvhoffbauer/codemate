@app.get(
    "/exclude_none", response_model=ModelDefaults, response_model_exclude_none=True
)
def get_exclude_none() -> ModelDefaults:
    return ModelDefaults(x=None, y="y")