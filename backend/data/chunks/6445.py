def docker(
    ctx,
    build=False,
    run=False,
    tag="covid-tracker-api:latest",
    name=f"covid-api-{random.randint(0,999)}",
):
    """Build and run docker container."""
    if not any([build, run]):
        raise invoke.Exit(message="Specify either --build or --run", code=1)
    if build:
        docker_cmds = ["build", "."]
    else:
        docker_cmds = ["run", "--publish", "80", "--name", name]
    ctx.run(" ".join(["docker", *docker_cmds, "-t", tag]))