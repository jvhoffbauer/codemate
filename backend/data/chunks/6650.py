def get_config(container: Container) -> Dict[str, Any]:
    gunicorn_conf = get_gunicorn_conf_path(container)
    result = container.exec_run(f"python {gunicorn_conf}")
    return json.loads(result.output.decode())