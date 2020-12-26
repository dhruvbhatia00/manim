from manimlib.imports import *

class MovingOxygen(Scene):
    CONFIG = {
        "camera_config": {"background_color": "#2F2F2E"},
        "text_config": {"background_stroke_color": "#2F2F2E", "fill_color": WHITE, },
        "cell_path": r"C:\Manim\manim-26_05_2020\science_animations\speech_bubble_1_cell_ver1.png",
        "oxygen_path": r"C:\Manim\manim-26_05_2020\science_animations\speech_bubble_1_oxygen_ver1.png",
    }

    def construct(self):
        cell = ImageMobject(self.cell_path).scale(4)
        #rect = Rectangle(width=4, height=6)
        outside = []
        while len(outside) < 10:
            new_x = random.uniform(math.ceil(-FRAME_WIDTH/2),math.floor(FRAME_WIDTH/2))
            new_y = random.uniform(math.ceil(-FRAME_HEIGHT/2),math.floor(FRAME_HEIGHT/2))
            if (new_x < -2 or new_x > 2) and (-3 < new_y < 3):
                outside.append(np.array([new_x, new_y, 0]))

        inside = []
        while len(inside) < 10:
            new_x = random.uniform(math.ceil(-FRAME_WIDTH/2),math.floor(FRAME_WIDTH/2))
            new_y = random.uniform(math.ceil(-FRAME_HEIGHT/2),math.floor(FRAME_HEIGHT/2))
            if (-2 < new_x < 2) and (-3 < new_y < 3):
                inside.append(np.array([new_x, new_y, 0]))


        self.play(FadeIn(cell))
        ox = VGroup(*[Dot(pt, color=RED) for pt in outside])
        oxi = VGroup(*[Dot(pt, color=RED) for pt in inside])

        self.play(ShowCreation(ox))
        self.play(Transform(ox, oxi))


        self.wait(5)