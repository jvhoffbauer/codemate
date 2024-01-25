def create_env_file_and_remove_env_template():
    env_template_file = Path(".env.template")
    env_file = Path(".env")

    env_file.write_text(env_template_file.read_text())
    env_template_file.unlink()