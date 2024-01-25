def on_config(config: MkDocsConfig, **kwargs: Any) -> MkDocsConfig:
    available_langs = get_mkdocs_material_langs()
    dir_path = Path(config.docs_dir)
    lang = dir_path.parent.name
    if lang in available_langs:
        config.theme["language"] = lang
    if not (config.site_url or "").endswith(f"{lang}/") and not lang == "en":
        config.site_url = f"{config.site_url}{lang}/"
    return config