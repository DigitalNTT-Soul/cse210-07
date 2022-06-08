from game.shared.point import Point
from config import Config
import pyray
import random
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._config = Config()
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._gravity_vector = Point(0,self._config.get_cell_size())
        self._gravity_speed = self._config.get_gravity_frames_per_tick()
        self._gravity_frame = 0
        self._total_score = 0

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the player.
        
        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("players")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the player's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        player = cast.get_first_actor("players")
        artifacts = cast.get_actors("artifacts")
        rocks = cast.get_actors("rocks")
        gems = cast.get_actors("gems")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        
        # for artifact in artifacts:
        #     if player.get_position().equals(artifact.get_position()):
        #         message = artifact.get_message()
        #         banner.set_text(message)
                
        for rock in rocks:
            if player.get_position().equals(rock.get_position()):
                cast.remove_actor("rocks", rock)
                self._total_score = self._total_score -1
                print("-1")
                if self._total_score < 0:
                    self._total_score = 0
                
        for gem in gems:
            if player.get_position().equals(gem.get_position()):
                print("+1")
                cast.remove_actor("gems", gem)
                self._total_score = self.total_score +1 
        
        # implementing gravity here
        self._gravity_frame = (self._gravity_frame + 1) % self._gravity_speed

        if not self._gravity_frame: # triggers gravity effects only when gravity frame resets to 0
            for actor in cast.get_all_actors():
                if not (actor is player and player.get_position().get_y() == max_y - self._config.get_cell_size()):
                    actor.set_velocity(self._gravity_vector)
                    actor.move_next(max_x, max_y) 
        

        # delete actors if they pass through the bottom of the screen

        # add 1-3 actors at the top of the screen
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()