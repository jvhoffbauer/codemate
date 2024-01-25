    def to_result(self):
        rv = {"detail": self.detail}
        if self.code:
            rv["code"] = self.code
        if self.biz_code:
            rv["biz_code"] = self.biz_code
        if self.errors:
            rv["errors"] = self.errors
        return ORJSONResponse(rv, status_code=self.status_code)