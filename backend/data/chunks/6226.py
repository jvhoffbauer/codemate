    @lru_cache()  # noqa: B019
    def gettext(self, value: str, language: str = None) -> str:
        language = language or self._language
        if language in self._locales:
            for trans in self._locales[language]:
                # noinspection PyProtectedMember
                if value in trans._catalog:  # type: ignore
                    value = trans.gettext(value)
        return value