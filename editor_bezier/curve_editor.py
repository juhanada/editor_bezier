import pygame


class CurveEditor:
    def __init__(self, interface):
        self.interface = interface
        self.pontos_controle = []
        self.modo_remover = False  # Novo atributo
        self.cor_curva = (255, 255, 0)
        self.cor_pontos = (255, 0, 0)
        self.cor_linhas = (100, 100, 100)

    def adicionar_ponto(self, x, y):
        self.pontos_controle.append((x, y))

    def remover_ponto(self, x, y):
        for ponto in self.pontos_controle:
            if abs(ponto[0] - x) < 10 and abs(ponto[1] - y) < 10:
                self.pontos_controle.remove(ponto)
                break

    def render_curve(self):
        tela = self.interface.tela
        # Desenhar pontos de controle
        for ponto in self.pontos_controle:
            pygame.draw.circle(tela, self.cor_pontos, ponto, 5)

        # Desenhar linhas de controle
        if len(self.pontos_controle) > 1:
            pygame.draw.lines(tela, self.cor_linhas, False, self.pontos_controle, 1)

        # Renderizar curva (usar algoritmo de De Casteljau ou interpolação)
        if len(self.pontos_controle) > 1:
            self.draw_bezier_curve(tela)

    def draw_bezier_curve(self, tela):
        # Implementação simples de uma curva de Bézier
        num_segmentos = 100
        if len(self.pontos_controle) < 2:
            return

        for t in range(num_segmentos + 1):
            t = t / num_segmentos
            ponto = self.calcular_ponto_bezier(t)
            pygame.draw.circle(tela, self.cor_curva, ponto, 2)

    def calcular_ponto_bezier(self, t):
        pontos = self.pontos_controle[:]
        while len(pontos) > 1:
            novos_pontos = []
            for i in range(len(pontos) - 1):
                x = (1 - t) * pontos[i][0] + t * pontos[i + 1][0]
                y = (1 - t) * pontos[i][1] + t * pontos[i + 1][1]
                novos_pontos.append((int(x), int(y)))
            pontos = novos_pontos
        return pontos[0]
