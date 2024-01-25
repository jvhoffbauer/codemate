    def create_upload_file(file: UploadFile):
        testing_file_store.append(file)
        return {"filename": file.filename}