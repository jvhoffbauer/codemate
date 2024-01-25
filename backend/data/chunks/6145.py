    @classmethod
    def valid_url_(cls, url: str):
        return url[:-1] if url.endswith("/") else url