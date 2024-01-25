def ok(
    *,
    data: Union[list, dict, str] = None,
    pagination: dict = None,
    msg: str = "success"
) -> Response:
    return JSONResponse(
        status_code=http_status.HTTP_200_OK,
        content=jsonable_encoder(
            {"status": 200, "msg": msg, "data": data, "pagination": pagination}
        ),
    )