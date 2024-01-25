def amis_templates(template_path: str, encoding="utf8") -> Template:
    """page template"""
    with open(template_path, encoding=encoding) as f:
        return Template(f.read())