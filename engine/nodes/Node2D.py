from __future__ import annotations

try:
    import pygame
except ImportError:  # pragma: no cover
    pygame = None

from engine.input.key import key
from engine.nodes.Node import Node
from engine.utils.loader import load_image


class Node2D(Node):
    def __init__(self, name: str | None = None) -> None:
        super().__init__(name)
        self.x = 0.0
        self.y = 0.0
        self.rotation = 0.0
        self.scale_x = 1.0
        self.scale_y = 1.0
        class_speed = getattr(self.__class__, "speed", 0.0)
        class_profiles = getattr(self.__class__, "input_profiles", ())
        self.speed = float(class_speed)
        self.input_profiles: tuple[str, ...] = tuple(class_profiles)
        self.render_offset_x = 0.0
        self.render_offset_y = 0.0
        self.texture = getattr(self.__class__, "texture", None)
        self._texture_surface = None
        self._characterbody2d_callbacks = self._collect_callbacks("_is_characterbody2d_callback")
        self._sprite_setup_callbacks = self._collect_callbacks("_is_sprite_setup_callback")

    def ready(self) -> None:
        for callback in self._sprite_setup_callbacks:
            self._invoke_callback(callback)
        if pygame is None or not self.texture:
            return
        self._texture_surface = load_image(self.texture)

    def process(self, dt: float) -> None:
        self.auto_move(dt)
        if self._characterbody2d_callbacks:
            input_axis = key.input(*self.input_profiles) if self.input_profiles else (0.0, 0.0)
            for callback in self._characterbody2d_callbacks:
                self._invoke_callback(callback, input_axis, dt)

    def auto_move(self, dt: float) -> None:
        if self.speed <= 0 or not self.input_profiles:
            return
        axis_x, axis_y = key.input(*self.input_profiles)
        self.x += axis_x * self.speed * dt
        self.y += axis_y * self.speed * dt

    def draw(self, screen) -> None:
        if self._texture_surface is None:
            return
        draw_x = int(self.x + self.render_offset_x)
        draw_y = int(self.y + self.render_offset_y)
        screen.blit(self._texture_surface, (draw_x, draw_y))
