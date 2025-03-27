from abc import *
from typing import Any
from enum import Enum
from functools import total_ordering

DamageType = Enum('DamageType', ['BASIC', 'BURNY', 'DAMPY', 'ZAPPY', 'LEAFY'])

@total_ordering
class Saalmon(ABC):
    _level: int
    _health: int
    _damage_type: DamageType

    @abstractmethod
    def __init__(self, level: int, health: int, type: DamageType) -> None:
        self._level = level
        self._health = health
        self._damage_type = type

    def take_damage(self, dmg: int, type: DamageType) -> int:
        self._health -= dmg
        return self._health
    
    def get_species(self) -> str:
        return type(self).__name__
    
    def get_health(self) -> int:
        return self._health
    
    def get_level(self) -> int:
        return self._level
    
    def get_damage_type(self) -> DamageType:
        return self._damage_type

    def __str__(self) -> str:
        return f'{type(self).__name__} [{self._level}]: {self._health} HP'
    
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, type(self)):
            return False
        return self.get_health() == other.get_health()
    
    def __lt__(self, other: Any):
        if not isinstance(other, type(self)):
            return False
        return self.get_health() < other.get_health()
    