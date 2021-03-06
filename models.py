import hashlib
import random

class Country(object):
    def __init__(self, name):
        self.border_countries = set()
        self.name = name
        self.owner = None
        self.troops = 0

    def attack(self, country, attacking_troops):
        assert country in self.border_countries
        assert country.owner is not None
        assert country.owner is not self.country.owner
        assert self.troops - attacking_troops >= 1

        if country.troops >= 2:
            defending_die = 2
        elif country.troop == 1:
            defending_die = 1
        else:
            raise NameError('defending country has no troops')

        if attacking_troops >= 3:
            attacking_die = 3
        elif attacking_troops == 2:
            attacking_die = 2
        elif attacking_troops == 1:
            attacking_die = 1
        else:
            raise NameError('attacking country has no troops')

        defending_die = sorted([random.randint(1,6) for i in xrange(defending_die)])
        attacking_die = sorted([random.randint(1,6) for i in xrange(attacking_die)])

        
        

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return isinstance(other, Country) and self.name == other.name

class Continent(object):
    def __init__(self, name, bonus):
        self.name = name
        self.countries = set()
        self.bonus = bonus

    def __hash__(self):
        return hash(self.name)

    def __eq__(self,other):
        return isinstance(other, Continent) and self.name == other.name

class Map(object):
    def __init__(self):
        self.continents = set()
        self.countries = set()

    def add_continent(self,continent):
        self.continents.add(continent)
        self.countries.union(continent.countries)

class Card(object):
    def __init__(self):
        pass

class Player(object):
    def __init__(self, base_url):
        self.base_url = base_url
        self.key = hashlib.md5().hexdigest()
        self.errors = 0
        self.cards = set()
        self.is_neutral = False

class World(object):
    def __init__(self, _map, players):
        self._map = map
        self.players = random.shuffle(players)
