from __future__ import annotations

import sys
from pathlib import Path

if __package__ in (None, ""):
    project_root = Path(__file__).resolve().parents[2]
    project_root_str = str(project_root)
    if project_root_str not in sys.path:
        sys.path.insert(0, project_root_str)

from engine.core.Engine import Engine
from engine.nodes.Node2D import Node2D
from examples.basic.player import Player


def main() -> None:
    root = Node2D()
    root.add_child(Player())
    Engine(root).run()


if __name__ == "__main__":
    main()
