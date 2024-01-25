    def __getattr__(self, item: str) -> Any:
        self._ensure_var(item)
        try:
            return self._vars[item].get()
        except LookupError:
            self._vars[item].set(None)
            return None