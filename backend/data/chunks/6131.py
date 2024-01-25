    def get_filename(self, file: UploadFile):
        filename = (
            str(uuid.uuid4()).replace("-", "") + os.path.splitext(file.filename)[1]
        )
        return Path().joinpath(time.strftime("%Y%m"), filename).as_posix()