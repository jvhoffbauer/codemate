def serve() -> None:
    """
    A quick server to preview a built site.

    For development, prefer the command live (or just mkdocs serve).

    This is here only to preview the documentation site.

    Make sure you run the build command first.
    """
    typer.echo("Warning: this is a very simple server.")
    typer.echo("For development, use the command live instead.")
    typer.echo("This is here only to preview the documentation site.")
    typer.echo("Make sure you run the build command first.")
    os.chdir("site")
    server_address = ("", 8008)
    server = HTTPServer(server_address, SimpleHTTPRequestHandler)
    typer.echo("Serving at: http://127.0.0.1:8008")
    server.serve_forever()