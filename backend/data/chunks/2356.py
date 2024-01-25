async def get_user(user_id: str, request: Request):
    route: APIRoute = request.scope["route"]
    return {"user_id": user_id, "path": route.path}