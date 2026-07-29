# battle/battle_state.py

from .chara import Chara

class BattleState:
    def __init__(self):
        # Participantes
        self.party = [
            Chara("Yurinka", 100, 0, [0,0,0,0], 0, 1, "Neutral"),
            Chara("Ola", 100, 0, [0,0,0,0], 0, 1.2, "Neutral"),
            Chara("Markus", 100, 0, [0,0,0,0], 0, 0.7, "Neutral")
        ]
        # Enemigos. Para la demo solo hay uno
        self.enemies = [
            Chara("Alicoptor", 800, 0, [0,0,0,0], 0, 0.5, "Machine")
        ]
      

        # Turnos
        self.round = 1
        self.turn_order = []
        self.current_actor = 1

        # Sistema de cartas
        self.hand = []