@app.get(
    "/items/coerce-exclude-unset",
    response_model=Item,
    response_model_exclude_unset=True,
)
def get_coerce_exclude_unset():
    return Item(aliased_name="coerce", price="1.0")