def on_files(files: Files, *, config: MkDocsConfig) -> Files:
    resolve_files(items=config.nav or [], files=files, config=config)
    if "logo" in config.theme:
        resolve_file(item=config.theme["logo"], files=files, config=config)
    if "favicon" in config.theme:
        resolve_file(item=config.theme["favicon"], files=files, config=config)
    resolve_files(items=config.extra_css, files=files, config=config)
    resolve_files(items=config.extra_javascript, files=files, config=config)
    return files