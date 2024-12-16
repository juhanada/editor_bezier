import pygame


class Interface:
    def __init__(self, tela, largura_tela, altura_tela):
        self.tela = tela
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.largura_area_desenho = int(largura_tela * 0.75)
        self.cor_fundo = (30, 30, 30)
        self.cor_area_desenho = (50, 50, 50)
        self.cor_area_controle = (20, 20, 20)
        self.fonte = pygame.font.Font(None, 36)

    def render(self):
        # Desenhar áreas
        self.tela.fill(self.cor_fundo)
        pygame.draw.rect(
            self.tela,
            self.cor_area_desenho,
            (0, 0, self.largura_area_desenho, self.altura_tela),
        )
        pygame.draw.rect(
            self.tela,
            self.cor_area_controle,
            (
                self.largura_area_desenho,
                0,
                self.largura_tela - self.largura_area_desenho,
                self.altura_tela,
            ),
        )

        # Renderizar textos básicos
        self.render_text("Informações e Ações", self.largura_area_desenho + 20, 20)

    def render_text(self, texto, x, y, cor=(200, 200, 200)):
        texto_renderizado = self.fonte.render(texto, True, cor)
        self.tela.blit(texto_renderizado, (x, y))
