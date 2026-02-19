from engine.nodes.Area2D import Area2D
from engine.nodes.AnimatedSprite2D import AnimatedSprite2D
from engine.nodes.Camera2D import Camera2D
from engine.nodes.CharacterBody2D import CharacterBody2D
from engine.nodes.Node import Node
from engine.nodes.Node2D import Node2D
from engine.nodes.Sprite2D import Sprite2D
import importlib
import sys

__all__ = [
    "Node",
    "Node2D",
    "Sprite2D",
    "AnimatedSprite2D",
    "CharacterBody2D",
    "Area2D",
    "Camera2D",
]

# Windows cannot store both Node2D.py and node2d.py.
# Register lowercase module aliases to support `engine.nodes.node2d` style imports.
_ALIASES = {
    "node": "Node",
    "node2d": "Node2D",
    "sprite2d": "Sprite2D",
    "characterbody2d": "CharacterBody2D",
    "area2d": "Area2D",
    "camera2d": "Camera2D",
    "animatedsprite2d": "AnimatedSprite2D",
}
for _alias, _target in _ALIASES.items():
    sys.modules[f"{__name__}.{_alias}"] = importlib.import_module(f"{__name__}.{_target}")
