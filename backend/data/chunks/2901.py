@app.get("/{repeated_alias}")
def get_parameters_with_repeated_aliases(
    path: str = Path(..., alias="repeated_alias"),
    query: str = Query(..., alias="repeated_alias"),
):
    return {"path": path, "query": query}