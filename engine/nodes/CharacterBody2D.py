from __future__ import annotations

from engine.nodes.Node2D import Node2D


class CharacterBody2D(Node2D):
    def __init__(self, name: str | None = None) -> None:
        super().__init__(name)
        self.velocity_x = 0.0
        self.velocity_y = 0.0
        self.gravity = 900.0
        self.use_gravity = False

    def process(self, dt: float) -> None:
        self.auto_move(dt)
        if self.use_gravity:
            self.velocity_y += self.gravity * dt
        self.move_and_slide(dt)

    def move_and_slide(self, dt: float) -> None:
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
