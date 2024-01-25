def verify_container(container: DockerClient, response_text: str) -> None:
    response = requests.get("http://127.0.0.1:8000")
    data = response.json()
    assert data["message"] == response_text
    config_data = get_config(container)
    assert config_data["workers_per_core"] == 1
    assert config_data["use_max_workers"] is None
    assert config_data["host"] == "0.0.0.0"
    assert config_data["port"] == "80"
    assert config_data["loglevel"] == "info"
    assert config_data["workers"] >= 2
    assert config_data["bind"] == "0.0.0.0:80"
    assert config_data["graceful_timeout"] == 120
    assert config_data["timeout"] == 120
    assert config_data["keepalive"] == 5
    assert config_data["errorlog"] == "-"
    assert config_data["accesslog"] == "-"
    logs = get_logs(container)
    assert "Checking for script in /app/prestart.sh" in logs
    assert "Running script /app/prestart.sh" in logs
    assert (
        "Running inside /app/prestart.sh, you could add migrations to this file" in logs
    )
    assert '"GET / HTTP/1.1" 200' in logs
    assert "[INFO] Application startup complete." in logs
    assert "Using worker: uvicorn.workers.UvicornWorker" in logs