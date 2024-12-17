import pygame
from interface import Interface, Botao
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

    # Funções para botões
    def limpar_pontos():
        editor.pontos_controle.clear()

    def habilitar_remover_ponto():
        editor.modo_remover = not editor.modo_remover

    # Criar botões
    botao_limpar = Botao(
        620, 100, 150, 40, "Limpar", (200, 50, 50), (255, 255, 255), limpar_pontos
    )
    botao_remover = Botao(
        620,
        160,
        150,
        40,
        "Remover Ponto",
        (50, 150, 200),
        (255, 255, 255),
        habilitar_remover_ponto,
    )

    interface.adicionar_botao(botao_limpar)
    interface.adicionar_botao(botao_remover)

    rodando = True
    while rodando:
        # Capturar e tratar eventos
        rodando = handle_events(editor, interface)

        # Atualizar e renderizar
        interface.render()
        editor.render_curve()

        # Atualizar display
        pygame.display.flip()
        clock.tick(60)  # Limitar FPS

    pygame.quit()


if __name__ == "__main__":
    main()
