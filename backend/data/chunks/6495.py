@V2.get("/locations/{id}", response_model=LocationResponse)
async def get_location_by_id(
    request: Request, id: int, source: Sources = Sources.JHU, timelines: bool = True
):
    """
    Getting specific location by id.
    """
    location = await request.state.source.get(id)

    return {"location": location.serialize(timelines)}