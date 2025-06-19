# Bot Telegram Drive com Fly.io (Worker)

Este bot faz postagens automáticas no Telegram usando imagens de uma pasta no Google Drive.

## Variáveis necessárias (Secrets no Fly.io)

- `TOKEN` → Token do bot Telegram
- `CANAL_ID` → ID do canal (ex.: -100xxxxxx)
- `DRIVE_FOLDER_ID` → ID da pasta do Google Drive
- `GOOGLE_APPLICATION_CREDENTIALS_JSON` → JSON da service account do Google

## Deploy

1. Instale o CLI do Fly.io:
https://fly.io/docs/hands-on/install-flyctl/

2. Execute:
```bash
fly launch
```

3. Configure os secrets:
```bash
fly secrets set TOKEN="seu_token" CANAL_ID="-100xxxxxx" DRIVE_FOLDER_ID="seu_id" GOOGLE_APPLICATION_CREDENTIALS_JSON='{"type":"service_account",...}'
```

4. Deploy:
```bash
fly deploy
```

✅ Pronto, funcionando 24h como Worker.