@lru_cache
def get_missing_translation_content(docs_dir: str) -> str:
    docs_dir_path = Path(docs_dir)
    missing_translation_path = docs_dir_path.parent.parent / "missing-translation.md"
    return missing_translation_path.read_text(encoding="utf-8")