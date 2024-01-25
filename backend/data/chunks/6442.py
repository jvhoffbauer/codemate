@invoke.task
def generate_reqs(ctx):
    """Generate requirements.txt"""
    # NOTE: updated for pipenv 2020 release
    # TODO: make backwards compatible
    reqs = [
        "pipenv lock -r > requirements.txt",
        "pipenv lock -r --dev-only > requirements-dev.txt",
    ]
    [ctx.run(req) for req in reqs]