import pygame
from interface import Interface
from curve_editor import CurveEditor
from events import handle_events

# Configurações iniciais
LARGURA_TELA = 800
ALTURA_TELA = 600


def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Editor de Curvas de Bézier")
    clock = pygame.time.Clock()

    # Inicializar módulos
    interface = Interface(tela, LARGURA_TELA, ALTURA_TELA)
    editor = CurveEditor(interface)

    rodando = True
    while rodando:
        # Capturar e tratar eventos
        rodando = handle_events(editor)

        # Atualizar e renderizar
        interface.render()
        editor.render_curve()

        # Atualizar display
        pygame.display.flip()
        clock.tick(60)  # Limitar FPS

    pygame.quit()


if __name__ == "__main__":
    main()
