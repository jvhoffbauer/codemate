    def is_deployed(self) -> bool:
        return self in (self.STAGING, self.PRODUCTION)