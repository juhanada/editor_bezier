import pygame


def handle_events(editor):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Botão esquerdo
                x, y = evento.pos
                if x < editor.interface.largura_area_desenho:
                    editor.adicionar_ponto(x, y)
            elif evento.button == 3:  # Botão direito
                x, y = evento.pos
                editor.remover_ponto(x, y)
    return True
