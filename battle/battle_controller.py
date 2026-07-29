import random
import battle_state
from .chara import Chara


def gen_hand():
    battle_state.hand.clear()
    for i in range(5):
        battle_state.hand.append(random.randint(1, 4))

        
def dec_status_countdown():
    for chara in battle_state.party:
        chara.status_countdown -= 1
        if chara.status_countdown == 0:
             print(chara.name + " got rid of its status.")
             chara.status = 0



# Poison is calculated on current, not max HP, so it is more detrimental the highest your HP % is

def apply_poison_dmg():
    for chara in battle_state.party:
        if chara.status == 1:
            chara.hp -= round(chara.hp * 0.2)
    for chara in battle_state.enemies:
        if chara.status == 1:
                    chara.hp -= round(chara.hp * 0.2)


def apply_radiation_dmg():
    for chara in battle_state.party:
        if chara.status == 11:
            chara.hp -= 10
            chara.status_countdown -=1
    for chara in battle_state.enemies:
        if chara.status == 11:
                chara.hp -= 10
                chara.status_countdown -=1


def apply_damage(target, amount):
    revised_def_factor = calc_defense_factor(target.def_factor, target.buffs[1])
    final_amount = amount * revised_def_factor
    target.hp -= final_amount


def apply_buff(target, amount, whichstat):
    target.buffs[whichstat] += amount



def apply_status(target, status_id, countdown):
    target.status = status_id
    target.status_countdown = countdown



def calc_defense_factor(base, stacks, alpha=0.6):
    if stacks < 0:
        # Debuffs: acerca el factor a 1 (más daño)
        return 1 - (1 - base) * (alpha ** abs(stacks))
    else:
        # Buffs: reduce aún más el daño
        return base * (alpha ** stacks)




# apply_damage(0, 25, battle_state.party)      / Yurinka recibe 25 de daño
# apply_damage(1, 10, battle_state.enemies)    / Enemigo 2 recibe 10 de daño


