from abc import ABC, abstractmethod


class Unit(ABC):
    def __init__(self, strength, dexterity, constitution, wisdom, intelligence, charisma):
        self.strength = strength            # сила
        self.dexterity = dexterity          # ловкость
        self.constitution = constitution    # телосложение
        self.wisdom = wisdom                # мудрость
        self.intelligence = intelligence    # интеллект
        self.charisma = charisma            # харизма

    @abstractmethod
    def calculate_max_health(self):
        pass

    @abstractmethod
    def calculate_damage(self):
        pass

    @abstractmethod
    def calculate_defense(self):
        pass


class Character(Unit):
    def calculate_max_health(self):
        return int(self.constitution * 10 + self.strength / 2)

    def calculate_damage(self):
        return int(self.strength * 1.5 + self.dexterity / 4)

    def calculate_defense(self):
        return int(self.constitution * 1.5 + self.dexterity / 3)


class Monster(Unit):
    def calculate_max_health(self):
        return int(self.constitution * 8 + self.strength / 3)

    def calculate_damage(self):
        return int(self.strength * 2 + self.constitution / 5)

    def calculate_defense(self):
        return int(self.constitution * 1.2 + self.strength / 5)