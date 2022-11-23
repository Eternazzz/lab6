class SingletonMeta(type):
    _objects = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._objects:
            object = super().__call__(*args, **kwargs)
            cls._objects[cls] = object
        return cls._objects[cls]


class Singleton(metaclass=SingletonMeta):
    def function(self):
        pass
