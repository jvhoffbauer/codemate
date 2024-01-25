    def AnnotatedSelect(self):
        """Annotated Select, used to automatically perform fastapi dependency injection"""
        return Annotated[Select, Depends(self._select_maker)]