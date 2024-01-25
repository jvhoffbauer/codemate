@router.get("/", dependencies=[Depends(get_token_data)])
async def home():
    return "Hello World!"