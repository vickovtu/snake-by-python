import pygame
from control import Control
from snake import Snake
from gui import Gui
from food import Food

gui = food = window = var_speed = control = snake = None


def start_game():
    global gui, food, window, var_speed, control, snake
    pygame.init()
    # создаем игровое окно
    window = pygame.display.set_mode((441, 441))
    # создаем название окна
    pygame.display.set_caption("Snake by Gamb")

    # создаем экземпляр контроля
    control = Control()
    # создаем экземпляр змеи
    snake = Snake()
    gui = Gui()
    food = Food()
    var_speed = 0
    # gui.create_image()
    gui.init_field()
    food.get_food_position(gui)


start_game()

while control.flag_game:

    gui.check_win_or_lose()
    control.control()
    # каждый раз закрашиваем полотно окна
    window.fill(pygame.Color("Black"))
    if gui.game == "game":
        # отрисовываем змейку
        snake.draw_snake(window)
        food.draw_food(window)
    elif gui.game == "win":
        gui.draw_win(window)
    elif gui.game == "lose":
        gui.draw_lose(window)
    gui.draw_indicator(window)
    # отрисовываем уровень
    gui.draw_level(window)
    if var_speed % 10 == 0 and control.flag_pause and gui.game == 'game':
        snake.move(control)
        snake.check_barrier(gui)
        snake.eat(food, gui)
        snake.check_end_window()
        snake.animation()
    var_speed += 1
    if control.flag_restart:
        start_game()
    # отображение окна
    pygame.display.flip()
