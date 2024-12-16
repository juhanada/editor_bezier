# Trabalho Final - Editor de Curvas de Bezier

Atividade solicitada como avaliação parcial da disciplina de Introdução à Computação Gráfica do semestre 2024/2 do curso de Ciência da Computação da Universidade Federal do Amazonas (UFAM).

## Autoras

- Maria Gabriela Morais de Sá - 22250537 - maria.morais@icomp.ufam.edu.br
- Maria Giovanna Gonçalves Sales - 22251138 - maria.sales@icomp.ufam.edu.br
- Juíle Yoshie Sarkis Hanada - 22251135 - juile.hanada@icomp.ufam.edu.br

## Apresentação

Este projeto é um editor interativo de curvas de Bézier desenvolvido em Python utilizando a biblioteca **Pygame**. Ele permite criar, editar e visualizar curvas de Bézier de forma interativa, com uma interface amigável e responsiva.

### Funcionalidades

- **Adição de pontos de controle**: Permite ao usuário clicar em uma área interativa para adicionar novos pontos de controle.
- **Movimentação de pontos**: Possibilita arrastar pontos de controle com o mouse para ajustar a curva.
- **Exibição dos pontos de controle**: Os pontos são representados como pequenos círculos na interface.
- **Exibição do Polígono de controle**: Conexão dos pontos de controle com segmentos de linha.
- **Renderização da curva**: A curva é desenhada com suavidade, utilizando interpolção baseada no algoritmo de De Casteljau.
- **Seleção e remoção de pontos**: Permite excluir pontos de controle selecionados.
- **Detalhes sobre dos pontos**: Exibição das coordenadas dos pontos de controle na interface.
- **Opção de redefinição**: Botão ou tecla para limpar todos os pontos e reiniciar a curva.
- **Atualização em tempo real**: A curva é automaticamente atualizada após qualquer alteração nos pontos de controle.

## Pré-requisitos

- Python 3.11.0
- Poetry 1.8.4 (para gerenciamento de dependências)
- Pygame

## Execução

### Usando Poetry

1. **Clone este repositório:**
   ```bash
   git clone git@github.com:juhanada/editor_bezier.git
   cd editor_bezier
   ```
2. **Instale as dependências:**
   ```bash
   poetry install
   ```
3. **Ative o ambiente virtual:**
   ```bash
   poetry shell
   ```
4. **Execute o programa:**
   ```bash
   python editor_bezier/main.py
   ```

### Sem Poetry (usando pip)

1. **Instale o Pygame diretamente:**
   ```bash
   pip install pygame
   ```
2. **Execute o programa:**
   ```bash
   python editor_bezier/main.py
   ```

## Estrutura do Projeto

```
editor_bezier/
├── editor_bezier/
│   ├── __init__.py
│   └── main.py        # Arquivo principal com a lógica do editor
├── tests/             # Arquivos de testes futuros
├── pyproject.toml     # Configuração do projeto para Poetry
└── README.md          # Este arquivo
```

## Como usar o editor

1. **Adicionar pontos de controle:** Clique em qualquer lugar da tela para adicionar um novo ponto.
2. **Mover pontos:** Clique e arraste um ponto existente.
3. **Remover pontos:** Selecione um ponto e use a tecla correspondente para removê-lo.
4. **Limpar pontos:** Use o botão ou comando para limpar todos os pontos.
5. **Ajustar suavidade:** Configure o número de segmentos na interface para melhorar a renderização da curva.
