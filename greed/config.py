# simple, importable class purely intended to hold config variables

class Config:
    def __init__(self):
        """ Hold's the configuration values used to direct the game. 

        Attributes:
            __target_framerate (int): Controls speed of player movement
            __gravity_ticks_per_second (int): The ticks per second
            __max_width (int): The width of the game window
            __max_height (int): The height of the game window
            __cell_size (int): The sixe of each cell in the game window
            __window_title (str): The title of the game displayed in the window frame
            __default_NPC_count (int): Number of actors (NPC's) that can be displayed in the game window at a time
            __jump_height (int): Number of cells, not pixels, the player can jump.

        """
        self.__target_framerate = 24 # controls speed of player movement, and realistically not much else
        self.__gravity_ticks_per_second = 2
        self.__max_width = 900
        self.__max_height = 600
        self.__cell_size = 15
        self.__window_title = "Greed"
        self.__default_NPC_count = 40
        self.__jump_height = 3 # number of cells, not pixels
    
    def get_target_framerate(self):
        """Returns the target framerate.
        """
        return self.__target_framerate

    def get_gravity_frames_per_tick(self):
        """Returns the gravity frames per tick.
        """
        return int(self.__target_framerate / self.__gravity_ticks_per_second)
    
    def get_cell_size(self):
        """Returns the cell size.
        """
        return self.__cell_size

    def get_max_width(self):
        """Returns the max width for the game window.
        """
        return self.__max_width

    def get_column_count(self):
        """Returns the number of columns in the game window.
        """
        return int(self.__max_width / self.__cell_size)

    def get_max_height(self):
        """Returns the max height of the game window.
        """
        return self.__max_height    
    
    def get_row_count(self):
        """Returns the number of rows in the game window.
        """
        return int(self.__max_height / self.__cell_size)
    
    def get_window_title(self):
        """Returns the window title.
        """
        return self.__window_title
    
    def get_default_NPC_count(self):
        """Returns the number of NPC's displayed in the game window.
        """
        return self.__default_NPC_count

    def get_jump_height(self):
        """Returns the number of cells high the player can jump.
        """
        return self.__jump_height