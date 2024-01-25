def lang_callback(lang: Optional[str]) -> Union[str, None]:
    if lang is None:
        return None
    if not lang.isalpha() or len(lang) != 2:
        typer.echo("Use a 2 letter language code, like: es")
        raise typer.Abort()
    lang = lang.lower()
    return lang