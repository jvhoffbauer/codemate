@app.get(
    "/exclude_unset_none",
    response_model=ModelDefaults,
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
)
def get_exclude_unset_none() -> ModelDefaults:
    return ModelDefaults(x=None, y="y")