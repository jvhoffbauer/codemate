    def set_language(self, language: str = None) -> str:
        """
        Set the i18n localization language. If it is empty, try to read the environment variable `LANGUAGE`/`LANG`,
        the system default language, in turn.
        :param language: the language to try to set
        :return: the language after the successful setting
        """
        language = (
            language
            or os.getenv("LANGUAGE")
            or os.getenv("LANG")
            or locale.getlocale()[0]
            or "en_US"
        )
        self._language = (
            "zh_CN" if language.lower().startswith(("zh", "chinese")) else language
        )
        I18N.gettext.cache_clear()  # clear cache after language has changed
        gc.collect()
        return self._language