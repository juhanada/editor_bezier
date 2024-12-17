import pygame


class CurveEditor:
    def __init__(self, interface):
        self.interface = interface
        self.pontos_controle = []
        self.modo_remover = False
        self.modo_mover = False
        self.ponto_selecionado = None  # Armazena o índice do ponto sendo movido
        self.mostrar_poligono = True  # Controla a visibilidade do polígono de controle
        self.cor_curva = (255, 255, 0)
        self.cor_pontos = (255, 0, 0)
        self.cor_linhas = (100, 100, 100)

    def adicionar_ponto(self, x, y):
        self.pontos_controle.append((x, y))

    def remover_ponto(self, posicao):
        for ponto in self.pontos_controle:
            if (posicao[0] - ponto[0]) ** 2 + (posicao[1] - ponto[1]) ** 2 <= 100:
                self.pontos_controle.remove(ponto)
                break

    def selecionar_ponto(self, posicao):
        """Seleciona um ponto próximo para movimentação."""
        for i, ponto in enumerate(self.pontos_controle):
            if (posicao[0] - ponto[0]) ** 2 + (posicao[1] - ponto[1]) ** 2 <= 100:
                self.ponto_selecionado = i
                return

    def mover_ponto(self, posicao):
        """Move o ponto selecionado para a nova posição."""
        if self.ponto_selecionado is not None:
            self.pontos_controle[self.ponto_selecionado] = posicao

    def liberar_ponto(self):
        """Libera o ponto após o movimento."""
        self.ponto_selecionado = None

    def alternar_poligono(self, botao=None):
        """Alterna a visibilidade do polígono de controle e atualiza o texto do botão."""
        self.mostrar_poligono = not self.mostrar_poligono
        if botao:
            novo_texto = (
                "Mostrar Polígono" if not self.mostrar_poligono else "Ocultar Polígono"
            )
            botao.texto = novo_texto

    def render_curve(self):
        tela = self.interface.tela

        # Desenhar pontos de controle
        for ponto in self.pontos_controle:
            pygame.draw.circle(tela, self.cor_pontos, ponto, 5)

        # Desenhar linhas de controle
        if self.mostrar_poligono and len(self.pontos_controle) > 1:
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
