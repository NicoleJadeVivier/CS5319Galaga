import pygame


class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.model.player.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    self.model.player.moving_right = True
                elif event.key == pygame.K_SPACE:
                    self.model.shoot()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.model.player.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    self.model.player.moving_right = False
            elif event.type == pygame.MOUSEBUTTONDOWN and self.model.game_over:
                if self.view.is_over_button(event.pos):
                    self.reset_game()

    def reset_game(self):
        # Reset the game model to its initial state
        self.model.__init__()