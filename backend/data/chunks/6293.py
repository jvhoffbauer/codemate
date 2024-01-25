        def __init__(self, app: "AdminApp"):
            super().__init__(app)
            self.register_admin(UserAdmin)