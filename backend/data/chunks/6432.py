@invoke.task(help={"targets": TARGETS_DESCRIPTION})
def sort(ctx, targets="."):
    """Sort module imports."""
    print("sorting imports ...")
    args = ["isort", "--atomic", targets]
    ctx.run(" ".join(args))