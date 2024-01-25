    def __init__(
        self,
        admin: BaseActionAdmin,
        *,
        action: Action = None,
        flags: List[str] = None,
        getter: Callable[[BaseActionAdmin, Request], ActionT] = None,
        **kwargs,
    ):
        AdminAction.__init__(
            self, admin, action=action, flags=flags, getter=getter, **kwargs
        )
        self.router = self.admin.router
        self.schema = self.schema or BaseModel
        FormAdmin.__init__(self, self.admin.app)