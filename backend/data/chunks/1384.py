async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}