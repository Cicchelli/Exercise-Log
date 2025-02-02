from abc import ABC, abstractmethod


class ManipuladorDeLog(ABC):
    @classmethod
    @abstractmethod
    def log(cls, message):
        raise NotImplementedError
