import sys

import pygame

FPS = 30
size = width, height = 500, 500
pygame.display.set_caption('Tic-tac-toe')
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def start_screen():
    font = pygame.font.Font(None, 100)
    string_rendered = font.render('Играть', 1, (255, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (125, 210, 250, 80), 2)
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 220
    intro_rect.left = 135
    screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 125 <= x <= 375 and 210 <= y <= 290:
                    return
        pygame.display.flip()
        clock.tick(FPS)


class Game:
    def __init__(self):
        self.units = {
            1: '',
            2: '',
            3: '',
            4: '',
            5: '',
            6: '',
            7: '',
            8: '',
            9: ''
        }
        self.start_unit = 'cross'  # cross or nought
        self.unit = self.start_unit
        self.win = ''

    def field_render(self):
        pygame.draw.rect(screen, (255, 255, 255), (170, 20, 5, 460), 5)
        pygame.draw.rect(screen, (255, 255, 255), (325, 20, 5, 460), 5)
        pygame.draw.rect(screen, (255, 255, 255), (20, 170, 460, 5), 5)
        pygame.draw.rect(screen, (255, 255, 255), (20, 325, 460, 5), 5)
        for pos, unit in self.units.items():
            if unit == 'cross':
                match pos:
                    case 1:
                        pygame.draw.line(screen, (254, 89, 194), (25, 25), (165, 165), 5)
                        pygame.draw.line(screen, (254, 89, 194), (25, 165), (165, 25), 5)
                    case 2:
                        pygame.draw.line(screen, (254, 89, 194), (180, 25), (320, 165), 5)
                        pygame.draw.line(screen, (254, 89, 194), (180, 165), (320, 25), 5)
                    case 3:
                        pygame.draw.line(screen, (254, 89, 194), (335, 25), (475, 165), 5)
                        pygame.draw.line(screen, (254, 89, 194), (335, 165), (475, 25), 5)
                    case 4:
                        pygame.draw.line(screen, (254, 89, 194), (25, 180), (165, 320), 5)
                        pygame.draw.line(screen, (254, 89, 194), (25, 320), (165, 180), 5)
                    case 5:
                        pygame.draw.line(screen, (254, 89, 194), (180, 180), (320, 320), 5)
                        pygame.draw.line(screen, (254, 89, 194), (180, 320), (320, 180), 5)
                    case 6:
                        pygame.draw.line(screen, (254, 89, 194), (335, 180), (475, 320), 5)
                        pygame.draw.line(screen, (254, 89, 194), (335, 320), (475, 180), 5)
                    case 7:
                        pygame.draw.line(screen, (254, 89, 194), (25, 335), (165, 475), 5)
                        pygame.draw.line(screen, (254, 89, 194), (25, 475), (165, 335), 5)
                    case 8:
                        pygame.draw.line(screen, (254, 89, 194), (180, 335), (320, 475), 5)
                        pygame.draw.line(screen, (254, 89, 194), (180, 475), (320, 335), 5)
                    case 9:
                        pygame.draw.line(screen, (254, 89, 194), (335, 335), (475, 475), 5)
                        pygame.draw.line(screen, (254, 89, 194), (335, 475), (475, 335), 5)
            elif unit == 'nought':
                match pos:
                    case 1:
                        pygame.draw.circle(screen, (85, 85, 255), (95, 95), 70, 5)
                    case 2:
                        pygame.draw.circle(screen, (85, 85, 255), (250, 95), 70, 5)
                    case 3:
                        pygame.draw.circle(screen, (85, 85, 255), (405, 95), 70, 5)
                    case 4:
                        pygame.draw.circle(screen, (85, 85, 255), (95, 250), 70, 5)
                    case 5:
                        pygame.draw.circle(screen, (85, 85, 255), (250, 250), 70, 5)
                    case 6:
                        pygame.draw.circle(screen, (85, 85, 255), (405, 250), 70, 5)
                    case 7:
                        pygame.draw.circle(screen, (85, 85, 255), (95, 405), 70, 5)
                    case 8:
                        pygame.draw.circle(screen, (85, 85, 255), (250, 405), 70, 5)
                    case 9:
                        pygame.draw.circle(screen, (85, 85, 255), (405, 405), 70, 5)

    def update_unit(self):
        if self.unit == 'cross':
            self.unit = 'nought'
        else:
            self.unit = 'cross'

    def victory(self):
        if (self.units[1] == 'cross' and self.units[2] == 'cross' and self.units[3] == 'cross') or \
                (self.units[4] == 'cross' and self.units[5] == 'cross' and self.units[6] == 'cross') or \
                (self.units[7] == 'cross' and self.units[8] == 'cross' and self.units[9] == 'cross') or \
                (self.units[1] == 'cross' and self.units[4] == 'cross' and self.units[7] == 'cross') or \
                (self.units[2] == 'cross' and self.units[5] == 'cross' and self.units[8] == 'cross') or \
                (self.units[3] == 'cross' and self.units[6] == 'cross' and self.units[9] == 'cross') or \
                (self.units[1] == 'cross' and self.units[5] == 'cross' and self.units[9] == 'cross') or \
                (self.units[3] == 'cross' and self.units[5] == 'cross' and self.units[7] == 'cross'):
            self.win = 'Победил игрок 1'
        elif (self.units[1] == 'nought' and self.units[2] == 'nought' and self.units[3] == 'nought') or \
                (self.units[4] == 'nought' and self.units[5] == 'nought' and self.units[6] == 'nought') or \
                (self.units[7] == 'nought' and self.units[8] == 'nought' and self.units[9] == 'nought') or \
                (self.units[1] == 'nought' and self.units[4] == 'nought' and self.units[7] == 'nought') or \
                (self.units[2] == 'nought' and self.units[5] == 'nought' and self.units[8] == 'nought') or \
                (self.units[3] == 'nought' and self.units[6] == 'nought' and self.units[9] == 'nought') or \
                (self.units[1] == 'nought' and self.units[5] == 'nought' and self.units[9] == 'nought') or \
                (self.units[3] == 'nought' and self.units[5] == 'nought' and self.units[7] == 'nought'):
            self.win = 'Победил игрок 2'
        elif self.units[1] != '' and self.units[2] != '' and self.units[3] != '' and \
                self.units[4] != '' and self.units[5] != '' and self.units[6] != '' and \
                self.units[7] != '' and self.units[8] != '' and self.units[9] != '':
            self.win = '          Ничья'
        if self.win != '':
            screen.fill((0, 0, 0))
            texts = [f'{self.win}', 'Сыграть ещё раз']
            font = pygame.font.Font(None, 70)
            text_cord = 50
            text_color = (57, 255, 20)
            for text in texts:
                string_rendered = font.render(text, 1, text_color)
                intro_rect = string_rendered.get_rect()
                intro_rect.top = text_cord
                intro_rect.left = 50
                screen.blit(string_rendered, intro_rect)
                text_cord += 200
                text_color = (188, 19, 254)
            pygame.draw.rect(screen, (188, 19, 254), (40, 245, 430, 60), 2)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = pygame.mouse.get_pos()
                        if 40 <= x <= 470 and 245 <= y <= 305:
                            self.units = {
                                1: '',
                                2: '',
                                3: '',
                                4: '',
                                5: '',
                                6: '',
                                7: '',
                                8: '',
                                9: ''
                            }
                            if self.start_unit == 'cross':
                                self.start_unit = 'nought'
                            else:
                                self.start_unit = 'cross'
                            self.unit = self.start_unit
                            self.win = ''
                            return
                pygame.display.flip()
                clock.tick(FPS)

    def update(self, x=0, y=0):
        self.field_render()
        if 20 <= x <= 170 and 20 <= y <= 170:
            if self.units[1] == '':
                self.units[1] = self.unit
                self.update_unit()
        elif 175 <= x <= 325 and 20 <= y <= 170:
            if self.units[2] == '':
                self.units[2] = self.unit
                self.update_unit()
        elif 330 <= x <= 480 and 20 <= y <= 170:
            if self.units[3] == '':
                self.units[3] = self.unit
                self.update_unit()
        elif 20 <= x <= 170 and 175 <= y <= 325:
            if self.units[4] == '':
                self.units[4] = self.unit
                self.update_unit()
        elif 175 <= x <= 325 and 175 <= y <= 325:
            if self.units[5] == '':
                self.units[5] = self.unit
                self.update_unit()
        elif 330 <= x <= 480 and 175 <= y <= 325:
            if self.units[6] == '':
                self.units[6] = self.unit
                self.update_unit()
        elif 20 <= x <= 170 and 330 <= y <= 480:
            if self.units[7] == '':
                self.units[7] = self.unit
                self.update_unit()
        elif 175 <= x <= 325 and 330 <= y <= 480:
            if self.units[8] == '':
                self.units[8] = self.unit
                self.update_unit()
        elif 330 <= x <= 480 and 330 <= y <= 480:
            if self.units[9] == '':
                self.units[9] = self.unit
                self.update_unit()
        self.victory()


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    pygame.init()
    start_screen()
    game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                game.update(x, y)
        screen.fill((0, 0, 0))
        game.update()
        pygame.display.update()
        clock.tick(FPS)
