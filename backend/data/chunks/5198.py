    def __init__(self, detail, status_code=None, biz_code=None, errors=None):
        self.status_code = status_code or self.status_code
        self.code = self.status_code or self.code
        self.biz_code = biz_code or self.biz_code
        self.detail = detail or self.detail
        self.errors = errors or []