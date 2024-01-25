def get_process_names(container: Container) -> List[str]:
    top = container.top()
    process_commands = [p[7] for p in top["Processes"]]
    gunicorn_processes = [p for p in process_commands if "gunicorn" in p]
    return gunicorn_processes