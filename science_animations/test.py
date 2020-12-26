from manimlib.imports import *

class Test1(Scene):
    CONFIG = {

    }

    def construct(self):
        lines = StreamLines(lambda x: np.array([1, 0, 0]),
                            **{"x_min": -4,
                                "x_max": 0,
                                "y_min": -2,
                                "y_max": 2,
                                "delta_x": 0.5,
                                "delta_y": 0.25,
                                "n_repeats": 1,
                                "noise_factor": 1,})
        anim = AnimatedStreamLines(lines,
                                   **{"lag_range": 2,
                                        "line_anim_class": ShowPassingFlash,
                                        "line_anim_config": {
                                            "run_time": 1,
                                            "rate_func": linear,
                                            "time_width": 0.4,
                                        },})

        self.add(anim)

        self.wait(2)


class Test2(Scene):
    CONFIG = {
        "path_1": r"C:\Manim\manim-26_05_2020\science_animations\animals_being_served_linear.png",
        "path_2": r"C:\Manim\manim-26_05_2020\science_animations\animals_being_served_sloped.png",
    }

    def construct(self):
        image_1 = ImageMobject(self.path_1).scale(4)
        self.add(image_1)
        self.wait()
        g = FunctionGraph(lambda x: 0.17*x - 0.2, x_min=0, x_max=8.4, color=RED, stroke_width=4).shift(4*LEFT)
        self.play(ShowCreation(g))
        self.wait(2)
        self.play(FadeOut(g))

        self.wait(2)

        image_2 = ImageMobject(self.path_2).scale(4)
        self.add(image_2)
        self.wait()
        self.play(FadeIn(g))
        g2 = FunctionGraph(lambda x: 0.17*x**(0.8) - 0.2, x_min=0, x_max=8.4, color=DARK_BLUE, stroke_width=4).shift(4*LEFT)

        self.play(TransformFromCopy(g, g2))


        self.wait(5)


class Test2B(Scene):
    CONFIG = {
        "path_1": r"C:\Manim\manim-26_05_2020\science_animations\animals_being_served_linear.png",
        "path_2": r"C:\Manim\manim-26_05_2020\science_animations\animals_being_served_sloped.png",
    }

    def construct(self):
        # image_1 = ImageMobject(self.path_1).scale(4)
        # self.add(image_1)
        # self.wait()
        g = FunctionGraph(lambda x: 0.17 * x - 0.2, x_min=0, x_max=8.4, color=RED, stroke_width=4).shift(4 * LEFT)
        # self.play(ShowCreation(g))
        # self.wait(2)
        # self.play(FadeOut(g))
        #
        # self.wait(2)

        image_2 = ImageMobject(self.path_2).scale(4)
        self.add(image_2)
        self.wait()
        self.play(FadeIn(g))
        g2 = FunctionGraph(lambda x: 0.17 * x ** (0.8) - 0.2, x_min=0, x_max=8.4, color=DARK_BLUE,
                           stroke_width=4).shift(4 * LEFT)
        g3 = FunctionGraph(lambda x: 0.17*3 * math.log(x+1) - 0.2 + 0.0*x, x_min=0, x_max=8.4, color=ORANGE,
                           stroke_width=4).shift(4*LEFT)

        self.play(TransformFromCopy(g, g2))
        self.play(TransformFromCopy(g, g3))

        self.wait(5)



class Test3(Scene):
    CONFIG = {
        "camera_config": {"background_color": "#2F2F2E", },
        "path_1": r"C:\Manim\manim-26_05_2020\science_animations\man_stairs.png",
        "path_2": r"C:\Manim\manim-26_05_2020\science_animations\man_with_goat_stairs.png",
        "back": r"C:\Manim\manim-26_05_2020\science_animations\blackboard_texture.png",
    }

    def construct(self):
        back = ImageMobject(self.back).scale(4)
        #self.add(back)
        image_1 = ImageMobject(self.path_1).scale(4)

        self.play(FadeIn(image_1))
        self.wait(2)

        image_2 = ImageMobject(self.path_2).scale(4)
        self.play(Transform(image_1, image_2))
        self.wait(3)


