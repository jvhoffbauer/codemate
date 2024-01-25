    def __iter__(self):
        return ((k, v) for k, v in self.__dict__.items())