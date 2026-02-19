from __future__ import annotations

try:
    import pygame
except ImportError:  # pragma: no cover
    pygame = None

from engine.core.SceneTree import SceneTree
from engine.input.key import key
from engine.nodes.Camera2D import Camera2D
from engine.nodes.Node import Node


class Engine:
    def __init__(self, root: Node, width: int = 960, height: int = 540, fps: int = 60) -> None:
        self.width = width
        self.height = height
        self.fps = fps
        self.tree = SceneTree(root)
        self._running = False

    def run(self) -> None:
        if pygame is None:
            raise RuntimeError("pygame no esta instalado. Ejecuta: pip install pygame")

        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("your_engine 0.1")
        clock = pygame.time.Clock()
        self.tree.enter_tree()
        self._running = True

        while self._running:
            dt = clock.tick(self.fps) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False

            pressed = pygame.key.get_pressed()
            key.update_from_pygame_pressed(pressed, pygame)

            self.tree.process(dt)
            screen.fill((18, 18, 22))

            camera = self._find_active_camera()
            if camera:
                camera.apply_to_root(self.tree.root)
            else:
                self._reset_render_offsets()

            self.tree.draw(screen)
            pygame.display.flip()

        pygame.quit()

    def _find_active_camera(self) -> Camera2D | None:
        for node in self.tree.root.walk():
            if isinstance(node, Camera2D) and node.current:
                return node
        return None

    def _reset_render_offsets(self) -> None:
        for node in self.tree.root.walk():
            if isinstance(node, Node):
                if hasattr(node, "render_offset_x"):
                    node.render_offset_x = 0.0
                if hasattr(node, "render_offset_y"):
                    node.render_offset_y = 0.0
