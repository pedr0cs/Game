# Game

Projeto pessoal de um jogo no estilo **Vampire Survivors** com elementos de RPG, desenvolvido em Python (backend) e HTML(frontend).

## Sobre o projeto

Um jogo web onde o jogador escolhe uma classe de RPG (mago, guerreiro, ninja, paladino, atirador) e enfrenta ondas de inimigos em uma arena. O foco é no gameplay core (sobrevivência + upgrades), com uma história opcional planejada para versões futuras.

## Roadmap

- [x] **Fase 1** — Protótipo em terminal: classes Player e Enemy, inimigo se move e é derrotado
- [x] **Fase 2** — Boneco se movendo na tela (Flask + Canvas + teclado)
- [x] **Fase 3** — Inimigos no frontend
- [x] **Fase 4** — Sistema de dano e morte
- [ ] **Fase 5** — Classes de RPG e upgrades
- [ ] **Fase 6** — Modo história (opcional)

## Tecnologias

- Python 3.14
- Flask (backend/API)
- HTML + Canvas API (frontend)
- JavaScript (movimento, game loop)

## Como rodar

```bash
# Clone o repositório
git clone https://github.com/pedr0cs/Game.git
cd Game

# Crie e ative o ambiente virtual
uv venv
.venv\Scripts\activate  # Windows

# Instale as dependências
pip install flask

# Rode o servidor
python backend/app.py
```

Acesse `http://localhost:5000` no navegador