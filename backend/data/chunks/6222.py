    def __init__(self):
        self._locales: Dict[str, Set[GNUTranslations]] = {}
        self._language: str = self.set_language()