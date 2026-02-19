from __future__ import annotations

from engine.nodes.Node2D import Node2D


class Camera2D(Node2D):
    def __init__(self, target: Node2D | str | None = None, name: str | None = None) -> None:
        super().__init__(name)
        class_target = getattr(self.__class__, "target", None)
        self.target = target if target is not None else class_target
        self.offset_x = 0.0
        self.offset_y = 0.0
        self.current = True

    def apply_to_root(self, root) -> None:
        focus = self.target or self.parent
        if isinstance(focus, str):
            focus = root.get_node(focus)
        if not isinstance(focus, Node2D):
            return
        cam_x = -focus.x + self.offset_x
        cam_y = -focus.y + self.offset_y
        for node in root.walk():
            if isinstance(node, Node2D):
                node.render_offset_x = cam_x
                node.render_offset_y = cam_y
