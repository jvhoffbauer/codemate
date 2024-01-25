    @cached_property
    def _filter_entities(self) -> Dict[str, Union[InstrumentedAttribute, Label]]:
        return {
            self.parser.get_alias(sqlfield): sqlfield
            for sqlfield in self.parser.filter_insfield(
                self.list_filter, save_class=(Label,)
            )
        }