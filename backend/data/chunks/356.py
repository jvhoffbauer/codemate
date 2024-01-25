def cov_tmp_path(tmp_path: Path):
    yield tmp_path
    for coverage_path in tmp_path.glob(".coverage*"):
        coverage_destiny_path = top_level_path / coverage_path.name
        shutil.copy(coverage_path, coverage_destiny_path)