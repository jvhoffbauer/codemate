@router.websocket("/custom_error/")
async def router_ws_custom_error(websocket: WebSocket):
    raise CustomError()