from manim import *
import numpy as np

class ExtinctionVortex(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES, zoom=0.6)

        # Vortex that tightens gently like a tornado
        def vortex_func(t):
            r = 2.5 - 0.15 * t  # Gradually tighter
            r = max(r, 0.2)     # Avoid collapsing to zero
            return np.array([
                r * np.sin(t),
                r * np.cos(t),
                -t * 0.4
            ])

        spiral_shift = np.array([0, 0, 5])

        vortex_path = ParametricFunction(
            lambda t: vortex_func(t) + spiral_shift,
            t_range=[0, 8 * PI],
            color=RED,
            stroke_width=3
        )

        dot = Dot3D(color=YELLOW, radius=0.15)
        dot.move_to(vortex_path.get_start())

        self.play(Create(vortex_path))
        self.play(FadeIn(dot))
        self.play(MoveAlongPath(dot, vortex_path), run_time=8)
        self.wait(1)
        self.play(FadeOut(dot), FadeOut(vortex_path))
