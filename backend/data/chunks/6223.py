    def load_translations(self, translations: Dict[str, GNUTranslations]):
        for language, trans in translations.items():
            if language in self._locales:
                self._locales[language].add(trans)
            else:
                self._locales[language] = {trans}