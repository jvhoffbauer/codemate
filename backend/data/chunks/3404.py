@app.delete(
    "/{id}",
    status_code=204,
    response_model=None,
)
async def delete_deployment(
    id: int,
    response: Response,
) -> Any:
    response.status_code = 400
    return {"msg": "Status overwritten", "id": id}