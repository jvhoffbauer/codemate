async def create_file(file: bytes = File(description="A file read as bytes")):
    return {"file_size": len(file)}