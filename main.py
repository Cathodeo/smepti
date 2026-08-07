from direct.showbase.ShowBase import ShowBase
from panda3d.core import DirectionalLight, AmbientLight

import simplepbr

from actors import Ola, Alicoptor

from battle import BattleState
from battle.attacks import *


from panda3d.core import DirectionalLight, AmbientLight
import simplepbr

from battle import BattleState


class MyApp(ShowBase):

    def __init__(self):

        self.battle = BattleState()
        super().__init__()

        # Inicializa el pipeline PBR
        simplepbr.init()
        base.disableMouse()
        
        # ==========================
        # Luces
        # ==========================

        # Luz ambiental suave
        alight = AmbientLight("ambient")
        alight.setColor((0.25, 0.25, 0.25, 1))
        alnp = self.render.attachNewNode(alight)
        self.render.setLight(alnp)

        # Luz direccional (sol)
        dlight = DirectionalLight("sun")
        dlight.setColor((1, 1, 1, 1))

        dlnp = self.render.attachNewNode(dlight)
        dlnp.setHpr(45, -45, 0)

        self.render.setLight(dlnp)

        # ==========================
        # Modelo
        # ==========================

        self.ola = Ola(self)
        self.alicoptor = Alicoptor(self)
        self.ola.actor.setPos(-5, -5, 0)
        self.ola.actor.setH(30)
        self.alicoptor.actor.setPos(2, 5, 0)
        self.alicoptor.actor.setH(210)
        self.cam.setPos(0, -15, 4)
        self.cam.lookAt(0, 2, 1)




app = MyApp()
app.run()