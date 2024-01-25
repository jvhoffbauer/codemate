    def render(self, content: Any) -> bytes:
        """Render JSON.

        Same defaults as starlette.responses.JSONResponse.render but allow NaN to be replaced by null using simplejson
        """
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=None,
            ignore_nan=True,
            separators=(",", ":"),
        ).encode("utf-8")