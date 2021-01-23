# В компьютерной игре есть юниты (персонажи).
# Каждый юнит имеет такие характеристики:
# имя
# клан
# здоровье    (int от 1 до 100. Начальное значение 100)
# сила        (int от 1 до 10. Начальное значение 1)
# ловкость    (int от 1 до 10. Начальное значение 1)
# интелект    (int от 1 до 10. Начальное значение 1)
#
# Каждый юнит может лечиться (увеличить свое здоровье на 10 пунктов, максимум 100) - написать метод увеличения здаровья.
#
# Есть три типа юнитов - маги, лучники и рыцари.
# У магов есть дополнительная характеристика - тип магии (воздух, огонь, вода)
# У лучников есть дополнительная характеристика - тип лука (лук, арбалет)
# У рыцарей есть дополнительная характеристика - тип оружия (меч, топор, пика)

# Каждый юнит может увеличить свой базовый навык на 1 пункт, максимум 10.
# Маг увеличивает интелект.
# Лучник увеличивает ловкость.
# Рыцарь увеличивает силу.
# Написать метод увеличения базового навыка (в родительском классе).

# Предложить свою реализацию классов Unit, Mage, Archer, Knight.

class Unit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = 100
        self._strength = 1
        self._agility = 1
        self._intellect = 1
        self._stats_point = 1

    @property
    def strength(self):
        return self._strength

    @property
    def agility(self):
        return self._agility

    @property
    def intellect(self):
        return self._intellect

    # def __repr__(self):
    #     return f"Name: {self.name}, clan: {self.clan}, health: {self.health}, strength: {self.strength}"

    def self_harm(self):
        if self.health < 10:
            self.health = 11
        elif self.health <= 100:
            self.health -= 10

    def self_heal(self):
        if self.health <= 90:
            self.health += 10
        elif self.health > 90 < 101:
            self.health = 100

    def increase_stats(self):
        if self._stats_point < 10:
            self._stats_point += 1


class Mage(Unit):
    def __init__(self, name, clan, type_magic):
        super(Mage, self).__init__(name, clan)
        self.type_magic = type_magic

    @property
    def intellect(self):
        return self._stats_point


class Archer(Unit):
    def __init__(self, name, clan, bow_type):
        super(Archer, self).__init__(name, clan)
        self.bow_type = bow_type

    @property
    def agility(self):
        return self._stats_point


class Knight(Unit):
    def __init__(self, name, clan, weapon_type):
        super(Knight, self).__init__(name, clan)
        self.weapon_type = weapon_type

    @property
    def strength(self):
        return self._stats_point



# knight_1 = Knight("Silver", "Moon", "Two handed pike")
# print(knight_1)
# knight_1.increase_stats()
# knight_1.self_harm()
# print(knight_1)
# knight_1.self_heal()
# print(knight_1)