    def __call__(self, value, language: str = None) -> str:
        return self.gettext(str(value), language)