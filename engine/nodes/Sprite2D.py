from __future__ import annotations

try:
    import pygame
except ImportError:  # pragma: no cover
    pygame = None

from engine.nodes.Node2D import Node2D
from engine.utils.loader import load_image


class Sprite2D(Node2D):
    def __init__(self, texture_path: str | None = None, name: str | None = None) -> None:
        super().__init__(name)
        class_texture = getattr(self.__class__, "texture", None)
        self.texture_path = texture_path or class_texture
        self.texture = None

    def ready(self) -> None:
        if pygame is None or not self.texture_path:
            return
        self.texture = load_image(self.texture_path)

    def draw(self, screen) -> None:
        if not self.texture:
            return
        draw_x = int(self.x + self.render_offset_x)
        draw_y = int(self.y + self.render_offset_y)
        screen.blit(self.texture, (draw_x, draw_y))
