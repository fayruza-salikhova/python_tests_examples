class ComponentMeta(type):
    def __new__(cls, name, bases, dct):
        if "render" not in dct:
            raise TypeError(f"Class {name} has to contain method render")
        return super().__new__(cls, name, bases, dct)

class GoodMeta(metaclass=ComponentMeta):
    def render(self):
        print("I am a component with render")

class BadComponent(metaclass=ComponentMeta):
    pass
