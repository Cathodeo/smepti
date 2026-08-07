from direct.interval.IntervalGlobal import Sequence
from direct.interval.IntervalGlobal import Wait
from direct.interval.IntervalGlobal import Func

import random

import battle_controller


class BattleDirector:

    def __init__(self,
                 app,
                 battle,
                 player,
                 enemy):

        self.app = app

        self.battle = battle

        self.player = player
        self.enemy = enemy

        self.busy = False


def begin_player_turn(self):

    self.busy = False

    print("Player turn")

def player_attack(self, attack, tier):

    if self.busy:
        return

    self.busy = True

    Sequence(

        Func(self.player.actor.play, "spell"),

        Wait(0.8),

        Func(self.switch_enemy_camera),

        Func(self.enemy.actor.play, "hurt"),

        Func(attack.execute, tier),

        Wait(0.5),

        Func(self.enemy_turn)

    ).start()


def enemy_turn(self):

    attack = random.choice(
        self.enemy.attacks
    )

    Sequence(

        Func(self.switch_enemy_camera),

        Func(self.enemy.actor.play, "attack"),

        Wait(0.8),

        Func(self.switch_player_camera),

        Func(self.player.actor.play, "hurt"),

        Func(attack.execute),

        Wait(0.5),

        Func(self.check_battle_end)

    ).start()


def check_battle_end(self):

        if self.battle.party[0].hp <= 0:

            self.player.actor.play("death")

            print("Game Over")

            return

        if self.battle.enemies[0].hp <= 0:

            self.enemy.actor.play("death")

            print("Victory")

            return

        self.begin_player_turn()



def switch_player_camera(self):

    self.app.cam.setPos(
        -2,
        -14,
        2
    )

    self.app.cam.lookAt(
        self.enemy.actor
    )




def switch_enemy_camera(self):

    self.app.cam.setPos(
        2,
        14,
        2
    )

    self.app.cam.lookAt(
        self.player.actor
    )