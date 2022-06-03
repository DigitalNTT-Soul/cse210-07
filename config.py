# simple, importable class purely intended to hold config variables

class Config:
    def __init__(self):
        self.__target_framerate = 12
        self.__max_width = 900
        self.__max_height = 600
        self.__cell_size = 15
        self.__column_count = self.__max_width / self.__cell_size
        self.__row_count = self.__max_height / self.__cell_size
        self.__window_title = "Greed"
        self.__default_NPC_count = 40
    
    def get_target_framerate(self):
        return self.__target_framerate
    
    def get_max_width(self):
        return self.__max_width
    
    def get_max_height(self):
        return self.__max_height
    
    def get_cell_size(self):
        return self.__cell_size
    
    def get_column_count(self):
        return self.__column_count
    
    def get_row_count(self):
        return self.__row_count
    
    def get_window_title(self):
        return self.__window_title
    
    def get_default_NPC_count(self):
        return self.__default_NPC_count