# actors.py
from direct.actor.Actor import Actor


class Ola:

    def __init__(self, app):

        print("Creando a Ola")

        self.actor = Actor("assets/models/yurinka.glb")

        self.actor.reparentTo(app.render)

        self.actor.loop("BattleBassic")

class Alicoptor:

    def __init__(self, app):

        print("Creando a alicoptor")

        self.actor = Actor("assets/models/alicoptor.glb")

        self.actor.reparentTo(app.render)

        self.actor.loop("hurt")