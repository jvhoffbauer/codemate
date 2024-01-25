    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False