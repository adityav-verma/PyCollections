from abc import ABC, abstractmethod


class QueueInterface(ABC):

    @abstractmethod
    def push(self, value) -> bool:
        pass

    @abstractmethod
    def pop(self):
        pass
