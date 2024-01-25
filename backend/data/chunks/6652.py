def get_logs(container: DockerClient) -> str:
    logs = container.logs()
    return logs.decode("utf-8")