    @classmethod
    def valid_database_url_(cls, values):
        # set default file upload api.
        file_upload_api = f"post:{values.get('site_path', '')}/file/upload"
        values.setdefault("amis_image_receiver", file_upload_api)
        values.setdefault("amis_file_receiver", file_upload_api)
        # set default database url.
        if not values.get("database_url") and not values.get("database_url_async"):
            values.setdefault(
                "database_url_async",
                "sqlite+aiosqlite:///amisadmin.db?check_same_thread=False",
            )
        return values