def get_lang_paths() -> List[Path]:
    return sorted(docs_path.iterdir())