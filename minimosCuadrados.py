import pygame

clock = pygame.time.Clock()

ANCHO_PANTALLA = 1200
ALTO_PANTALLA = 800

pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

White = (255, 255, 255)
Red = (169, 19, 38)
Black = (0, 0, 0)
Green = (8, 101, 55)
Silver = (192, 192, 192)
Gold = (255, 188, 0)
Grey = (100, 100, 100)
Yellow = (255, 255, 0)


class Calculate:
    def sumX(self, x):
        total = 0
        for num in x:
            total += num
        return total

    def sumY(self, y):
        total = 0
        for num in y:
            total += num
        return total

    def mult(self, x, y):
        total = 0
        for i in range(len(x)):
            total += x[i] * y[i]
        return total

    def powe(self, x):
        total = 0
        for num in x:
            total += num ** 2
        return total


class Calcula(object):
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 40)
        self.render = self.font.render('Calculate', True, Black, White)
        self.rect = self.render.get_rect()
        self.rect.x = ANCHO_PANTALLA - self.render.get_rect()[2] - 25
        self.rect.bottom = ALTO_PANTALLA - 25


class Delete(object):
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 40)
        self.render = self.font.render('Delete', True, Black, White)
        self.rect = self.render.get_rect()
        self.rect.x = 25
        self.rect.bottom = ALTO_PANTALLA - 25


class Tabla(object):
    def __init__(self):
        pygame.init()
        self.pantalla, self.rect = self.screen()
        self.calcula = Calcula()
        self.delete = Delete()
        self.calculate = Calculate()

    def screen(self):
        pygame.display.set_caption('Minimos Cuadrados')
        rect = pantalla.get_rect()
        pantalla.convert()

        return pantalla, rect

    def actualizaCalcula(self):
        self.calcula.render = self.calcula.font.render('Calculate', True, Black, White)
        self.calcula.rect = self.calcula.render.get_rect()
        self.calcula.rect.x = ANCHO_PANTALLA - self.calcula.render.get_rect()[2] - 25
        self.calcula.rect.bottom = ALTO_PANTALLA - 25

    def actualizaDelete(self):
        self.delete.render = self.delete.font.render('Delete', True, Black, White)
        self.delete.rect = self.delete.render.get_rect()
        self.delete.rect.x = 25
        self.delete.rect.bottom = ALTO_PANTALLA - 25

    def bucle(self):
        points = []
        Y1 = -5
        Y2 = -5
        while True:
            for event in pygame.event.get():  # detecta clicks y teclas
                if event.type == pygame.QUIT:  # detecta solo cuando haces click en cerrar la ventana
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if 100 < pos[0] < ANCHO_PANTALLA - 100 and 100 < pos[1] < ALTO_PANTALLA - 100:
                        points.append(pos)
                        Y1 = -5
                        Y2 = -5

                    elif 1028 < pos[0] < ANCHO_PANTALLA - 25 and ALTO_PANTALLA - 25 - 48 < pos[1] < ALTO_PANTALLA - 25:
                        if not points:
                            print('error')

                        else:
                            arrayX = []
                            arrayY = []
                            for x in points:
                                arrayX.append(x[0])
                                arrayY.append(x[1])
                            xTotal = self.calculate.sumX(arrayX)
                            yTotal = self.calculate.sumY(arrayY)
                            xy = self.calculate.mult(arrayX, arrayY)
                            x2 = self.calculate.powe(arrayX)
                            print('Σx = ' + str(xTotal) + ', Σy = ' + str(yTotal) + ', Σxy = ' + str(
                                xy) + ', Σx2 = ' + str(x2))
                            pendiente = (xy - ((xTotal * yTotal) / len(arrayX))) / (
                                        x2 - ((xTotal * xTotal) / len(arrayX)))
                            intercepcionY = (yTotal / len(arrayX)) - pendiente * (xTotal / len(arrayX))
                            print('ecuation: Y = ' + str(intercepcionY) + ' * X + ' + str(pendiente))

                            Y1 = (pendiente * 101) + intercepcionY
                            Y2 = (pendiente * 1100) + intercepcionY

                    elif 25 < pos[0] < 25 + 133 and ALTO_PANTALLA - 25 - 48 < pos[1] < ALTO_PANTALLA - 25:
                        if not points:
                            print('error')

                        else:
                            del points[-1]
                            Y1 = -5
                            Y2 = -5

            pantalla.fill(White)
            pygame.draw.line(pantalla, Black, (100, ALTO_PANTALLA - 100), (ANCHO_PANTALLA - 100, ALTO_PANTALLA - 100),
                             4)
            pygame.draw.line(pantalla, Black, (100, ALTO_PANTALLA - 100), (100, 100), 4)
            pygame.draw.line(pantalla, Black, (101, int(Y1)), (1100, int(Y2)), 4)

            pantalla.blit(self.calcula.render, self.calcula.rect)
            self.actualizaCalcula()

            pantalla.blit(self.delete.render, self.delete.rect)
            self.actualizaDelete()

            for point in points:
                pygame.draw.circle(pantalla, Black, point, 3, 0)
            pygame.display.update()
            clock.tick(60)


if __name__ == '__main__':
    tabla = Tabla()
    tabla.bucle()
