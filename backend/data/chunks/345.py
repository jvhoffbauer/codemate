def live() -> None:
    """
    Serve with livereload a docs site for a specific language.

    This only shows the actual translated files, not the placeholders created with
    build-all.

    Takes an optional LANG argument with the name of the language to serve, by default
    en.
    """
    # Enable line numbers during local development to make it easier to highlight
    os.environ["LINENUMS"] = "true"
    mkdocs.commands.serve.serve(dev_addr="127.0.0.1:8008")