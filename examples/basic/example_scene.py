from __future__ import annotations

import sys
from pathlib import Path

if __package__ in (None, ""):
    project_root = Path(__file__).resolve().parents[2]
    project_root_str = str(project_root)
    if project_root_str not in sys.path:
        sys.path.insert(0, project_root_str)

from engine.core.Engine import Engine
from engine.nodes.Camera2D import Camera2D
from engine.nodes.Node2D import Node2D

from examples.basic.example_player import Player


class FollowCamera(Camera2D):
    target = "Player"


def build_scene() -> Node2D:
    root = Node2D("Root")
    player = Player()
    camera = FollowCamera()
    root.add_child(player)
    root.add_child(camera)
    return root


def main() -> None:
    root = build_scene()
    Engine(root).run()


if __name__ == "__main__":
    main()
