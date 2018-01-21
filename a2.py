# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """
    
    def __init__(self,  symbol, row, col):
        """ (Rat, str, int, int) -> NoneType

        Initialize the rat's four instance variables:
        symbol, row, col, num_sprouts_eaten.
        
        >>> rat = Rat('P', 1, 4)
        >>> rat.symbol
        'P'
        >>> rat.col
        4
        >>> rat.row
        1
        >>> rat.num_sprouts_eaten
        0
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        """ (Rat, int, int) -> NoneType

        Set the rat's row and col to the given row and column.

        >>> rat = Rat('P', 3, 1)
        >>> Rat.set_location(rat, 2, 4)
        >>> rat.row
        2
        >>> rat.col
        4
        """
        self.row = row
        self.col = col
    
    def eat_sprout(self):
        """ (Rat) -> NoneType

        Add one sprout to num_sprouts_eaten. Yuck!

        >>> r = Rat('P', 4, 5)
        >>> r.num_sprouts_eaten
        0
        >>> Rat.eat_sprout()
        >>> r.num_sprouts_eaten
        1
        """
        self.num_sprouts_eaten = self.num_sprouts_eaten + 1

    def __str__(self):
        """ (Rat) -> str

        Return a string representation of the rat.

        >>> rat = Rat('P', 1, 3, 4)
        >>> rat.__str__()
        'P at (1, 3) ate 4 sprouts.'
        
        """
        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol, self.row, self.col, self.num_sprouts_eaten)
        
class Maze:
    """ A 2D maze. """
    
    def __init__(self, maze, rat_1, rat_2):

        """ (Maze, list of list of str, Rat, Rat) -> NoneType
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], 
        ['#', '.', '.', '.', '.', '.', '#'], 
        ['#', '.', '#', '#', '#', '.', '#'], 
        ['#', '.', '.', '@', '#', '.', '#'], 
        ['#', '@', '#', '.', '@', '.', '#'], 
        ['#', '#', '#', '#', '#', '#', '#']], 
        Rat('J', 1, 1),
        Rat('P', 1, 4))
        >>>
        """
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2

        sprouts = 0
        for line in maze:
            for elem in line:
                if elem == SPROUT:
                    sprouts += 1
        self.num_sprouts_left = sprouts
                

    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool

        Check to see if there is a wall at given coordinates.
        
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], 
        ['#', '.', '.', '.', '.', '.', '#'], 
        ['#', '.', '#', '#', '#', '.', '#'], 
        ['#', '.', '.', '@', '#', '.', '#'], 
        ['#', '@', '#', '.', '@', '.', '#'], 
        ['#', '#', '#', '#', '#', '#', '#']], 
        Rat('J', 1, 1),
        Rat('P', 1, 4))
        >>> Maze.is_wall(maze, 0, 0) == '#'
        True
        >>> Maze.is_wall(maze, 1, 1) == '#'
        False
        """
        return self.maze[row][col] == WALL

    def get_character(self, row, col):
        """ (Maze, int, int) -> str

        Return the character in the maze at the given row and column.

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], 
        ['#', '.', '.', '.', '.', '.', '#'], 
        ['#', '.', '#', '#', '#', '.', '#'], 
        ['#', '.', '.', '@', '#', '.', '#'], 
        ['#', '@', '#', '.', '@', '.', '#'], 
        ['#', '#', '#', '#', '#', '#', '#']], 
        Rat('J', 1, 1),
        Rat('P', 1, 4))
        >>> Maze.get_character(maze, 4, 5)
        '.'
        >>> Maze.get_character(maze, 3, 4)
        '#'
        >>> Maze.get_character(maze, 3, 3)
        '@'
        >>> Maze.get_character(maze, 1, 1)
        'J'
        >>> Maze.get_character(maze, 1, 4)
        'P'
        """
        elem = self.maze[row][col]
        if self.rat_1.set_location() == (row, col):
            elem = self.rat_1.symbol
        if self.rat_2.set_location() == (row, col):
            elem = self.rat_2.symbol
        return elem

    def move(self, Rat, vert_change, hor_change):

        """ (Maze, Rat, int, int) -> bool
        """
        new_location = (Rat.row + vert_change, Rat.col + hor_change)
        elem = self.get_character(new_location[0], new_location[1])
        if elem == WALL:
            return False
        else:
            Rat.set_location(new_location[0], new_location[1])
            if elem == SPROUT:
                Rat.eat_sprout()
                self.maze[new_location[0], new_location[1]] = HALL
                self.num_sprouts_left -= 1
            return True
                
    def __str__(self):
       """ (Maze) -> str

        Return a string representation of the maze.

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], 
        ['#', '.', '.', '.', '.', '.', '#'], 
        ['#', '.', '#', '#', '#', '.', '#'], 
        ['#', '.', '.', '@', '#', '.', '#'], 
        ['#', '@', '#', '.', '@', '.', '#'], 
        ['#', '#', '#', '#', '#', '#', '#']], 
        Rat('J', 1, 1),
        Rat('P', 1, 4))
        >>> str(maze)
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """
        board = ""
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                char = self.get_character(i, j)
                board += "\n"
            board += str(self.rat_1)
            board += "\n"
            board += str(self.rat_2)
            return board + self.symbol + ' at (' + self.row + ', ' \
            + self.col + ') ate ' + self.num_sprouts_eaten + ' sprouts.'
  
                
