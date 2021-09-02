import math
import os


def screen_clear():
  if os.name == 'posix':
      _ = os.system('clear')
  else:
      _ = os.system('cls')

class Inventory(object):
  def __init__(self, player):
    player.player_class

class Skills(object):
  def __init__(self, name, dmg, cost, desc, type, level, stats_bonus):
    self.name = name
    self.dmg = dmg
    self.cost = cost
    self.desc = desc
    self.type = type
    self.level = level
    self.stats_bonus = stats_bonus

  def print_skill(self):
    print(str(self.name))
    print("Cost: "+str(self.cost))
    print("Type: "+str(self.type))
    print("Level: "+str(self.level))
    print("Stats Bonus: "+str(self.stats_bonus))
    print("Desc: " + str(self.desc))
    print('')

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
    self.health = 16
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
    print("Health: " + str(self.health))
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
  def __init__(self, type, name, level, xp, stats_bonus, skills, inventory):
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
    self.skills = skills,
    self.inventory = inventory
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
    print("Health: " + str(self.health))
    print("Level: "+str(self.level))
    print("XP: "+str(self.xp)+"/"+str(self.xp_cap))
    print("Strength: "+str(self.strength))
    print("Intelligence: "+str(self.intelligence))
    print("Wisdom: "+str(self.wisdom))
    print("Stamina: "+str(self.stamina))
    print("Stats Bonus: "+str(self.stats_bonus))
    print('')

  def attack(self, skill, action):
    dmg = 0
    if(action == "normal_attack"):
        dmg = (self.strength + self.agility) * 0.08
    elif (skill.type == "melee" and action == "skill"):
        dmg = ((self.strength * (0.1)) +
                (self.agility * (0.08))) + skill.dmg
    elif (skill.type == "magic" and action == "skill"):
        dmg = skill.dmg * (self.intelligence + self.wisdom) * 0.08
    return dmg


def combat(player, mob):
  while(mob.health > 0 and player.health > 0):
    screen_clear()
    if(mob.health > 0 and player.health > 0):
        valid_opt = False
        while(valid_opt == False):
          mob.show_mob_stats()
          player.show_stats()

          print("------- Player Phase -------")
          print("1 -> Attack")
          print("2 -> Inventory")
          print("3 -> Fortify")
          print("4 -> Run")
          choice = str(input())

          if(choice == "1" or choice == 'attack' or choice == 'Attack'):
            valid_opt = True
            player_dmg = player.attack("", "normal_attack")
            player_dmg = player_dmg * \
                ((mob.strength + mob.agility) * 0.15)
            mob.health = math.ceil(mob.health - player_dmg)
            print(">> Player delas " +
                  str(math.ceil(player_dmg)) + " damage!")
          elif(choice == "2" or choice == 'inventory' or choice == 'Inventory'):
            b = 2
          elif(choice == "3" or choice == 'fortify' or choice == 'Fortify'):
            valid_opt = True
            c = 3
          elif(choice == "4" or choice == 'run' or choice == 'Run'):
            valid_opt = True
            return 1
          else:
            print("** Choose a valid option **")
            valid_opt = False
        action = input()
        del(action)
    if(mob.health > 0 and player.health > 0):
        print("------- Enemy Phase -------")
        mob_dmg = math.ceil(
            (1 + (mob.agility + mob.strength) * 0.15) / (player.agility + player.strength))
        player.health = player.health - mob_dmg
        print(">> Enemy deals " + str(mob_dmg) + " damage!")
        mob.show_mob_stats()
        player.show_stats()
        action = input()
        del(action)
  if(player.health <= 0):
      print(str(player.name) + " has died...")
      return -1
  else:
      return player


def main():
  player = PlayerCharacter(1, 'Player', 0, 0, 0, [], [])
  player.show_stats()
  mob = Mobs(1)
  mob.show_mob_stats()
  player = combat(player, mob)

main()
