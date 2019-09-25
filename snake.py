import pygame


class Snake:

    def __init__(self):
        self.head = [45, 45]
        self.body = [[45, 45], [34, 45], [23, 45]]

    def move(self, control):
        """ Движение змейки в зависимости от направленич"""
        if control.flag_direction == "RIGHT":
            self.head[0] += 11
        elif control.flag_direction == "LEFT":
            self.head[0] -= 11
        elif control.flag_direction == "UP":
            self.head[1] -= 11
        elif control.flag_direction == "DOWN":
            self.head[1] += 11

    def animation(self):
        """ прибавляем в начало списка голову а хвост удаляем"""
        self.body.insert(0, list(self.head))
        self.body.pop()

    def draw_snake(self, window):
        """ Отрисовываем змейку на экране """
        for segment in self.body:
            pygame.draw.rect(window, pygame.Color("Green"), pygame.Rect(segment[0], segment[1], 10, 10))

    def check_end_window(self):
        """ отслеживает достижение змией края экрана """
        if self.head[0] == 419:
            self.head[0] = 23
        elif self.head[0] == 12:
            self.head[0] = 419
        elif self.head[1] == 23:
            self.head[1] = 419
        elif self.head[1] == 419:
            self.head[1] = 34

    def eat(self, food, gui):
        """змея ест еду"""
        if self.head == food.food_position:
            self.body.append(food.food_position)
            food.get_food_position(gui)
            gui.get_new_indicator()

    def check_barrier(self, gui):
        """проверяет не врезалась ли змея в препятствие"""
        if self.head in gui.barrier:
            self.body.pop()
            try:
                gui.indicator.pop()
            except:
                print("game over")
        if self.head in self.body[1:]:
            self.body.pop()
            try:
                gui.indicator.pop()
            except:
                print("game over")
