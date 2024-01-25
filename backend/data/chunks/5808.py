    def __init__(self, modelfield: ModelField, update: Dict[str, Any] = None):
        self.__dict__["_modelfield"] = modelfield
        self.__dict__["_update"] = update or {}