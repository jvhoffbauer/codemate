    @classmethod
    def get_data_model(cls):
        if cls.__dict__.get("data_model") is not None:
            return cls.data_model
        cls.data_model = cls.build_data_model()
        return cls.data_model