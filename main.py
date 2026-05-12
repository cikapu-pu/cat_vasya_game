"""Ролевая игра с персонажами и заклинаниями"""
from abc import ABC, abstractmethod


class Spell(ABC):
    """Абстрактный класс для заклинаний"""
    def __init__(self, name: str, damage: int, mana_cost: int) -> None:
        """Инициализация заклинания"""
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    @abstractmethod
    def cast(self) -> int:
        """Метод для применения заклинания.
        Должен возвращать наносимый урон."""
        pass


class Fireball(Spell):
    """Заклинание "Огненный шар" """
    def __init__(self) -> None:
        """Инициализация заклинания "Огненный шар" """
        super().__init__("Fireball", 35, 15)

    def cast(self) -> int:
        """Применение заклинания "Огненный шар". Возвращает наносимый урон."""
        return self.damage


class IceLance(Spell):
    """Заклинание "Ледяное копье" """
    def __init__(self) -> None:
        """Инициализация заклинания "Ледяное копье" """
        super().__init__("Ice Lance", 25, 10)

    def cast(self) -> int:
        """Применение заклинания "Ледяное копье". Возвращает наносимый урон."""
        return self.damage


class LightningBolt(Spell):
    """Заклинание "Молния" """
    def __init__(self) -> None:
        """Инициализация заклинания "Молния" """
        super().__init__("Lightning Bolt", 40, 20)

    def cast(self) -> int:
        """Применение заклинания "Молния". Возвращает наносимый урон."""
        return self.damage


class Unit(ABC):
    """Абстрактный класс для юнитов"""
    def __init__(self, strength: int, dexterity: int, constitution: int,
                 wisdom: int, intelligence: int, charisma: int) -> None:
        """Инициализация юнита с базовыми характеристиками"""
        self.strength = strength    # сила
        self.dexterity = dexterity  # ловкость
        self.constitution = constitution    # телосложение
        self.wisdom = wisdom    # мудрость
        self.intelligence = intelligence    # интеллект
        self.charisma = charisma    # харизма
        self.spells: list[Spell] = []
        self.mana = 0

    @abstractmethod
    def calculate_max_health(self) -> int:
        """Метод для расчета максимального здоровья юнита"""
        pass

    @abstractmethod
    def calculate_damage(self) -> int:
        """Метод для расчета наносимого урона юнита"""
        pass

    @abstractmethod
    def calculate_defense(self) -> int:
        """Метод для расчета защиты юнита"""
        pass

    def add_spell(self, spell: Spell) -> None:
        """Метод для добавления заклинания юниту"""
        self.spells.append(spell)

    def cast_spell(self, index: int) -> int:
        """Метод для применения заклинания по индексу"""
        spell = self.spells[index]
        if self.mana < spell.mana_cost:
            raise ValueError("Недостаточно маны для использования заклинания.")
        self.mana -= spell.mana_cost
        return spell.cast()


class Character(Unit):
    """Класс для персонажа"""
    def __init__(self, strength: int, dexterity: int, constitution: int,
                 wisdom: int, intelligence: int, charisma: int,
                 character_class: str) -> None:
        """Инициализация персонажа с базовыми характеристиками и классом"""
        super().__init__(strength, dexterity, constitution, wisdom,
                         intelligence, charisma)
        available_classes = ["warrior", "mage", "hunter"]
        if character_class not in available_classes:
            raise ValueError(
                "Некорректный класс персонажа. "
                "Доступные классы: 'warrior', 'mage', 'hunter'.")
        self.character_class = character_class
        self.max_health = self.calculate_max_health()
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()
        self.max_mana = self.calculate_max_mana()
        self.mana = self.max_mana

    def calculate_max_health(self) -> int:
        """Метод для расчета максимального здоровья персонажа
        в зависимости от класса"""
        return int(self.constitution * 10 + self.strength / 2)

    def calculate_damage(self) -> int:
        """Метод для расчета наносимого урона персонажа
        в зависимости от класса"""
        if self.character_class == "warrior":
            return int(self.strength * 2.2 + self.constitution / 3)
        if self.character_class == "mage":
            return int(self.intelligence * 2.5 + self.wisdom / 2)
        if self.character_class == "hunter":
            return int(self.dexterity * 1.9 + self.strength / 3)

    def calculate_defense(self) -> int:
        """Метод для расчета защиты персонажа в зависимости от класса"""
        if self.character_class == "warrior":
            return int(self.constitution * 1.8 + self.strength / 4)
        if self.character_class == "mage":
            return int(self.wisdom * 1.3 + self.intelligence / 6)
        if self.character_class == "hunter":
            return int(self.dexterity * 1.6 + self.constitution / 5)

    def calculate_max_mana(self) -> int:
        """Метод для расчета максимальной маны персонажа
        в зависимости от класса"""
        if self.character_class == "warrior":
            return int(self.intelligence + self.strength / 2)
        if self.character_class == "mage":
            return int(self.intelligence * 3 + self.wisdom)
        if self.character_class == "hunter":
            return int(self.dexterity * 1.5 + self.wisdom / 2)
