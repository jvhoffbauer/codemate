        async def file_upload(file: UploadFile = File(...)):
            filename = self.get_filename(file)
            file_path = Path(self.file_directory) / filename
            os.makedirs(file_path.parent, exist_ok=True)
            try:
                res = await file.read()
                if self.file_max_size and len(res) > self.file_max_size:
                    return BaseApiOut(status=-2, msg="The file size exceeds the limit")
                async with aiofiles.open(file_path, "wb") as f:
                    await f.write(res)
                return BaseApiOut(
                    data=self.UploadOutSchema(
                        filename=filename, url=f"{self.static_path}/{filename}"
                    ),
                )

            except Exception as e:
                return BaseApiOut(status=-1, msg=str(e))