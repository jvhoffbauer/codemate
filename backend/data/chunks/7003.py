    def probe(
        http_response: Response,
        data: str = Body(..., examples=["123"]),
    ) -> str:
        http_response.set_cookie(key="probe-cookie", value=data)
        http_response.status_code = 404
        return data