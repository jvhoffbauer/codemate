async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}