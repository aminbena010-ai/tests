from __future__ import annotations

try:
    import pygame
except ImportError:  # pragma: no cover
    pygame = None

from engine.nodes.Node2D import Node2D
from engine.utils.loader import load_image


class AnimatedSprite2D(Node2D):
    def __init__(
        self,
        frames: list[str] | None = None,
        animation_speed: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(name)
        class_frames = getattr(self.__class__, "frames", ())
        class_animation_speed = getattr(self.__class__, "animation_speed", 10.0)
        self.frames_paths = list(frames) if frames is not None else list(class_frames)
        self.animation_speed = (
            float(animation_speed) if animation_speed is not None else float(class_animation_speed)
        )
        self._frames_surfaces: list = []
        self._frame_index = 0.0

    def ready(self) -> None:
        super().ready()
        if pygame is None or not self.frames_paths:
            return
        self._frames_surfaces = [load_image(path) for path in self.frames_paths]

    def process(self, dt: float) -> None:
        super().process(dt)
        if not self._frames_surfaces:
            return
        self._frame_index += self.animation_speed * dt
        if self._frame_index >= len(self._frames_surfaces):
            self._frame_index = 0.0

    def draw(self, screen) -> None:
        if self._frames_surfaces:
            draw_x = int(self.x + self.render_offset_x)
            draw_y = int(self.y + self.render_offset_y)
            frame = self._frames_surfaces[int(self._frame_index)]
            screen.blit(frame, (draw_x, draw_y))
            return
        super().draw(screen)
