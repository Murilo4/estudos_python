# abstractmethod para qualquer método já decorado
# é possivel criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso 
# use @abstractmethod como decorador mais interno.
# foo - bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.
from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def _init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    @abstractmethod
    def name(self, name): ...

class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name

foo = Foo('Bar')
print(foo.name)