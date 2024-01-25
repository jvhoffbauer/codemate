    def __getattr__(self, item):
        if item == "cloned_field":
            return self.__dict__[item]
        return self.__dict__["_update"].get(
            item, getattr(self.__dict__["_modelfield"], item)
        )