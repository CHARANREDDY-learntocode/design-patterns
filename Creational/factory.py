class Light:
    pass


class Fan:
    pass


class TV:
    pass

class AndroidTV(TV):
    pass


class Room:
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)


class RoomFactory:
    def build_room(self):
        room = self.make_room()

        light = self.make_light()
        fan = self.make_fan()
        tv = self.make_tv()

        room.add_component(light)
        room.add_component(fan)
        room.add_component(tv)

    # in this pattern, the base class defines the basic expected object
    # if you are building the SmartRoom, you can inherit the base class and return a different object
    def make_room(self):
        return Room()

    def make_light(self):
        return Light()

    def make_fan(self):
        return Fan()

    def make_tv(self):
        return TV()


class SmartTVRoomFactory:
    def make_tv(self): #the subclass is deciding the object to return (only TV changing)
        return AndroidTV

