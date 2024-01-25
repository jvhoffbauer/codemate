        @property
        def required(self) -> bool:
            return self.field_info.is_required()