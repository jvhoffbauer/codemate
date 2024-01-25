@app.get(
    "/items/validdict-exclude-unset",
    response_model=Dict[str, Item],
    response_model_exclude_unset=True,
)
def get_validdict_exclude_unset():
    return {
        "k1": Item(aliased_name="foo"),
        "k2": Item(aliased_name="bar", price=1.0),
        "k3": Item(aliased_name="baz", price=2.0, owner_ids=[1, 2, 3]),
    }