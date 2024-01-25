    def __init__(self, app: "AdminApp"):
        super().__init__(app)
        assert hasattr(
            self.model, "delete_time"
        ), "SoftDeleteModelAdmin需要在模型中定义delete_time字段"