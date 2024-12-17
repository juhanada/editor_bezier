import pygame


def handle_events(editor, interface):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            # Primeiro, verifica se o clique foi em algum botão
            for botao in interface.botoes:
                if botao.is_hovered(pos):
                    interface.handle_event(event, pos)
                    return True  # Interrompe aqui para evitar que o editor também processe o clique

            # Se o clique não foi em um botão, processa no editor
            if editor.modo_remover:
                editor.remover_ponto(pos)
            elif editor.modo_mover:
                editor.selecionar_ponto(pos)
            else:
                editor.adicionar_ponto(pos[0], pos[1])

        elif event.type == pygame.MOUSEMOTION:
            if editor.modo_mover and editor.ponto_selecionado is not None:
                pos = pygame.mouse.get_pos()
                editor.mover_ponto(pos)

        elif event.type == pygame.MOUSEBUTTONUP:
            if editor.modo_mover:
                editor.liberar_ponto()

    return True
