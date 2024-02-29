from game import Game
import pygame

CELL_SIZE = 50
EXTRA_INFO_WIDTH = 200
EXTRA_HEIGHT = 50


class Drawer:

    _game: Game
    _screen: pygame.Surface
    _rows: int
    _cols: int
    _height: int

    def __init__(self, game: Game, screen: pygame.Surface):
        self._game = game
        self._screen = screen
        self._rows, self._cols = self._game.get_board().get_size()
        self._height = self._rows * CELL_SIZE

    def draw(self) -> None:
        self._screen.fill("white")
        self._draw_board()
        self._draw_cities()
        self._draw_paths()
        self._draw_players_info()

    def _draw_board(self):
        offset_x, offset_y = EXTRA_INFO_WIDTH, EXTRA_HEIGHT
        font = pygame.font.Font(None, 24)

        for row in range(self._rows + 1):
            for col in range(self._cols + 1):
                pygame.draw.circle(self._screen, "black", (col * CELL_SIZE + offset_x, row * CELL_SIZE + offset_y), 5)

        for row in range(self._rows):
            for col in range(self._cols):
                pygame.draw.rect(
                    self._screen,
                    "black",
                    (col * CELL_SIZE + offset_x, row * CELL_SIZE + offset_y, CELL_SIZE, CELL_SIZE),
                    1,
                )
                r = self._game.get_board().get_resources((row, col))
                text = font.render(str(r), True, "black")
                text_rect = text.get_rect(
                    center=(
                        col * CELL_SIZE + CELL_SIZE // 2 + offset_x,
                        row * CELL_SIZE + CELL_SIZE // 2 + offset_y,
                    )
                )
                self._screen.blit(text, text_rect)

    def _draw_cities(self):
        offset_x, offset_y = EXTRA_INFO_WIDTH, EXTRA_HEIGHT

        cities = self._game.get_board().get_cities()
        for player, coord in cities:
            pygame.draw.circle(
                self._screen, player.get_color(), (coord[1] * CELL_SIZE + offset_x, coord[0] * CELL_SIZE + offset_y), 12
            )

    def _draw_paths(self):
        offset_x, offset_y = EXTRA_INFO_WIDTH, EXTRA_HEIGHT

        paths = self._game.get_board().get_paths()
        for player, path in paths:
            start_pos = (path[0][1] * CELL_SIZE + offset_x, path[0][0] * CELL_SIZE + offset_y)
            end_pos = (path[1][1] * CELL_SIZE + offset_x, path[1][0] * CELL_SIZE + offset_y)
            pygame.draw.line(self._screen, player.get_color(), start_pos, end_pos, 5)

    def _draw_players_info(self):
        player_info_margin = 20
        player_info_width = EXTRA_INFO_WIDTH - 2 * player_info_margin
        total_players = len(self._game.get_players())

        available_height = self._height - 2 * player_info_margin
        player_info_height = available_height // total_players

        for player in self._game.get_players():
            pygame.draw.rect(
                self._screen,
                player.get_color(),
                (
                    player_info_margin,
                    (player.get_id() - 1) * player_info_height + player_info_margin + EXTRA_HEIGHT,
                    player_info_width,
                    player_info_height,
                ),
            )

            font = pygame.font.Font(None, 25)
            text = font.render(f"Player {player.get_id()}", True, "white")
            text_rect = text.get_rect(
                center=(
                    player_info_margin + player_info_width // 2,
                    (player.get_id() - 1) * player_info_height
                    + player_info_margin
                    + player_info_height // 2
                    + EXTRA_HEIGHT,
                )
            )
            self._screen.blit(text, text_rect)
