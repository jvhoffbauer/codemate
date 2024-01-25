    def __setattr__(self, key, value):
        self.__dict__["_update"][key] = value