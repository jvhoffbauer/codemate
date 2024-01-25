@invoke.task(pre=[sort], help={"targets": TARGETS_DESCRIPTION})
def fmt(ctx, targets="."):
    """Format python source code & sort imports."""
    print("formatting ...")
    args = ["black", targets]
    ctx.run(" ".join(args))