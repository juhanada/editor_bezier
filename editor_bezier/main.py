import pygame
import sys


def main():
    # Inicializa o Pygame
    pygame.init()

    # Configurações da janela
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Editor de Curvas de Bézier")

    # Cores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Loop principal
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Preenche o fundo
        screen.fill(WHITE)

        # Atualiza a tela
        pygame.display.flip()

    # Finaliza o Pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
