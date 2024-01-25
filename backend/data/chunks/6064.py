    def register_router(self):
        for form in self.link_model_forms:
            form.register_router()
        self.register_crud()
        super(ModelAdmin, self).register_router()
        return self