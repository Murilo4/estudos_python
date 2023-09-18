# classes abstratas - abstract base class (abc)
# ABCs são usados como contratos para a definição
# de novas classes. Elas podem forçar outras classes
# a criarem métodos concretos. Também podem ter
# metodos concretos por elas mesmas.
# @abstractmethods são métodos que não têm corpo.
# as regras para classes abstratas com métodos
# abstratos é que elas NÃO PODEM ser instânciadas
# diretamente.
# métodos abstratos DEVEM ser implementados
# nas subclasses (@abstractmethod)
# uma classe abstrata em python tem sua metaclasse
# sendo ABCmeta.
# É possivel criar @property @setter @classmethod
# @staticmethod e @method como abstratos, para isso
# use @abstractmethod como decorador mais interno.

from abc import ABC, abstractmethod

class Log(ABC):
    @abstractmethod
    def _log(self, msg): ...

    def log_error(self, msg):
        return self._log(f'error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'success: {msg}')
    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


l = LogPrintMixin()
l.log_error('oi')