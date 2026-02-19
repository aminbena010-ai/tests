from __future__ import annotations

from engine.nodes.AnimatedSprite2D import AnimatedSprite2D


class AnimatedPlayer(AnimatedSprite2D):
    frames = [
        "assets/sprites/player.png",
        "assets/sprites/player.png",
    ]
    animation_speed = 6.0
