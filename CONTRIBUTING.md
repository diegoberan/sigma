# Contribuição

O repositório usa revisão manual antes de qualquer promoção para ambiente remoto.

## Fluxo

1. Crie uma branch de trabalho a partir de `main`.
2. Faça alterações pequenas e explique o objetivo no commit.
3. Abra um Pull Request para `main`.
4. Aguarde a revisão do responsável pelo projeto.
5. Só depois do merge aprovado o commit poderá ser considerado candidato a deploy.

O workflow de CI apenas executa testes e builds. Ele não acessa a VPS, não usa
chaves de deploy e não publica automaticamente nenhum ambiente.

## Comandos locais

```bash
uv sync
uv run python manage.py check
uv run pytest -q
uv run ruff check .
cd frontend && pnpm install --frozen-lockfile && pnpm build
```

Não commite `.env`, senhas, tokens, chaves SSH ou dados capturados do broker.
