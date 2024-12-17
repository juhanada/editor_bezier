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

    def alternar_modo_remover():
        editor.modo_remover = not editor.modo_remover
        if editor.modo_remover:
            botao_remover.atualizar(texto="Modo Remoção ON", cor_fundo=(200, 50, 50))
        else:
            botao_remover.atualizar(texto="Remover Ponto", cor_fundo=(50, 150, 200))

    def alternar_modo_mover():
        editor.modo_mover = not editor.modo_mover
        if editor.modo_mover:
            botao_mover.atualizar(texto="Modo Mover ON", cor_fundo=(50, 200, 50))
            editor.modo_remover = False  # Desativa o modo de remoção, se necessário
            botao_remover.atualizar(texto="Remover Ponto", cor_fundo=(50, 150, 200))
        else:
            botao_mover.atualizar(texto="Mover Ponto", cor_fundo=(50, 150, 200))

    # Criar botões
    botao_limpar = Botao(
        560, 100, 200, 40, "Limpar", (200, 50, 50), (255, 255, 255), limpar_pontos
    )
    botao_remover = Botao(
        560,
        160,
        200,
        40,
        "Remover Ponto",
        (50, 150, 200),
        (255, 255, 255),
        alternar_modo_remover,
    )
    botao_mover = Botao(
        560,
        220,
        200,
        40,
        "Mover Ponto",
        (50, 150, 200),
        (255, 255, 255),
        alternar_modo_mover,
    )
    # Adicionar botão para alternar a visibilidade do polígono
    botao_alternar_poligono = Botao(
        560,
        280,
        200,
        40,
        texto="Ocultar Polígono",
        cor_fundo=(0, 100, 200),
        cor_texto=(255, 255, 255),
        acao=lambda: editor.alternar_poligono(botao_alternar_poligono),
    )

    interface.adicionar_botao(botao_limpar)
    interface.adicionar_botao(botao_remover)
    interface.adicionar_botao(botao_mover)
    interface.adicionar_botao(botao_alternar_poligono)

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
