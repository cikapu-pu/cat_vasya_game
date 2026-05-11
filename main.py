from abc import ABC, abstractmethod


class Spell(ABC):
    def __init__(self, name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    @abstractmethod
    def cast(self):
        pass


class Fireball(Spell):
    def __init__(self):
        super().__init__("Fireball", 35, 15)

    def cast(self):
        return self.damage
    

class IceLance(Spell):
    def __init__(self):
        super().__init__("Ice Lance", 25, 10)

    def cast(self):
        return self.damage
    

class LightningBolt(Spell):
    def __init__(self):
        super().__init__("Lightning Bolt", 40, 20)

    def cast(self):
        return self.damage


class Unit(ABC):
    def __init__(self, strength, dexterity, constitution, wisdom, intelligence, charisma):
        self.strength = strength            # сила
        self.dexterity = dexterity          # ловкость
        self.constitution = constitution    # телосложение
        self.wisdom = wisdom                # мудрость
        self.intelligence = intelligence    # интеллект
        self.charisma = charisma            # харизма

        self.spells = []
        self.mana = 0

    @abstractmethod
    def calculate_max_health(self):
        pass

    @abstractmethod
    def calculate_damage(self):
        pass

    @abstractmethod
    def calculate_defense(self):
        pass

    def add_spell(self, spell):
        self.spells.append(spell)

    def cast_spell(self, index):
        spell = self.spells[index]

        if self.mana < spell.mana_cost:
            raise ValueError("Недостаточно маны для использования заклинания.")
        
        self.mana -= spell.mana_cost

        return spell.cast()


class Character(Unit):
    def __init__(self, strength, dexterity, constitution, wisdom, intelligence, charisma, character_class):
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)

        if character_class not in ["warrior", "mage", "hunter"]:
            raise ValueError("Некорректный класс персонажа. Доступные классы: 'warrior', 'mage', 'hunter'.")
        
        self.character_class = character_class

        self.max_health = self.calculate_max_health()
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()

        self.max_mana = self.calculate_max_mana()
        self.mana = self.max_mana

    def calculate_max_health(self):
        return int(self.constitution * 10 + self.strength / 2)
    
    def calculate_damage(self):
        if self.character_class == "warrior":
            return int(self.strength * 2.2 + self.constitution / 3)
        
        elif self.character_class == "mage":
            return int(self.intelligence * 2.5 + self.wisdom / 2)
        
        elif self.character_class == "hunter":
            return int(self.dexterity * 1.9 + self.strength / 3)
        
    def calculate_defense(self):
        if self.character_class == "warrior":
            return int(self.constitution * 1.8 + self.strength / 4)
        
        elif self.character_class == "mage":
            return int(self.wisdom * 1.3 + self.intelligence / 6)
        
        elif self.character_class == "hunter":
            return int(self.dexterity * 1.6 + self.constitution / 5)
        
    def calculate_max_mana(self):
        if self.character_class == "warrior":
            return int(self.intelligence + self.strength / 2)
        
        elif self.character_class == "mage":
            return int(self.intelligence * 3 + self.wisdom)
        
        elif self.character_class == "hunter":
            return int(self.dexterity * 1.5 + self.wisdom / 2)
