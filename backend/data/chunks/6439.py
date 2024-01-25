def lint(ctx):
    """Run linter."""
    ctx.run(" ".join(["pylint", "app"]))