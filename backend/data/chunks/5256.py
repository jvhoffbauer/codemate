    def partial_from_dict(self, obj: dict[str, Any], *fields: str):
        if not fields:
            for k, v in obj.items():
                setattr(self, k, v)
        else:
            for field in fields:
                setattr(self, field, obj[field])