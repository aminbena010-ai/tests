from __future__ import annotations

import sys
from pathlib import Path

if __package__ in (None, ""):
    project_root = Path(__file__).resolve().parents[2]
    project_root_str = str(project_root)
    if project_root_str not in sys.path:
        sys.path.insert(0, project_root_str)

from engine.decorators.characterbody2d import characterbody2d
from engine.decorators.sprite import sprite
from engine.input.key import key
from engine.nodes.Node2D import Node2D


class Player(Node2D):
    speed = 220
    key.input("wasd", "arrow")

    @characterbody2d
    def mov(self, input_axis, dt):
        # Hook visual: aqui puedes extender o reemplazar la logica.
        pass

    @sprite
    def sprint(self):
        self.texture = "assets/sprites/player.png"
