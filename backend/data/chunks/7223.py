@router.get("/", status_code=204)
async def health(session: AsyncSession = Depends(get_session)):
    try:
        await asyncio.wait_for(session.execute("SELECT 1"), timeout=1)
    except (asyncio.TimeoutError, socket.gaierror):
        return Response(status_code=503)
    return Response(status_code=204)