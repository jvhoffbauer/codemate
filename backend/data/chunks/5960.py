def _exists_faa_global(name: str) -> bool:
    """Judge whether the global variable exists in the FAA_GLOBALS module"""
    return __faa_globals__ is not None and hasattr(__faa_globals__, name)