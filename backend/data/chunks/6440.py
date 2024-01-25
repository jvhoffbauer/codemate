@invoke.task
def test(ctx):
    """Run pytest tests."""
    ctx.run(" ".join(["pytest", "-v"]))