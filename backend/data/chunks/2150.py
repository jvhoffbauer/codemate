def update_config() -> None:
    config = get_en_config()
    languages = [{"en": "/"}]
    alternate: List[Dict[str, str]] = config["extra"].get("alternate", [])
    alternate_dict = {alt["link"]: alt["name"] for alt in alternate}
    new_alternate: List[Dict[str, str]] = []
    for lang_path in get_lang_paths():
        if lang_path.name == "en" or not lang_path.is_dir():
            continue
        name = lang_path.name
        languages.append({name: f"/{name}/"})
    for lang_dict in languages:
        name = list(lang_dict.keys())[0]
        url = lang_dict[name]
        if url not in alternate_dict:
            new_alternate.append({"link": url, "name": name})
        else:
            use_name = alternate_dict[url]
            new_alternate.append({"link": url, "name": use_name})
    config["extra"]["alternate"] = new_alternate
    en_config_path.write_text(
        yaml.dump(config, sort_keys=False, width=200, allow_unicode=True),
        encoding="utf-8",
    )