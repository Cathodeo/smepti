# battle/battle_state.py

from .chara import Chara

class BattleState:
    def __init__(self):
        # Participantes
        self.party = [
            Chara("Yurinka", 100, 0, [0,0,0,0], 0, 1),
            Chara("Ola", 100, 0, [0,0,0,0], 0, 1.2),
            Chara("Markus", 100, 0, [0,0,0,0], 0, 0.7)
        ]
        self.enemies = []
      

        # Turnos
        self.round = 1
        self.turn_order = []
        self.current_actor = None

        # Sistema de cartas
        self.hand = None