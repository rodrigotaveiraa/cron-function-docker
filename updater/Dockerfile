FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
        cron curl ca-certificates tzdata \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY download.sh entrypoint.sh /app/
COPY crontab /etc/cron.d/github-update

RUN chmod +x /app/*.sh && chmod 0644 /etc/cron.d/github-update

ENTRYPOINT ["/app/entrypoint.sh"]