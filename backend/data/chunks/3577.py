async def no_body_status_code_exception():
    raise HTTPException(status_code=204)