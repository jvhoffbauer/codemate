def check(
    ctx, fmt=False, sort=False, diff=False
):  # pylint: disable=redefined-outer-name
    """Check code format and import order."""
    if not any([fmt, sort]):
        fmt = True
        sort = True

    fmt_args = ["black", "--check", "."]
    sort_args = ["isort", "--check", "."]

    if diff:
        fmt_args.append("--diff")
        sort_args.append("--diff")

    # FIXME: run each command and check return code
    cmd_args = []
    if fmt:
        cmd_args.extend(fmt_args)
    if sort:
        if cmd_args:
            cmd_args.append("&")
        cmd_args.extend(sort_args)
    ctx.run(" ".join(cmd_args))