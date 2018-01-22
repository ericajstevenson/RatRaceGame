# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.
 
WALL = '#'
HALL = '.'
SPROUT = '@'

# Constants for the directions the rats will move.

LEFT = -1
RIGHT = 1
NO_CHANGE = 0
UP = -1
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

        >>> rat = Rat('P', 4, 5)
        >>> rat.num_sprouts_eaten
        0
        >>> rat.eat_sprout()
        >>> rat.num_sprouts_eaten
        1
        """
        self.num_sprouts_eaten = self.num_sprouts_eaten + 1

    def __str__(self):
        """ (Rat) -> str

        Return a string representation of the rat.

        >>> rat = Rat('P', 4, 5)
        >>> rat.__str__()
        'P at (4, 5) ate 1 sprouts.'
        
        """
        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol, self.row, self.col, self.num_sprouts_eaten)
        
class Maze:
    """ A 2D maze. """
    
    def __init__(self, maze, rat_1, rat_2):

        """ (Maze, list of list of str, Rat, Rat) -> NoneType
 
        A 2 dimensional maze for the rat!
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
        >>> __str__(maze)
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """
        # Place rats in the maze
        self.maze[self.rat_1.row][self.rat_1.col] = RAT_1_CHAR
        self.maze[self.rat_2.row][self.rat_2.col] = RAT_2_CHAR
        board = ''
        for row in self.maze:
            for value in row:
                board += value
            board += '\n'
        board = board + str(self.rat_1) + '\n'
        board += str(self.rat_2)
            
        print (board)

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

        # Place rats in the maze at given row and col
        self.maze[self.rat_1.row][self.rat_1.col] = self.rat_1.symbol
        self.maze[self.rat_2.row][self.rat_2.col] = self.rat_2.symbol

        # Return the character in the maze at given row and col
        return self.maze[row][col]

    def move(self, Rat, vert_change, hor_change):

        """ (Maze, Rat, int, int) -> bool

        Move the rat to a new location. Eat sprout if new location contains a sprout.
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
##                
##if __name__ == "__main__":
##    import doctest
##    doctest.testmod()
##  
                
