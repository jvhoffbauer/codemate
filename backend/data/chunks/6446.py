@APP.middleware("http")
async def add_datasource(request: Request, call_next):
    """
    Attach the data source to the request.state.
    """
    # Retrieve the datas ource from query param.
    source = data_source(request.query_params.get("source", default="jhu"))

    # Abort with 404 if source cannot be found.
    if not source:
        return Response("The provided data-source was not found.", status_code=404)

    # Attach source to request.
    request.state.source = source

    # Move on...
    LOGGER.debug(f"source provided: {source.__class__.__name__}")
    response = await call_next(request)
    return response