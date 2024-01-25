@app.get(
    "/exclude_defaults",
    response_model=ModelDefaults,
    response_model_exclude_defaults=True,
)
def get_exclude_defaults() -> ModelDefaults:
    return ModelDefaults(x=None, y="y")