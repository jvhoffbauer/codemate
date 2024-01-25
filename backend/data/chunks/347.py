def build() -> None:
    """
    Build the docs.
    """
    insiders_env_file = os.environ.get("INSIDERS_FILE")
    print(f"Insiders file {insiders_env_file}")
    if is_mkdocs_insiders():
        print("Using insiders")
    print("Building docs")
    subprocess.run(["mkdocs", "build"], check=True)
    typer.secho("Successfully built docs", color=typer.colors.GREEN)