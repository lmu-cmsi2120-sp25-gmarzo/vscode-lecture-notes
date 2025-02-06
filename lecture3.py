from abc import *
from typing import Any 

class Saalmon(ABC):

  def __init__(self, health: int, name: str) -> None:
    self.__health: int = health
    self.__name: str = name

  
  def take_damage(self, dmg: int, dmg_type: str) -> int:
    """
    Deals the specified amount of typed damage to this Burnymon

    Params:
    - dmg: int. The amount of damage taken
    - dmg_type: str. The type of damage taken

    Returns:
    - int: The remaining health of this Burnymon
    """
    self.__health -= dmg
    return self.__health

  def get_health(self) -> int:
    return self.__health

  def get_name(self) -> str:
    return self.__name
  
  def __str__(self) -> str:
    return f"{self.__name} {self.__name}"

  def __eq__(self, other: Any) -> bool:
    if not isinstance(other, type(self)):
      return False
    return self.get_name() == other.get_name()
  
  def __hash__(self) -> Any:
    return hash(self.__name)
  
  def __gt__(self, other: 'Saalmon') -> bool:
    return self.__health > other.get_health()
  
  def __lt__(self, other: 'Saalmon') -> bool:
    return self.__health < other.get_health()

class Burnymon(Saalmon):

  def __init__(self, name: str) -> None:
    super().__init__(15, name)

class Dampymon(Saalmon):
  """
  Dampymon incinerate their opponents with teh fire of 5 suns.
  - Start with 25 health
  - Deal dampy damage
  """
  def __init__(self, name:str) -> None:
    super().__init__(25, name)
  
  def take_damage(self, dmg: int, dmg_type: str) -> int:
    """
    Deals the specified amount of typed damage to this Burnymon

    Params:
    - dmg: int - The amount of damage taken
    - dmg_type: str - The type of damage taken

    Returns:
    - int: The remaining health of this Burnymon
    """
    if dmg_type == "burny":
      dmg += 5
    return super().take_damage(dmg, dmg_type)


# lizardont: Burnymon = Burnymon("Pickahu")
# print(lizardont)
# print(lizardont.__health)
# lizardont.take_damage(10, "Burny")
# print(lizardont.__health)

not_charizard: Burnymon = Burnymon("Dave")
not_charizard.take_damage(5, "dampy")
# print(not_charizard.get_health())

sudsturtle: Dampymon = Dampymon("Sudsy")
sudsturtle.take_damage(5, "burny")

# [!] Should print 15 b/c our Dampymon started 
# with 25 health and took 5 base damage and
# 5 bonus burny damage
# print(sudsturtle.get_health())

b1: Burnymon = Burnymon("bob")
b2: Burnymon = Burnymon("bob")
b3: Burnymon = b1

# print(b1 == b1)
# print(b1 == b2)
# print(b1 == b3)
# print(b1 is b2)
# print(b1 is b3)
# print(b1)