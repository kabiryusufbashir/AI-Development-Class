from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def predict(self, prompt: int) -> int:
        pass
