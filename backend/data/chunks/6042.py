    def get_link_model_forms(self) -> List[LinkModelForm]:
        self.link_model_forms = list(
            filter(
                None,
                [
                    LinkModelForm.bind_model_admin(self, insfield)
                    for insfield in self.link_model_fields
                ],
            )
        )
        return self.link_model_forms