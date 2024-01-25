def get_path_param_names(path: str) -> Set[str]:
    return set(re.findall("{(.*?)}", path))