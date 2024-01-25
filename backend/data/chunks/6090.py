    def __init__(self, app: "AdminApp"):
        PageAdmin.__init__(self, app)
        AdminGroup.__init__(self, app)
        self.engine = self.engine or self.app.engine
        self.db = get_engine_db(self.engine)
        self._registered: Dict[Type[BaseAdminT], Optional[BaseAdminT]] = {}
        self.__register_lock = False