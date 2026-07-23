from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

from panda3d.core import DirectionalLight, AmbientLight
import simplepbr

from battle import BattleState


class MyApp(ShowBase):

    def __init__(self):

        battle = BattleState()
        super().__init__()

        # Inicializa el pipeline PBR
        simplepbr.init()

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

        self.yurinka = Actor("assets/models/yurinka.glb")
        self.yurinka.reparentTo(self.render)
        self.yurinka.loop("walk")
        self.yurinka.setScale(0.75)
        self.camera.lookAt(self.yurinka)
        self.camLens.setFov(400)

        # ==========================
        # Cámara
        # ==========================
        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 60.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont





app = MyApp()
app.run()