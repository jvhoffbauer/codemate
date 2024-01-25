async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}