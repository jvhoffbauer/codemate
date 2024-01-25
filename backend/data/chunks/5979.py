    def __init__(
        self,
        pk_admin: "ModelAdmin",
        display_admin: "ModelAdmin",
        link_model: Table,
        link_col: Column,
        item_col: Column,
    ):
        self.link_model = link_model
        self.pk_admin = pk_admin
        self.display_admin = display_admin
        assert self.display_admin, "display_admin is None"
        self.link_col = link_col
        self.item_col = item_col
        assert self.item_col is not None, "item_col is None"
        assert self.link_col is not None, "link_col is None"
        self.path = f"/{self.display_admin.model.__name__}"