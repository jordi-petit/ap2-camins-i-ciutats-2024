import places
from player import Player
from board import Board
import yogi


class Game:

    def __init__(self): ...

    def get_board(self) -> Board: ...

    def get_players(self) -> list[Player]: ...

    def get_current_player(self) -> Player: ...

    def is_game_over(self) -> bool: ...
