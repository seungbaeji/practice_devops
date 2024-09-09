# Loki Cloud

## Run Promtail via Docker

```bash
docker run --name promtail \
    --volume "$PWD/promtail:/etc/promtail" \
    --volume "$PWD/tmp:/var/log" \
    grafana/promtail:latest \
    -config.file=/etc/promtail/config.yaml
```

## Run Promtail using Windows application

```bash
.\promtail\promtail-windows-amd64.exe --config.file=.\promtail\config.yaml
```