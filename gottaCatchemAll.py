class Pokemon:
    def __init__(self, pokeName, region, attackPow, defense, specialAtt, pokeType):
        self.pokeName = pokeName
        self.region = region
        self.attackPow = attackPow
        self.defense = defense
        self.specialAtt = specialAtt
        self.pokeType = pokeType
        
pokemon1 = Pokemon(
    'Picachu', 
    'USA',
    78,
    55,
    93,
    'Electricity',)
pokemon2 = Pokemon(
    'Charazard', 
    'USA',
    89,
    70,
    71,
    'Fire',)
pokemon3 = Pokemon(
    'Squirtle', 
    'USA',
    61,
    90,
    74,
    'Water',
)
class Trainer(object):
    def __init__(self, name, region, pokelist):
        self.name = name
        self.region = region
        self.pokelist = pokelist  # list of Pokemon objects

# Example usage
# trainer = Trainer(
#     "Ash",
#     "Kanto",
#     [
#         Pokemon("Squirtle", 48, 65, 50, "Water"),
#         Pokemon("Bulbasaur", 49, 49, 65, "Grass"),
#     ],
# )

# print(trainer.name) # Outputs "Ash"
# print(trainer.region) # Outputs "Kanto"
print(pokemon1.pokeName, pokemon1.pokeType, pokemon1.attackPow) # Outputs "
print(pokemon2.pokeName, pokemon2.pokeType, pokemon2.attackPow) # Outputs "
print(pokemon3.pokeName, pokemon3.pokeType, pokemon3.attackPow, pokemon3.defense) # Outputs "
