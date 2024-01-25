async def create_file(file: bytes = File()):
    return {"file_size": len(file)}