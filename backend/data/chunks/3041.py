@app.get(
    "/exclude_unset", response_model=ModelDefaults, response_model_exclude_unset=True
)
def get_exclude_unset() -> ModelDefaults:
    return ModelDefaults(x=None, y="y")