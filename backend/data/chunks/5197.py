    def to_response(self):
        return ORJSONResponse(
            self.value,
            status_code=self.status_code,
        )