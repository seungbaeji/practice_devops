# Loki Cloud

## 1. Logging Example

### 1-1. Run Promtail via Docker

```bash
docker run --name promtail \
    --volume "$PWD/promtail:/etc/promtail" \
    --volume "$PWD/tmp:/var/log" \
    grafana/promtail:latest \
    -config.file=/etc/promtail/config.yaml
```

### 1-2. Run Promtail using Windows application

```bash
.\promtail\promtail-windows-amd64.exe --config.file=.\promtail\config.yaml
```

## 2. Log Normalization Example

### 2-1. Run Promtail via Docker

```bash
docker run --name norm-promtail \
    --volume "$PWD/promtail:/etc/promtail" \
    --volume "$PWD/unstructured_log:/var/log" \
    grafana/promtail:latest \
    -config.file=/etc/promtail/norm-config-local.yaml
```

### 2-2. Run Promtail using Windows application

```bash
.\promtail\promtail-windows-amd64.exe --config.file=.\promtail\norm-config.yaml
```
