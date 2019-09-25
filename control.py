import pygame


class Control:

    def __init__(self):
        self.flag_game = True
        # создаем флаг направления
        self.flag_direction = "right".upper()
        self.flag_pause = True
        self.flag_restart = False

    def control(self):
        """ Управление в зависимости от флага """
        # pygame.event модуль принимает сигналы
        for event in pygame.event.get():
            # если нажали на крестик завершаем игру
            if event.type == pygame.QUIT:
                self.flag_game = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.flag_direction != "LEFT":
                    self.flag_direction = "right".upper()
                elif event.key == pygame.K_LEFT and self.flag_direction != "RIGHT":
                    self.flag_direction = "left".upper()
                elif event.key == pygame.K_UP and self.flag_direction != "DOWN":
                    self.flag_direction = "up".upper()
                elif event.key == pygame.K_DOWN and self.flag_direction != "UP":
                    self.flag_direction = "down".upper()
                elif event.key == pygame.K_ESCAPE:
                    self.flag_game = False
                elif event.key == pygame.K_SPACE:
                    self.flag_pause = not self.flag_pause
                elif event.key == pygame.K_r:
                    self.flag_restart = not self.flag_restart
