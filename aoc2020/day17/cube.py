class Cube(object):
    '''Describes a Conway Cube node'''
    def __init__(self, location: tuple, active: bool):
        self.location = location
        self.active = active
