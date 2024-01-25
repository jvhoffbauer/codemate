    def __call__(
        self,
        page: Union[int, str] = 1,
        perPage: Union[int, str] = None,
        show_total: int = 1,
        orderBy: str = None,
        orderDir: str = "asc",
    ):
        self.page = page if page and page > 0 else self.perPageDefault
        self.perPage = perPage if perPage and perPage > 0 else self.perPageDefault
        if self.perPageMax:
            self.perPage = min(self.perPage, self.perPageMax)
        self.show_total = show_total
        self.orderBy = orderBy
        self.orderDir = orderDir
        return self