def fail(resp: Resp) -> Response:
    return JSONResponse(
        status_code=resp.code,
        content=jsonable_encoder(
            {
                "status": resp.status,
                "msg": resp.msg,
            }
        ),
    )