class inventory(object):
    def __init__(self, player):
        player.player_class

class skills(object):
    def __init__(self, name, dmg, cost, desc):
        self.name = name
        self.dmg = dmg
        self.cost = cost
        self.desc = desc

class Mobs(object):
    def __init__(self, mob_type):
        self.type = mob_type
        self.name = None
        self.mob_class = None
        self.level = 0
        self.xp_given = 0
        self.stats_bonus = 0
        self.strength = 0
        self.agility = 0
        self.intelligence = 0
        self.wisdom = 0
        self.stamina = 0
        self.base_stamina = 0
        self.choosen_mob()
    
    def choosen_mob(self):
        if(self.type == 1):
            self.rat()

    def rat(self):
        self.name = 'Rat'
        self.health = 15
        self.mob_class = 'Animal'
        self.level = 0
        self.strength = 9
        self.agility = 10
        self.intelligence = 6
        self.wisdom = 8
        self.stamina = 1
        self.base_stamina = 2
        self.xp_given = 3
    
    def show_mob_stats(self):
        print(str(self.name))
        print("Type: "+str(self.mob_class))
        print("Level: "+str(self.level))
        print("XP: "+str(self.xp_given))
        print("Strength: "+str(self.strength))
        print("Intelligence: "+str(self.intelligence))
        print("Wisdom: "+str(self.wisdom))
        print("Stamina: "+str(self.stamina))
        print("Stats Bonus: "+str(self.stats_bonus))
        print('')

class PlayerCharacter(object):
    def __init__(self, type, name, level, xp, stats_bonus):
        self.player_class = type
        self.name = name
        self.health = 0
        self.mana = 0
        self.rage = 0
        self.level = level
        self.xp = xp
        self.xp_cap = 0
        self.stats_bonus = 0
        self.strength = 0
        self.agility = 0
        self.intelligence = 0
        self.wisdom = 0
        self.stamina = 0
        self.base_stamina = 0
        self.choosen_class()

    def choosen_class(self):
        if(self.player_class == 'Warrior' or self.player_class == 'warrior' or self.player_class == 1):
            self.player_class = 'Warrior'
            self.warrior_class()
    
    def warrior_class(self):
        self.health = 35
        self.mana = -1
        self.rage = 0
        self.stats_bonus = 0
        self.strength = 16
        self.agility = 14
        self.intelligence = 10
        self.wisdom = 12
        self.stamina = 4
        self.base_stamina = 4
        self.xp_cap = 30

    def show_stats(self):
        print("Name: "+str(self.name))
        print(str(self.player_class))
        print("Level: "+str(self.level))
        print("XP: "+str(self.xp)+"/"+str(self.xp_cap))
        print("Strength: "+str(self.strength))
        print("Intelligence: "+str(self.intelligence))
        print("Wisdom: "+str(self.wisdom))
        print("Stamina: "+str(self.stamina))
        print("Stats Bonus: "+str(self.stats_bonus))
        print('')


def combat(player, mob):
    while(mob.health > 0 and player.health > 0):
        if(player.base_stamina >= mob.base_stamina):
            mob.show_mob_stats()
            player.show_stats()
            print("------- Player Phase -------")
            print("1 -> Attack")
            print("inventory")
            print("3 -> Fortify")
            print("4 -> Run")
            choice = input()
            if(choice == 1 or choice == 'attack' or choice == 'Attack'):
                a = 1 
            elif(choice == 2 or choice == 'inventory' or choice == 'Inventory'):
                b = 2
            elif(choice == 3 or choice == 'fortify' or choice == 'Fortify'):
                c = 3
            if(choice == 4 or choice == 'run' or choice == 'Run'):
                d = 4
            else: print("** Choose a valid option **")
        else:
            mob.show_mob_stats()
            player.show_stats()
            print("Enemy Phase:")

def main():
    player = PlayerCharacter(1,'Player',0,0,0)
    player.show_stats()
    mob = Mobs(1)
    mob.show_mob_stats()
    combat(player, mob)

main()
