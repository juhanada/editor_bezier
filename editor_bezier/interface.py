import pygame


class Botao:
    def __init__(self, x, y, largura, altura, texto, cor_fundo, cor_texto, acao):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.cor_fundo = cor_fundo
        self.cor_texto = cor_texto
        self.acao = acao
        self.fonte = pygame.font.Font(None, 30)

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor_fundo, self.rect)
        texto_renderizado = self.fonte.render(self.texto, True, self.cor_texto)
        texto_rect = texto_renderizado.get_rect(center=self.rect.center)
        tela.blit(texto_renderizado, texto_rect)

    def verificar_clique(self, pos):
        return self.rect.collidepoint(pos)

    def executar_acao(self):
        if self.acao:
            self.acao()


class Interface:
    def __init__(self, tela, largura_tela, altura_tela):
        self.tela = tela
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.largura_area_desenho = int(largura_tela * 0.60)
        self.cor_fundo = (30, 30, 30)
        self.cor_area_desenho = (50, 50, 50)
        self.cor_area_controle = (20, 20, 20)
        self.fonte = pygame.font.Font(None, 36)

        # Lista de botões
        self.botoes = []

    def adicionar_botao(self, botao):
        self.botoes.append(botao)

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
        self.render_text("Ações", self.largura_area_desenho + 20, 20)

        # Desenhar botões
        for botao in self.botoes:
            botao.desenhar(self.tela)

    def render_text(self, texto, x, y, cor=(200, 200, 200)):
        texto_renderizado = self.fonte.render(texto, True, cor)
        self.tela.blit(texto_renderizado, (x, y))
