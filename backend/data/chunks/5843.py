    @cached_property
    def _select_entities(self) -> Dict[str, Union[InstrumentedAttribute, Label]]:
        return {self.parser.get_alias(insfield): insfield for insfield in self.fields}