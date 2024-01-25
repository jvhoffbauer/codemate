    @cached_property
    def model_insfields(self) -> List[SqlaInsAttr]:
        return self.parser.filter_insfield(self.model.__dict__.values())