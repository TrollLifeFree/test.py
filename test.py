import random
import pygame
import copy
import random as rd


class Cube:
    reverse_direction = 1

    def __init__(self, point, color):
        self.point = copy.deepcopy(point)
        self.color = color

    def set_height(self, height):
        for i in range(7):
            new_cube.point[i][1] -= height

    def set_point(self, cube, direction):
        if ((self.point[2][0] < cube.point[1][0] and self.point[3][0] < cube.point[0][0]) and (
                self.point[2][1] + 50 > cube.point[1][1] and self.point[3][1] + 50 > cube.point[0][1])) or \
                ((self.point[0][0] > cube.point[3][0] and self.point[1][0] > cube.point[2][0]) and (
                        self.point[0][1] + 50 < cube.point[3][1] and self.point[1][1] + 50 < cube.point[2][1])) or \
                ((self.point[2][0] < cube.point[3][0] and self.point[1][0] < cube.point[0][0]) and (
                        self.point[2][1] + 50 < cube.point[3][1] and self.point[1][1] + 50 < cube.point[0][1])) or \
                ((self.point[0][0] > cube.point[1][0] and self.point[3][0] > cube.point[2][0]) and (
                        self.point[0][1] + 50 > cube.point[1][1] and self.point[3][1] + 50 > cube.point[2][1])):
            return False
        elif (self.point[0][0] < cube.point[0][0] and self.point[1][0] < cube.point[1][0]) and (
                self.point[0][1] + 50 > cube.point[0][1] and self.point[1][1] + 50 > cube.point[1][
            1]) and direction == 1:
            self.point[4] = copy.deepcopy(cube.point[0])
            self.point[5] = copy.deepcopy(cube.point[1])
            self.point[0] = copy.deepcopy(cube.point[0])
            self.point[0][1] -= 50
            self.point[1] = copy.deepcopy(cube.point[1])
            self.point[1][1] -= 50
        elif (self.point[3][0] > cube.point[3][0] and self.point[2][0] > cube.point[2][0]) and (
                self.point[3][1] + 50 < cube.point[3][1] and self.point[3][1] + 50 < cube.point[3][
            1]) and direction == 1:
            self.point[6] = copy.deepcopy(cube.point[2])
            self.point[3] = copy.deepcopy(cube.point[3])
            self.point[3][1] -= 50
            self.point[2] = copy.deepcopy(cube.point[2])
            self.point[2][1] -= 50
        elif (self.point[0][0] < cube.point[0][0] and self.point[3][0] < cube.point[3][0]) and (
                self.point[0][1] + 50 < cube.point[0][1] and self.point[3][1] + 50 < cube.point[3][
            1]) and direction == 0:
            self.point[4] = copy.deepcopy(cube.point[0])
            self.point[0] = copy.deepcopy(cube.point[0])
            self.point[0][1] -= 50
            self.point[3] = copy.deepcopy(cube.point[3])
            self.point[3][1] -= 50
        elif (self.point[1][0] > cube.point[1][0] and self.point[2][0] > cube.point[2][0]) and (
                self.point[1][1] + 50 > cube.point[1][1] and self.point[2][1] + 50 > cube.point[2][
            1]) and direction == 0:
            self.point[5] = copy.deepcopy(cube.point[1])
            self.point[6] = copy.deepcopy(cube.point[2])
            self.point[1] = copy.deepcopy(cube.point[1])
            self.point[1][1] -= 50
            self.point[2] = copy.deepcopy(cube.point[2])
            self.point[2][1] -= 50
        return True

    def move_cube(self, cube, direction):
        move_speed = 2
        if self.point[3][0] > cube.point[2][0] * 1.3 and Cube.reverse_direction == 1:
            Cube.reverse_direction = -1
        elif self.point[2][0] * 1.3 < cube.point[3][0] and Cube.reverse_direction == -1:
            Cube.reverse_direction = 1

        if direction == 0:
            for i in range(7):
                self.point[i][0] += Cube.reverse_direction * move_speed
                self.point[i][1] += Cube.reverse_direction * move_speed / 3
        elif direction == 1:
            for i in range(7):
                self.point[i][0] += Cube.reverse_direction * move_speed
                self.point[i][1] -= Cube.reverse_direction * move_speed / 3


