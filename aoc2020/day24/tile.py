class Tile():
    '''Describes a hexagonal tile'''

    def __init__(self):
        # Neighbors
        self.e = None
        self.se = None
        self.sw = None
        self.w = None
        self.nw = None
        self.ne = None