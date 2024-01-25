    @app.get("/model", response_model=ModelWithDatetimeField)
    def get_model():
        return model