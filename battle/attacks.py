import random
import battle_controller
import battle_state

# the standard accuracy check for every attack.

def acheck(accuracy):
    return random.randint(1, 100) <= accuracy


class Attack:
    def __init__(self, name, description, execute, target_type):
        self.name = name
        self.description = description
        self.execute = execute
        self.target_type = target_type


pocket_crocket = Attack(
    "Pocket Crocket",
    "Launches a miniature nuke. Can backfire on lower tiers",
    execute_pocket_crocket,

)


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


termite_spray = Attack(
    "Termite Spray",
    "Causes a small amount of heat damage. Machines are weak to it. Decreases foe's defense",
    execute_termite
)


def execute_termite_spray(tier, target):
    match tier:
        case 1:
            if acheck(95):
                battle_controller.apply_damage(target, random.randint(15,20))
                battle_controller.apply_buff(target, 1, 1)





biohazard_rain = Attack(
    "Biohazard Rain",
    "Applies standard Poison to all foes, runs an accuracy check every time.",
    execute_biohazard
)



elastopunch = Attack(
    "Elastopunch",
    "Ola extends her prosthetic hand and impacts a single foe. May cause paralysis",
    execute_elastopunch
)
      