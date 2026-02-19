from __future__ import annotations

from engine.nodes.Node2D import Node2D


class Area2D(Node2D):
    def __init__(
        self,
        width: float | None = None,
        height: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(name)
        class_size = getattr(self.__class__, "size", None)
        if class_size is not None and len(class_size) == 2:
            size_w = float(class_size[0])
            size_h = float(class_size[1])
        else:
            size_w = 32.0
            size_h = 32.0
        self.width = float(width) if width is not None else size_w
        self.height = float(height) if height is not None else size_h
        self._overlapping: set[Area2D] = set()
        self._enter_callbacks = self._collect_callbacks("_is_enter_callback")

    def overlaps(self, other: "Area2D") -> bool:
        left_a = self.x
        right_a = self.x + self.width
        top_a = self.y
        bottom_a = self.y + self.height

        left_b = other.x
        right_b = other.x + other.width
        top_b = other.y
        bottom_b = other.y + other.height

        return left_a < right_b and right_a > left_b and top_a < bottom_b and bottom_a > top_b

    def update_overlap(self, other: "Area2D") -> None:
        is_overlapping = self.overlaps(other)
        was_overlapping = other in self._overlapping
        if is_overlapping and not was_overlapping:
            self._overlapping.add(other)
            self.on_body_entered(other)
        if not is_overlapping and was_overlapping:
            self._overlapping.remove(other)
            self.on_body_exited(other)

    def on_body_entered(self, other: "Area2D") -> None:
        for callback in self._enter_callbacks:
            self._invoke_callback(callback, other)

    def on_body_exited(self, other: "Area2D") -> None:
        pass
