# Load Testing with Locust and HTTPBin

## Project description

This project demonstrates automated load testing and basic resilience
analysis using Locust. A ready-made HTTPBin service runs locally in Docker,
so no custom web application is required.

The demonstration includes:
- a baseline load test;
- a heavier stress test;
- slow responses;
- an intentional HTTP 500 error scenario.

## Requirements

- Docker Desktop
- Python
- Locust
- Git

## Project files

- `locustfile.py` — Locust user behaviour and test tasks
- `README.md` — installation and launch instructions
- `results/` — screenshots and test results
- `report/` — technical report materials

## Step 1: Start HTTPBin

Run the following command:

```bash
docker run --rm -p 8080:8080 mccutchen/go-httpbin