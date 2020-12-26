from manimlib.imports import *

class Slider(NumberLine):
    CONFIG = {
        "color": WHITE,
        "x_min": 0,
        "x_max": 10,
        "unit_size": 4/10,
        "start_value": 1,
        "number_scale_val": 0.75,
        "label_scale_val": 1,
        "numbers_with_elongated_ticks": [],
        #"line_to_number_vect": LEFT,
        "line_to_number_buff": MED_LARGE_BUFF,
        "dial_radius": 0.1,
        "dial_color": YELLOW,
        "label_direction": LEFT,
        "numbers_to_show": np.arange(0,11,5),
        "decimal_number_config": {
            "num_decimal_places": 0, "background_stroke_color": BLACK, "fill_color": WHITE,
        },
        "text_config": {"background_stroke_color": BLACK, "fill_color": WHITE}
    }

    def __init__(self, **kwargs):
        NumberLine.__init__(self, **kwargs)
        self.rotate(np.pi/2)
        self.move_to(ORIGIN)
        self.init_dial()

    def init_dial(self):
        dial = Dot(
            radius=self.dial_radius,
            color=self.dial_color,
        )
        dial.move_to(self.number_to_point(self.start_value))

        value = DecimalNumber(self.start_value, **self.text_config).next_to(dial, RIGHT)


        self.add(dial)
        self.dial = dial
        self.add(value)
        self.value = value

    def add_label(self, tex):
        label = TexMobject(tex, **self.text_config)
        label.scale(self.label_scale_val)


        label.move_to(np.array([self.dial.get_center()[0], self.get_top()[1], 0]))
        label.shift(MED_LARGE_BUFF*UP)
        self.add(label)
        self.label = label

    def get_value(self):
        return self.point_to_number(self.dial.get_center())

    def set_value(self, x):
        self.dial.move_to(self.number_to_point(x))
        self.value.set_value(x)
        self.value.next_to(self.dial, RIGHT)

    def copy(self):
        return self.deepcopy()



class Sliders(Scene):
    CONFIG = {
        "slider_config": {"color": BLUE,
                          "x_min": 0,
                          "x_max": 30,
                          "unit_size": 4 / 20,
                          "numbers_to_show": np.arange(0, 31, 5),
                          "decimal_number_config":
                              {"num_decimal_places": 0, "background_stroke_color": "#2F2F2E", "fill_color": WHITE,},
                          "text_config": {"background_stroke_color": "#2F2F2E", "fill_color": WHITE,},
                          "dial_color": RED,
                          },
        "num_sliders": 3,
        "start_point": None,
        "camera_config": {"background_color": "#2F2F2E"},
        "slider_spacing": 0.9*LARGE_BUFF,
        "text_config": {"background_stroke_color": "#2F2F2E", "fill_color": WHITE, },
        "back": r"C:\Manim\manim-26_05_2020\science_animations\blackboard_texture.png",
    }

    def setup(self):
        self.scale_factor = ValueTracker(1, **self.slider_config["text_config"])

        if self.start_point is None:
            self.start_point = np.ones(self.num_sliders)
        sliders = VGroup(*[
            Slider(start_value=cv, **self.slider_config)
            for cv in self.start_point
        ])
        sliders.arrange(RIGHT, buff=self.slider_spacing)

        self.sliders = sliders
        self.add_labels_to_sliders()
        self.sliders[0].add_numbers()
        for slider in self.sliders:
            slider.save_state()

    def add_labels_to_sliders(self):
        if len(self.sliders) <= 3:
            for slider, char in zip(self.sliders, ["\\text{Length}", "\\text{Area}", "\\text{Volume}"]):
                slider.add_label(char)
            for slider in self.sliders[1:]:
                slider.label.align_to(self.sliders[0].label, UP)
        else:
            for i, slider in enumerate(self.sliders):
                slider.add_label("x_{%d}"%(i+1))
        return self

    def update_sliders(self, sf=1, *other_animations, **kwargs):
        def update_func(slider, exponent):
            slider.set_value(self.scale_factor.get_value()**exponent)

        slider_animations = [UpdateFromFunc(self.sliders[0], lambda slider: update_func(slider, 1)),
                             UpdateFromFunc(self.sliders[1], lambda slider: update_func(slider, 2)),
                             UpdateFromFunc(self.sliders[2], lambda slider: update_func(slider, 3))]

        self.play(self.scale_factor.set_value, sf,
                  *slider_animations, *other_animations, **kwargs)

    def construct(self):
        back = ImageMobject(self.back).scale(4)
        #self.add(back)
        bear = ImageMobject(r"C:\Manim\manim-26_05_2020\science_animations\cube_bear_png_1.png")
        bear.shift(3.2*LEFT).scale(2)
        line = Line(ORIGIN, 1.75*UP).scale(2/3).shift(3.95*LEFT + 0.6*DOWN)
        brace1 = BraceLabel(line, "1", LEFT, **self.text_config)

        self.sliders.shift(3.8*RIGHT)
        self.play(FadeIn(self.sliders), FadeIn(bear), FadeIn(brace1))
        self.wait()

        line.scale(2).shift(0.85*LEFT + 0.2*UP)
        brace2 = BraceLabel(line, 2, LEFT, **self.text_config)
        self.update_sliders(2, ApplyMethod(bear.scale, 2), Transform(brace1, brace2), run_time=2)
        self.wait()
        line.scale(3/2).shift(1*LEFT + 0.2*UP)
        brace2 = BraceLabel(line, 3, LEFT, **self.text_config)
        self.update_sliders(3, ApplyMethod(bear.scale, 3/2), Transform(brace1, brace2), run_time=2)

        self.wait(2)

        self.play(FadeOut(brace1), FadeOut(self.sliders),
                  bear.move_to, ORIGIN)
        self.wait(2)

        directions = [3*RIGHT, 3*(UP+RIGHT), 4*UP, 3*(UP+LEFT), 3*LEFT]
        heat = VGroup()
        for i in range(5):
            g = FunctionGraph(lambda x: math.sin(5*x), color=RED).scale(0.2)
            g.rotate(interpolate(0, PI, i/4))
            g.shift(directions[i])
            heat.add(g)

        self.play(ShowCreationThenDestruction(heat))
        self.play(ShowCreationThenDestruction(heat))
        self.play(ShowCreationThenDestruction(heat))

        self.wait(5)

class Test(Scene):
    CONFIG = {
        "text_config": {"background_stroke_color": WHITE, "fill_color": BLACK, },
    }

    def construct(self):
        d = Dot(ORIGIN)
        v = DecimalNumber(0, **self.text_config).next_to(d, RIGHT)

        def update(mob):
            mob.next_to(d, RIGHT)
            mob.set_value(d.get_center()[1])

        self.play(ShowCreation(v), ShowCreation(d))

        self.play(d.shift, UP,
                  UpdateFromFunc(v, update))

        self.wait(2)



