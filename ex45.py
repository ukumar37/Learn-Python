# Class and Method hierarchy -
#
# Map
#	- opening_scene
#	- next_scene
# Engine
#	- play
# Scene
#	- enter
#	* college cafe
#	* guest house
#	* factory
#	* drug house
#	* dentist
#	* save calcutta

class Scene(object):

    def enter(self):
        pass()
        
class Engine(object):

    def __init__(self, scene_map):
        pass
        
    def play(self):
        pass
        
class CollegeCafe(object):

    def enter(self):
        pass()
        
class GuestHouse(object):

    def enter(self):
        pass
        
class Factory(object):

    def enter(self):
        pass
        
class DrugHouse(object):

    def enter(self):
        pass
        
class Dentist(object):

    def enter(self):
        pass
        
class SaveCalcutta(object):

    def enter(self):
        pass
        
class Map(object):

    def __init__(self, start_scene):
        pass
        
    def opening_scene(self):
        pass
        
    def next_scene(self, scene_name):
        pass
        
a_map = Map('college_cafe')
a_game = Engine(a_map)
a_game.play()