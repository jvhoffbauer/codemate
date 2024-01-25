@app.get(
    "/a/{id}",
    response_class=JsonApiResponse,
    responses={422: {"description": "Error", "model": JsonApiError}},
)
async def a(id):
    pass  # pragma: no cover