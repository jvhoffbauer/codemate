def coverage_run(*, module: str, cwd: Union[str, Path]) -> subprocess.CompletedProcess:
    result = subprocess.run(
        [
            "coverage",
            "run",
            "--parallel-mode",
            "--source=docs_src,tests,sqlmodel",
            "-m",
            module,
        ],
        cwd=str(cwd),
        capture_output=True,
        encoding="utf-8",
    )
    return result