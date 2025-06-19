# Bot Telegram Drive com Fly.io

Este bot faz postagens automáticas no Telegram rodando no Fly.io como Background Worker.

## 🚀 Como usar:

1. Instale o CLI do Fly.io: https://fly.io/docs/hands-on/install-flyctl/
2. Execute `fly launch` na pasta do projeto.
3. Configure os secrets:

```
fly secrets set TOKEN="seu-token" CANAL_ID="@seucanal"
```

4. Deploy:

```
fly deploy
```

Pronto! O bot estará rodando no Fly.io como worker, sem precisar de portas ou servidores web.