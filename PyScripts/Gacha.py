import random as rng

class Gacha:

    def __init__(self,items):
        self.items = items
        self.pity_counter = 0
    
    def roll(self):
        rarity = {
            "common" : 0.7,
            "rare" : 0.28,
            "legendary" : 0.02
        }
        keys = rarity.keys()
        values = rarity.values()
        rarityChoice = rng.choices(list(keys), weights=values)[0]
        itemsAvailable = [item for item in self.items if item["rarity"] == rarityChoice]
        if itemsAvailable:
            if self.pity_counter <= 70:
                if rarityChoice != "legendary":
                    self.pity_counter += 1
                else:
                    self.pity_counter = 0
                itemPulled = rng.choices(itemsAvailable)[0]
                return itemPulled
            else:
                itemsAvailable = [item for item in self.items if item["rarity"] == 'legendary']
                itemPulled = rng.choices(itemsAvailable)[0]
                self.pity_counter = 0
                return itemPulled
        else:
            print(self.pity_counter)
            print("No items found!")

print("-----Gacha Program-----")
print("")
itemList = [
    {"name":"Soldier's Sword","rarity":"common"},
    {"name":"Colosseum Mace","rarity":"common"},
    {"name":"Iron Battle Axe","rarity":"common"},
    {"name":"Bronze Flail","rarity":"common"},
    {"name":"Bronze Sickle","rarity":"common"},
    {"name":"Blue Steel Blade","rarity":"rare"},
    {"name":"Spartan Spear","rarity":"rare"},
    {"name":"Gold Halberd","rarity":"rare"},
    {"name":"Excalibur","rarity":"legendary"},
    {"name":"Red Scythe","rarity":"legendary"}
]

GachaSystem = Gacha(itemList)
lCounter = 0
rCounter = 0 
cCounter = 0
items = []
for _ in range(int(input("Enter Number of tries: "))):
    Got = GachaSystem.roll()
    print(f"You got the {Got['rarity']} item '{Got['name']}'")
    items.append(Got['name'])
    match Got['rarity']:
        case 'legendary':
            lCounter += 1
        case 'common':
            cCounter += 1
        case 'rare':
            rCounter += 1



print(items)
print(f'Legendary items: {lCounter}, Common items: {cCounter}, Rare items: {rCounter}')
