@app.get("/", response_model=Model, response_model_exclude_unset=True)
def get_root() -> ModelSubclass:
    return ModelSubclass(sub={}, y=1, z=0)