def draw_cube(cube):
    # 위 사각형 (p1, p2, p3, p4)
    point = cube.point
    color = cube.color
    pygame.draw.polygon(screen, color,
                        [point[0], point[1], point[2], point[3]], 0)
    # 아래 오각형 (p3, p1, p5, p6, p7)
    pygame.draw.polygon(screen, color,
                        [point[2], point[0], point[4], point[5], point[6]], 0)
    # p1 p2 직선
    pygame.draw.line(screen, color_black, point[0], point[1], 2)
    # p1 p4 직선
    pygame.draw.line(screen, color_black, point[0], point[3], 2)
    # p2 p3 직선
    pygame.draw.line(screen, color_black, point[1], point[2], 2)
    # p3 p4 직선
    pygame.draw.line(screen, color_black, point[2], point[3], 2)
    # p1 p5 직선
    pygame.draw.line(screen, color_black, point[0], point[4], 2)
    # p5 p6 직선
    pygame.draw.line(screen, color_black, point[4], point[5], 2)
    # p2 p6 직선
    pygame.draw.line(screen, color_black, point[1], point[5], 2)
    # p6 p7 직선
    pygame.draw.line(screen, color_black, point[5], point[6], 2)
    # p3 p7 직선
    pygame.draw.line(screen, color_black, point[2], point[6], 2)


def scroll_map(cube_list):
    for i in range(len(cube_list)):
        for j in range(7):
            cube_list[i].point[j][1] += 30

def draw_score():
    score = pygame.font.SysFont('Ariel',40)
    text_score = score.render("Score : " + str(len(cube_list) - 1), True, color_white)
    screen.blit(text_score,[20,20])

def draw_mesaage():
    gameover = pygame.font.SysFont('Ariel', 100)
    text_gameover = gameover.render("GAME OVER", True, (255,0,0))
    screen.blit(text_gameover,[100,300])

pygame.init()

size = [640, 1000]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Stack Game")

play = True

point0 = [[20, 850], [320, 950], [620, 850], [320, 750], [20, 900], [320, 1000], [620, 900]]

zero_cube_color = (rd.randint(128, 255), rd.randint(128, 255), rd.randint(128, 255))
background_color = (rd.randint(0, 12), rd.randint(0, 127), rd.randint(0, 127))
cube_color = (rd.randint(128, 255), rd.randint(128, 255), rd.randint(128, 255))
color_black = (0, 0, 0)
color_white = (255, 255, 255)

cube_list = list()

zero_cube = Cube(point0, zero_cube_color)
cube_list.append(zero_cube)

new_cube = Cube(cube_list[len(cube_list) - 1].point, cube_color)
new_cube.set_height(50)

clock = pygame.time.get_ticks()
direction = 0

while play:
    # screen.blit(screen, screen_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            play = new_cube.set_point(cube_list[len(cube_list) - 1], direction)
            cube_list.append(new_cube)
            scroll_map(cube_list)
            cube_color = (rd.randint(128, 255), rd.randint(128, 255), rd.randint(128, 255))
            background_color = (rd.randint(0, 12), rd.randint(0, 127), rd.randint(0, 127))
            if play:
                new_cube = Cube(cube_list[len(cube_list) - 1].point, cube_color)
                new_cube.set_height(50)
            direction = random.randint(0, 1)

    screen.fill(background_color)
    # 큐브리스트 큐브 그리기
    for cube_data in cube_list:
        draw_cube(cube_data)
    draw_score()
    new_cube.move_cube(cube_list[len(cube_list) - 1], direction)
    draw_cube(new_cube)
    pygame.display.update()

draw_mesaage()
pygame.display.update()
pygame.time.delay(3000)

pygame.quit()
