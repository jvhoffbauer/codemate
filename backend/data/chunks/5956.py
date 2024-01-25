def _get_faa_globals__() -> Optional[ModuleType]:
    module_name = os.environ.get("FAA_GLOBALS", "")
    if not module_name:
        return None
    try:
        module = import_module(module_name)
    except ImportError as e:
        raise ImportError(f"Cannot import FAA_GLOBALS module {module_name}") from e
    global __globals__
    __globals__ = getattr(module, "__globals__", {})
    return module