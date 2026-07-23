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



# Poison is calculated on current, not max HP, so it is more detrimental the highest your HP % is

def apply_poison():
    for chara in battle_state.party:
        if chara.status == 1:
            chara.hp -= round(chara.hp * 0.2)





