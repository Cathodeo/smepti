class Chara:

   def __init__(self, name, hp, status, buffs, status_countdown, def_factor, element):
        self.name = name
        self.hp = hp
        self.status = status
        self.buffs = buffs
        self.status_countdown = status_countdown
        self.def_factor = def_factor
        self.element = element

# Statuses will be hardcoded for the demo:

# 1 means Poison. 2 means Paralysis. 3.  means Recoil 10. 'means thermal shield' 11. Radiation poison
   