@app.get(
    "/items/valid-exclude-unset", response_model=Item, response_model_exclude_unset=True
)
def get_valid_exclude_unset():
    return Item(aliased_name="valid", price=1.0)