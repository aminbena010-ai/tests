from __future__ import annotations

from engine.nodes.Area2D import Area2D
from engine.nodes.Node import Node


class SceneTree:
    def __init__(self, root: Node) -> None:
        self.root = root
        self._entered = False

    def enter_tree(self) -> None:
        if self._entered:
            return
        self.root._enter_tree()
        self._entered = True

    def add_child(self, node: Node) -> None:
        self.root.add_child(node)

    def process(self, dt: float) -> None:
        self.root._propagate_process(dt)
        self._update_area_overlaps()

    def draw(self, screen) -> None:
        self.root._propagate_draw(screen)

    def _update_area_overlaps(self) -> None:
        areas = [node for node in self.root.walk() if isinstance(node, Area2D)]
        for i, area_a in enumerate(areas):
            for area_b in areas[i + 1 :]:
                area_a.update_overlap(area_b)
                area_b.update_overlap(area_a)
