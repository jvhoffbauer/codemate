def resolve_file(*, item: str, files: Files, config: MkDocsConfig) -> None:
    item_path = Path(config.docs_dir) / item
    if not item_path.is_file():
        en_src_dir = (Path(config.docs_dir) / "../../en/docs").resolve()
        potential_path = en_src_dir / item
        if potential_path.is_file():
            files.append(
                EnFile(
                    path=item,
                    src_dir=str(en_src_dir),
                    dest_dir=config.site_dir,
                    use_directory_urls=config.use_directory_urls,
                )
            )