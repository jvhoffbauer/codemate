async def create_files(files: list[bytes] = File()):
    return {"file_sizes": [len(file) for file in files]}