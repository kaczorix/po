from ursina import *
from ursina.prefabs.firt_person_controller \
import FirstPersonController

app = Ursina()
ground = Entity(model= 'plane', texture= 'grass', collider= 'mesh', scale= (100,1, 100))

player = FirstPersonController

app.run
