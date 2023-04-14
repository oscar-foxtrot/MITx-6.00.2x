class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.tiles = {(x, y): False \
            for y in range(height) for x in range(width)}
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        tile = math.floor(pos.getX()), math.floor(pos.getY()) # pos[0] is x, pos[1] is y
        self.tiles[tile] = True
        
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.tiles[(m, n)]
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return len(self.tiles)

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        counter = 0
        for key in self.tiles.keys():
            if self.tiles[key]:
                counter += 1
        return counter

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        pos = random.choice(list(self.tiles.keys()))
        posx = pos[0]
        posy = pos[1]
        return Position(posx, posy)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        try:
            tile = math.floor(pos.getX()), math.floor(pos.getY())
            self.tiles[tile]
        except KeyError:
            return False
        return True
