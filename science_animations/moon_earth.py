from manimlib.imports import *

class Size(Scene):
    CONFIG = {
        "earth_config": {"checkerboard_colors": [BLUE_D, GREEN],
                            "resolution": (12, 24),
                            "radius": 8/32,
                            "u_min": 0.001,
                            "u_max": PI - 0.001,
                            "v_min": 0,
                            "v_max": TAU,},

    }

    def construct(self):
        text = TextMobject("Distance between the Earth and the Moon").to_edge(UP)
        line = Line(color=WHITE).scale(text.get_width()/2).next_to(text, DOWN)

        earths = VGroup()
        for i in range(30):
            earth = Circle(radius = 8/38, fill_opacity=1, stroke_width=0).set_color_by_gradient(GREEN, BLUE)
            earths.add(earth)

        moons = VGroup()
        for i in range(111):
            moon = Circle(radius = 8/38, fill_opacity=1, stroke_width=0).set_color(WHITE).scale(30/111)
            moons.add(moon)

        earths.arrange(RIGHT, buff=0).shift(0.7*UP)
        moons.arrange(RIGHT, buff=0 * 30/111).shift(0.7*DOWN)

        right_arrow = Arrow(buff=0).scale(earths.get_width()/4).shift(earths.get_width()/4 * RIGHT)
        left_arrow = Arrow(RIGHT, LEFT, buff=0).scale(earths.get_width()/4).shift(earths.get_width()/4 * LEFT)

        earth_brace = BraceLabel(earths, "30 earths", UP, label_constructor=TextMobject)
        moon_brace = BraceLabel(moons, "111 moons", DOWN, label_constructor=TextMobject)


        distance = TextMobject("384,400km").add_background_rectangle(color=BLACK, opacity=0.5)

        self.add(text)
        self.add(line)
        self.add(earths)
        self.add(moons)
        self.add(earth_brace)
        self.add(moon_brace)
        self.add(right_arrow)
        self.add(left_arrow)
        self.add(distance)


class Try(Scene):
    def construct(self):
        earth = VectorizedEarth()
        self.play(ShowCreation(earth))
        self.wait(3)