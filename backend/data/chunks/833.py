    @property
    def is_debug(self):
        return self in (self.LOCAL, self.STAGING, self.TESTING)