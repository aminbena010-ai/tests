from __future__ import annotations

import sys
from pathlib import Path

if __package__ in (None, ""):
    project_root = Path(__file__).resolve().parents[2]
    project_root_str = str(project_root)
    if project_root_str not in sys.path:
        sys.path.insert(0, project_root_str)

try:
    import pygame
except ImportError:  # pragma: no cover
    pygame = None

from engine.decorators import on_process, on_ready
from engine.input.key import key
from engine.nodes.Node2D import Node2D


class Player(Node2D):
    speed = 260.0
    key.input("wasd", "arrow")
    color = (90, 220, 150)

    @on_ready
    def spawn(self) -> None:
        self.x = 120
        self.y = 120

    @on_process
    def animate(self, dt: float) -> None:
        self.rotation += 70.0 * dt

    def draw(self, screen) -> None:
        if pygame is None:
            return
        x = int(self.x + self.render_offset_x)
        y = int(self.y + self.render_offset_y)
        pygame.draw.circle(screen, self.color, (x, y), 18)
