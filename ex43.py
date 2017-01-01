#  THIS GAME IS LAME......


from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print("This scene has not been configured yet.  Subclass it and implement enter()")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

    while current_scene != last_scene:
        next_scene_name = current_scene.enter()
        current_scene = self.scene_map.next_scene(next_scene_name)

    # be sure to print out the last scene
    current_scene.enter()


class Death(Scene):

    def enter(self):
        print("You were eaten by a pack of dead clowns.")
        exit(0)


class CentralCorridor(Scene):

    def enter(self):
        print("There is a Gothon standing in front you of you.",
              "In order to get past him you must kill him with laughter.",
              "Say something funny.")

    while len(joke) > 10:
        print("Say something funny.")
        joke = input("> ")
        if len(joke) > 10:
            print("That joke killed, literally!")
            pass
        else:
            print("Not funny.  He's growing angrier with you.")


class LaserWeaponArmory(Scene):

    def enter(self):
        print("You've approached the Laser Weapon Armory."
              "In order to enter you must guess the digital password."
              "(Hint: it's one digit long)")


class TheBridge(Scene):

    def enter(self):
        pass


class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
