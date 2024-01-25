        def __init__(self, func):
            self.__doc__ = getattr(func, "__doc__")
            self.func = func