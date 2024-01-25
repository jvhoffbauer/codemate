def get_mkdocs_material_langs() -> List[str]:
    material_path = Path(material.__file__).parent
    material_langs_path = material_path / "templates" / "partials" / "languages"
    langs = [file.stem for file in material_langs_path.glob("*.html")]
    return langs