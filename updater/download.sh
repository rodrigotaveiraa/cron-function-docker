#!/bin/sh
set -e
. /app/env.sh

echo "[$(date '+%F %T')] Baixando $FILE_URL"
curl -fsSL "$FILE_URL" -o /data/arquivo.txt.tmp

# Troca atômica: o app nunca lê um arquivo pela metade
mv /data/arquivo.txt.tmp /data/arquivo.txt
echo "[$(date '+%F %T')] arquivo.txt atualizado"