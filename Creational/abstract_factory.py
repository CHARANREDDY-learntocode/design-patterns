from abc import ABC, abstractmethod


class Room:
    pass

class GlassRoom:
    pass

class BrickRoom:
    pass

class Wall:
    pass


class Brick(Wall):
    pass


class Glass(Wall):
    pass


class Building(ABC):
    def __init__(self):
        self.rooms = []

    @abstractmethod
    def get_room(self, number):
        pass

    @abstractmethod
    def get_material(self):
        pass

    def add_room(self, number):
        room = self.get_room(number)
        self.rooms.append(room)


# the shopping & residential things are two different types where most of the things will change.

class Residential(Building): #residential buildings are for living.
    def get_room(self, number):
        print("constructing brick room")
        return BrickRoom()

    def get_material(self):
        print("residential building with bricks")
        return Brick()


class Shopping(Building): #here the shopping building is all together servers a different purpose
    def get_room(self, number):
        print("constructing glass room")
        return GlassRoom()

    def get_material(self):
        print("residential building with glass")
        return Glass()



def make_building(builder: Building):
    builder.get_material()
    builder.add_room("123")
    print("building completed")


make_building(Shopping())
print("===============================================")
make_building(Residential())

