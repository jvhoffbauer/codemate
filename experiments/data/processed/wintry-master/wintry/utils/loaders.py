import importlib
from pathlib import Path
from typing import List

from wintry.settings import WinterSettings


class LoaderError(Exception):
    pass


def to_package_format(path: Path) -> str:
    module_fs_path = ".".join(path.parts)
    # remove module last .py extension
    module = module_fs_path.replace(".py", "")
    # if module is like "path.to.module.__init__", then
    # leave it as "path.to.module"
    if module.endswith(".__init__"):
        return module.replace(".__init__", "")

    return module


def discover(path: Path, app_path: str):
    dirs: list[Path] = [path]
    while dirs:
        module = dirs.pop(0)
        for sub_module in module.iterdir():
            if sub_module.is_dir():
                dirs.append(sub_module)
            else:
                if sub_module.name.endswith(".py"):
                    try:
                        mod = to_package_format(sub_module)
                        if mod not in app_path:
                            importlib.import_module(mod)
                    except ModuleNotFoundError as e:
                        raise LoaderError(str(e))


def autodiscover_modules(modules: List[str], app_path: str):
    """Utility to automatically import the app's modules so there is
    no need to manual importing controllers, services, etc, to provide
    the necessary registry for DI

    Args:
        modules:
        app_path:

    Returns:
        None

    """

    for module in modules:
        app_root = Path(module)

        if not app_root.is_dir():
            raise LoaderError(
                f"{app_root.resolve()} is not a dir. Autodiscovery must be called on a dir."
            )

        discover(app_root, app_path)
