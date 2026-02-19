from __future__ import annotations

try:
    import pygame
except ImportError:  # pragma: no cover
    pygame = None

_image_cache: dict[str, object] = {}


def load_image(path: str):
    if path in _image_cache:
        return _image_cache[path]
    if pygame is None:
        raise RuntimeError("pygame no esta instalado. Ejecuta: pip install pygame")
    image = pygame.image.load(path).convert_alpha()
    _image_cache[path] = image
    return image
