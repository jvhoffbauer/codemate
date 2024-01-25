async def read_system_status(current_user: User = Depends(get_current_user)):
    return {"status": "ok"}