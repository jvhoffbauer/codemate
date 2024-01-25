async def create_item(request: Request):
    raw_body = await request.body()
    data = magic_data_reader(raw_body)
    return data