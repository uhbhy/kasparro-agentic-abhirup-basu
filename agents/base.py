# agents/base.py

from abc import ABC, abstractmethod
from typing import Any


class Agent(ABC):
    """Base class for all agents."""

    @abstractmethod
    def run(self, input_data: Any) -> Any:
        ...
