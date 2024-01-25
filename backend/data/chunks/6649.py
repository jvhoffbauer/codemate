def get_gunicorn_conf_path(container: Container) -> str:
    gunicorn_processes = get_process_names(container)
    first_process = gunicorn_processes[0]
    first_part, partition, last_part = first_process.partition("-c")
    gunicorn_conf = last_part.strip().split()[0]
    return gunicorn_conf