import pygame


def handle_events(editor, interface):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Botão esquerdo
                pos = evento.pos

                # Verificar cliques nos botões
                for botao in interface.botoes:
                    if botao.verificar_clique(pos):
                        botao.executar_acao()
                        return True

                # Adicionar ou remover ponto
                if pos[0] < editor.interface.largura_area_desenho:
                    if editor.modo_remover:
                        editor.remover_ponto(pos[0], pos[1])
                    else:
                        editor.adicionar_ponto(pos[0], pos[1])

    return True
