#!/bin/sh
# O cron não herda as variáveis do container, então gravamos num arquivo
echo "export FILE_URL=\"$FILE_URL\"" > /app/env.sh

# Download imediato, para o app já ter o que mostrar
/app/download.sh || echo "Falha no download inicial"

exec cron -f