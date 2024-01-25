@app.get(
    "/items/validlist-exclude-unset",
    response_model=List[Item],
    response_model_exclude_unset=True,
)
def get_validlist_exclude_unset():
    return [
        Item(aliased_name="foo"),
        Item(aliased_name="bar", price=1.0),
        Item(aliased_name="baz", price=2.0, owner_ids=[1, 2, 3]),
    ]