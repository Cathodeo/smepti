import random

from battle.battle_controller import *


# The standard accuracy check for every attack.
def acheck(accuracy):
    return random.randint(1, 100) <= accuracy


class Attack:
    def __init__(self, name, description, execute, target_type):
        self.name = name
        self.description = description
        self.execute = execute
        self.target_type = target_type


def miss():
    print("The attack missed!")

# Pocket Crocket is always AOE and against foes.
def execute_pocket_crocket(tier):

    match tier:

        case 1:
            if acheck(70):
                for chara in battle_state.enemies:
                    battle_controller.apply_damage(chara, random.randint(22, 28))
                print("The pocket crocket was launched. It landed on the enemies!")
            else:
                for chara in battle_state.party:
                    battle_controller.apply_status(chara, 11, 3)
                print("The pocket crocket missed the enemies and the blast poisoned Ola and co")

        case 2:
            if acheck(80):
                for chara in battle_state.enemies:
                    battle_controller.apply_damage(chara, random.randint(28, 35))
                print("The pocket crocket was launched. It landed on the enemies!")
            else:
                for chara in battle_state.party:
                    battle_controller.apply_status(chara, 11, 2)
                print("The pocket crocket missed the enemies and the blast poisoned Ola and co")

        case 3:
            if acheck(90):
                for chara in battle_state.enemies:
                    battle_controller.apply_damage(chara, random.randint(35, 40))
                print("The pocket crocket was launched. It landed on the enemies!")
            else:
                print("The pocket crocket missed, but no one was harmed.")

        case 4:
            if acheck(95):
                for chara in battle_state.enemies:
                    battle_controller.apply_damage(chara, random.randint(35, 40))
                    battle_controller.apply_status(chara, 11, 2)
                print("The pocket crocket was launched. It landed on the enemies!")
                print("The enemies got radiation poison!")
            else:
                print("The pocket crocket missed, but no one was harmed.")


def execute_termite_spray(tier, target):

    match tier:

        case 1:
            if acheck(95):
                battle_controller.apply_damage(target, random.randint(15, 20))
                battle_controller.apply_buff(target, -1, 1)
                print("The termite burnt the foe!")
            else:
                print("The termite spray narrowly missed the target")

        case 2:
            battle_controller.apply_damage(target, random.randint(20, 25))
            battle_controller.apply_buff(target, -2, 1)
            print("The termite burnt the foe!")

        case 3:
            for chara in battle_state.enemies:
                battle_controller.apply_damage(chara, random.randint(10, 15))
                battle_controller.apply_buff(chara, -2, 1)
            print("The termite burnt all the foes!")

        case 4:
            for chara in battle_state.enemies:
                battle_controller.apply_damage(chara, random.randint(45, 70))
                battle_controller.apply_buff(chara, -3, 1)
            print("The termite severely burnt all the foes!")


def execute_biohazard(tier):

    count_of_poison = 0

    match tier:

        case 4:
            for chara in battle_state.enemies:
                if acheck(100):
                    battle_controller.apply_status(chara, 1, 99)
                    count_of_poison += 1
                    print(str(count_of_poison) + " enemies have been poisoned.")

        case 3:
            for chara in battle_state.enemies:
                if acheck(70):
                    battle_controller.apply_status(chara, 1, 99)
                    count_of_poison += 1
                    print(str(count_of_poison) + " enemies have been poisoned.")

        case 2:
            for chara in battle_state.enemies:
                if acheck(60):
                    battle_controller.apply_status(chara, 1, 5)
                    count_of_poison += 1
                    print(str(count_of_poison) + " enemies have been poisoned.")

        case 1:
            for chara in battle_state.enemies:
                if acheck(60):
                    battle_controller.apply_status(chara, 1, 3)
                    count_of_poison += 1
                    print(str(count_of_poison) + " enemies have been poisoned.")


def execute_thermal_shield():
    for chara in battle_state.enemies:
        chara.element = "Shielded"        

def execute_tail_swing():
    print("Alicoptor swung his tail!")
    for chara in battle_state.party:
        battle_controller.apply_damage(chara, random.randint(20, 25))

def execute_headbutt():
    print("Alicoptor charges forward!")
    #target = randint(1,3)
    # the demo will always have a sole target
    if acheck(60):
        battle_controller.apply_damage(battle_state.party[0], random.randint(10, 15))
        print("The attack connected!")
        if acheck(50):
            print("The attack also made its target flinch!")
            battle_controller.apply_status(battle_state.party[0], 2, 1)
    else:
        miss()





pocket_crocket = Attack(
    "Pocket Crocket",
    "Launches a miniature nuke. Can backfire on lower tiers",
    execute_pocket_crocket,
    "enemies_aoe",
)

termite_spray = Attack(
    "Termite Spray",
    "Causes a small amount of heat damage. Machines are weak to it. Decreases foe's defense",
    execute_termite_spray,
    "enemy",
)

biohazard_rain = Attack(
    "Biohazard Rain",
    "Applies standard Poison to all foes, runs an accuracy check every time.",
    execute_biohazard,
    "enemies_aoe",
)

thermal_shield = Attack(
    "Thermal Shield",
    "Brings up the enemy's thermal shield",
    execute_thermal_shield,
    "self"
)
tail_swing = Attack(
    'Tail Swing',
    "Powerful AOE attack",
    execute_tail_swing,
    "enemies_aoe"
)
headbutt = Attack(
    "Headbutt",
    "Alicoptor charges forward and hits a foe. May cause knockback",
    execute_headbutt,
    "enemy"
)

