    @property
    def AnnotatedPage(self):
        """Annotated Page, for fastapi dependency injection"""
        return Annotated[Page, Depends(self.get_page)]