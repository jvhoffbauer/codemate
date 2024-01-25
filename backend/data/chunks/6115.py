    def as_amis_form(
        self, model: Type[BaseModel], set_default: bool = False, is_filter: bool = False
    ) -> Form:
        """Get amis form from pydantic model.
        Args:
            model: Pydantic model
            set_default: Is set default value
            is_filter: Is filter form
        Returns:
            amis.Form
        """
        form = amis.Form(title=model_config_attr(model, "title", None), size="lg")  # type: ignore
        form.body = [
            self.as_form_item(modelfield, set_default=set_default, is_filter=is_filter)
            for modelfield in model_fields(model).values()
        ]
        # InputSubForm
        return form