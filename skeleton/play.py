import pygame

from game import Game
from drawer import Drawer


def loop(game: Game, drawer: Drawer, screen: pygame.Surface, clock: pygame.time.Clock):

    FRAMERATE = 30  # desired frames per second

    running = True
    while running:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE | pygame.K_q:
                            running = False
                        case pygame.K_SPACE | pygame.K_RETURN | pygame.K_KP_ENTER:
                            game.next_turn()
                            drawer = Drawer(game, screen)
                        case _:
                            pass
                case _:
                    pass
        drawer.draw()
        pygame.display.flip()
        clock.tick(FRAMERATE)


def main():
    # initialize pygame
    pygame.init()
    pygame.display.set_caption("Ciutats i Camins")
    pygame.display.set_icon(pygame.image.load("ciutats-i-camins.png"))
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()

    # create game
    game = Game()

    # create drawer that will draw the game on the screen
    drawer = Drawer(game, screen)

    # perform game loop
    loop(game, drawer, screen, clock)

    # finalize pygame
    pygame.quit()


# main script
if __name__ == "__main__":
    main()