class Test4(Scene):
    CONFIG = {
        "camera_config": {"background_color": "#2F2F2E", },
        "text_config": {"stroke_color": "#2F2F2E", "fill_color": WHITE},
        "path_1": r"C:\Manim\manim-26_05_2020\science_animations\green_check.png",
        "back": r"C:\Manim\manim-26_05_2020\science_animations\blackboard_texture.png",
    }

    def construct(self):
        back = ImageMobject(self.back).scale(4)
        #self.add(back)
        top_text = TextMobject("\\underline{Good Theory Checklist}", **self.text_config).shift(1.5*UP)
        list1 = TextMobject("$\\square$ Accurately predict real-world data", **self.text_config)
        list2 = TextMobject("$\\square$ Make reasonable assumptions", **self.text_config).align_to(list1, LEFT, alignment_vect=UP).shift(1*DOWN)
        self.play(Write(top_text))
        self.play(Write(list1))
        self.play(Write(list2))
        self.wait(2)

        check1 = ImageMobject(self.path_1).scale(0.25).move_to(list1.get_left()).shift(0.2 * RIGHT + 0.1*UP)
        check2 = ImageMobject(self.path_1).scale(0.25).move_to(list2.get_left()).shift(0.2 * RIGHT + 0.1*UP)

        self.play(FadeIn(check1))
        self.wait(2)
        self.play(FadeOut(check1))
        self.wait(2)
        self.play(FadeIn(check2))
        self.wait(2)
        self.play(FadeOut(check2))
        # self.play(FadeIn(check1), FadeIn(check2))

        self.wait(3)


class Test5(Scene):
    CONFIG = {
        "camera_config": {"background_color": GREEN, },
        "text_config": {"stroke_color": "#2F2F2E", "fill_color": WHITE},
        "back": r"C:\Manim\manim-26_05_2020\science_animations\blackboard_texture.png",
        "path_1": r"C:\Manim\manim-26_05_2020\science_animations\elephant.png",
        "path_2": r"C:\Manim\manim-26_05_2020\science_animations\mouse.png",
        "path_3": r"C:\Manim\manim-26_05_2020\science_animations\energy.png",
    }

    def construct(self):
        back = ImageMobject(self.back).scale(4)
        #self.add(back)
        elephant = ImageMobject(self.path_1).scale(4)
        mouse = ImageMobject(self.path_2).scale(4)
        energy = TextMobject("Energy?", **self.text_config).scale(3.5).move_to(1.25*UP + 3.6*LEFT)

        self.play(FadeIn(elephant))
        self.wait()
        self.play(FadeIn(mouse))
        self.wait()
        self.play(Write(energy))
        self.wait(3)


class Test6(MovingCameraScene):
    CONFIG = {
        "back": r"C:\Manim\manim-26_05_2020\science_animations\blackboard_texture.png",
    }

    def construct(self):
        back = ImageMobject(self.back).scale(4)
        self.add(back)

        l = Line(color=WHITE)

        self.play(ShowCreation(l))

        self.play(self.camera_frame.set_width, 20,
                  back.scale, 1.40625)
        self.wait(2)


class Credits(Scene):
    CONFIG = {
        #"camera_config": {"background_color": "#2F2F2E", },
        #"text_config": {"stroke_color": "#2F2F2E", "fill_color": WHITE},
        "back": r"C:\Manim\manim-26_05_2020\science_animations\blackboard_texture.png",
    }

    def construct(self):
        text1 = TextMobject("By Dhruv Bhatia,", "Joe Emmetti,", "and Thomas Patti").arrange(DOWN)
        text2 = TextMobject("With thanks to", "Steven Subotnick,", "John Stein,", "and Faye Thomas").arrange(DOWN)
        text3 = TextMobject("Made with Manim,", "an open source animation library", "by Grant Sanderson").arrange(DOWN)

        self.play(ShowCreation(text1), run_time=2)
        self.wait(3)
        self.play(Uncreate(text1), run_time=2)

        self.play(ShowCreation(text2), run_time=2)
        self.wait(3)
        self.play(Uncreate(text2), run_time=2)

        self.play(ShowCreation(text3), run_time=2)
        self.wait(3)
        self.play(Uncreate(text3), run_time=2)

        self.wait(3)




