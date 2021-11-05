from game import constants
from game.action import Action
from game.point import Point
from game.actor import Actor

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects 
    is to update the game state when actor collides.
    
    Stereotype:
        Controller
    """

    def __init__(self, output_service):

        self._output_service = output_service
        self._point = Point
        self._actor = Actor

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        paddle= cast["paddle"][0] # there's only one
        bricks = cast["brick"]
        ball = cast["ball"] # there's only one

        #Check if the ball is bouncing against any of the 4 walls:
    
        x = ball.position
        y = ball.position

            #right wall
        if x >= 80:
            ball.self._point._x *= -1
            #left wall
        if x <= 1:
           ball.self._point._x *= -1
            #top wall
        if y >= 1:
            ball.self._point._y *= -1
            #bottom wall
        if y <= 20:
            self._output_service.game_over()

        #Check if there is the ball collides with any of bricks
        for brick in range(bricks):
            if ball.get_position().equals(brick.get_position()):
                self._output_service.delete_brick(brick)

        
        #Detect collisions between the ball and the paddles
        if ball.get_position().equals(paddle.get_position()):
            ball -= ball.y * -1
