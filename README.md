# Bot Telegram Drive com Fly.io

Este bot faz postagens automáticas no Telegram usando imagens de uma pasta no Google Drive.

## Como usar no Fly.io

1. Instale o CLI do Fly.io: https://fly.io/docs/hands-on/install-flyctl/
2. Execute `fly launch` na pasta do projeto.
3. Configure as variáveis de ambiente usando `fly secrets set`:

- TOKEN
- CANAL_ID
- YUAN_PARA_REAL
- YUAN_PARA_EURO
- DRIVE_FOLDER_ID
- GOOGLE_APPLICATION_CREDENTIALS_JSON (insira o JSON inteiro da chave do Google Drive)

4. Deploy com `fly deploy`.

## Observação

Este projeto usa Docker, portanto ignora limitações de versão de Python no servidor.
