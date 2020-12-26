from manimlib.imports import *

class GraphData(GraphScene):
    CONFIG = {
        "labels": ["Mouse", "Rat", "Guinea pig", "Rabbit", "Rabbit"
                   "Rabbit", "Rabbit", "Rabbit", "Rabbit", "Cat", "Macaque",
                   "Dog", "Dog", "Dog", "Dog", "Goat", "Chimpanzee", "Sheep",
                   "Sheep", "Woman", "Woman", "Woman", "Cow", "Cow", "Beef heifers",
                   "Cow"],
        "mass": [0.021, 0.282, 0.410, 2.98, 1.52, 2.46, 3.57, 4.33, 5.33, 3.00, 4.2, 6.6, 14.1, 24.8, 23.6, 36.0, 38.0, 46.4, 46.8, 57.2, 54.8, 57.9, 300, 435, 482, 600],
        "BMR": [3.6, 28.1, 35.1, 167, 83, 119, 164, 191, 233, 152, 207, 288, 534, 875, 872, 800, 1090, 1254, 1330, 1368, 1224, 1320, 4221, 8166, 7754, 7877],
        "y_max": 2000,
        "y_min": 0,
        "x_max": 100,
        "x_min": 0,
        "y_tick_frequency": 500,
        "y_bottom_tick": None,
        "x_tick_frequency": 20,
        "x_axis_width": 8,
        "y_axis_height": 6,
        "x_labeled_nums": np.arange(0, 101, 20),
        "y_labeled_nums": np.arange(0, 2001, 500),
        "x_axis_label": "Mass (kg)",
        "y_axis_label": "Basal Metabolic Rate (kcal/day)",
        "axes_color": LIGHT_GRAY,
        "camera_config": {"background_color": "#2F2F2E"},
        "x_label_background_color": "#2F2F2E",
        "y_label_background_color": "#2F2F2E",
        "x_label_fill_color": LIGHT_GREY,
        "y_label_fill_color": LIGHT_GREY,
        "x_label_scale": 0.75,
        "y_label_scale": 0.75,
        "x_decimal_number_config": {"num_decimal_places": 0, "background_stroke_color": "#2F2F2E", "fill_color": LIGHT_GREY},
        "x_label_num_scale_val": 0.75,
        "y_decimal_number_config": {"num_decimal_places": 0, "background_stroke_color": "#2F2F2E", "fill_color": LIGHT_GREY},
        "y_label_num_scale_val": 0.75,
        "text_config": {"background_stroke_color": "#2F2F2E", "fill_color": WHITE},
        "num_rects": 500,
        "back": r"C:\Manim\manim-26_05_2020\science_animations\blackboard_texture.png",
    }

    def construct(self):
        back = ImageMobject(self.back).scale(4)
        #self.add(back)
        self.graph_origin = 4 * LEFT + 3*DOWN
        self.setup_axes(animate=True)

        data = VGroup()
        for x, y in zip(self.mass, self.BMR):
            d = Dot(self.coords_to_point(x,y), color=WHITE)
            data.add(d)

        self.play(ShowCreation(data), run_time=2.5)

        self.wait(2)

        graph_0 = self.get_graph(lambda x: 71.38 * x**(3/4), color=WHITE, x_min=0.001, x_max=85.1)
        graph_1 = self.get_graph(lambda x: 71.38 * x**(1) if x <= 28.01 else 1987, color=WHITE, x_min=0.001, x_max=85.1)
        graph_2 = DashedVMobject(self.get_graph(lambda x: 71.38 * x**(1), color=WHITE, x_min=0.001, x_max=28.01))
        graph_3 = self.get_graph(lambda x: 71.38 * x**(2/3), color=RED, x_min=0.001, x_max=100)
        surface_law = TextMobject("Square-Cube Law", color=RED).next_to(self.input_to_graph_point(80, graph_3), RIGHT+DOWN)
        area = self.get_area(graph_0, 0, 85.1, graph_1, start_color=WHITE, end_color=LIGHT_GRAY)
        area.set_opacity(0.5)
        efficiency = TextMobject("Extra efficiency").shift(2*UP+0.4*LEFT).scale(0.75)
        surface = TextMobject("$\\text{BMR} = c \cdot \\text{M}^\\frac{2}{3}$", color=RED).next_to(surface_law, DOWN)
        efficiency.add_background_rectangle()
        function = TextMobject("$\\text{BMR} = c \cdot \\text{M}^\\frac{3}{4}$", **self.text_config) \
            .next_to(self.input_to_graph_point(80, graph_0), RIGHT + DOWN)
        linear = TextMobject("$\\text{BMR} = c \cdot \\text{M}$", **self.text_config)\
            .next_to(self.input_to_graph_point(25, graph_1), LEFT)


        self.play(ShowCreation(graph_0))
        self.wait(2)
        self.play(FadeOut(data))
        self.wait(2)
        self.play(Write(function))
        self.wait()
        self.play(Indicate(function))
        self.wait(2)
        self.play(ShowCreation(graph_2))
        self.play(ShowCreation(area), FadeIn(efficiency), Write(linear))
        self.wait(2)
        self.play(Uncreate(graph_2), Uncreate(area), FadeOut(efficiency), FadeOut(linear))
        self.wait(2)
        self.play(ShowCreation(graph_3), Write(surface_law), Write(surface))
        self.wait(2)
        self.play(Uncreate(graph_3), Uncreate(surface_law), Uncreate(surface))



        self.wait(5)


class Trial(GraphScene):
    CONFIG = {
        "y_max": 8500,
        "y_min": 0,
        "x_max": 650,
        "x_min": 0,
        "y_tick_frequency": 1000,
        "y_bottom_tick": None,
        "x_tick_frequency": 100,
        "x_axis_width": 9,
        "y_axis_height": 6,
        "x_labeled_nums": np.arange(0, 650, 100),
        "y_labeled_nums": np.arange(0, 8500, 1000),
        "num_rects": 500,
    }

    def construct(self):
        self.setup_axes(animate=True)
        graph_0 = self.get_graph(lambda x: 70.38*x**(3/4), color=GREEN, x_min=0.001, x_max=650)
        graph_1 = self.get_graph(lambda x: 70.38*x**(1), color=BLUE, x_min=0.001, x_max=650)
        graph_2 = self.get_graph(lambda x: 70.38*x**(2/3), color=YELLOW, x_min=0.001, x_max=650)

        area = self.get_area(graph_1, 0, 650, bounded=graph_0)

        self.play(ShowCreation(graph_0), ShowCreation(graph_1), ShowCreation(graph_2))
        self.play(ShowCreation(area))

        self.wait(2)


class Trial2(Scene):
    CONFIG = {
        "camera_config": {"background_color": WHITE},
        "text_config": {"background_stroke_color": WHITE, "fill_color": BLACK},
    }
    def construct(self):
        #text = TexMobject("BMR = c \\cdot M^{\\frac{3}{4}}")

        #self.play(ShowCreation(text))

        self.wait()


class GraphData2(GraphScene):
    CONFIG = {
        "labels": ["Mouse", "Rat", "Guinea pig", "Rabbit", "Rabbit"
                   "Rabbit", "Rabbit", "Rabbit", "Rabbit", "Cat", "Macaque",
                   "Dog", "Dog", "Dog", "Dog", "Goat", "Chimpanzee", "Sheep",
                   "Sheep", "Woman", "Woman", "Woman", "Cow", "Cow", "Beef heifers",
                   "Cow"],
        "mass": [0.021, 0.282, 0.410, 2.98, 1.52, 2.46, 3.57, 4.33, 5.33, 3.00, 4.2, 6.6, 14.1, 24.8, 23.6, 36.0, 38.0, 46.4, 46.8, 57.2, 54.8, 57.9, 300, 435, 482, 600],
        "BMR": [3.6, 28.1, 35.1, 167, 83, 119, 164, 191, 233, 152, 207, 288, 534, 875, 872, 800, 1090, 1254, 1330, 1368, 1224, 1320, 4221, 8166, 7754, 7877],
        "y_max": 0.0004,
        "y_min": 0,
        "x_max": 10,
        "x_min": 0,
        "y_tick_frequency": 500,
        "y_bottom_tick": None,
        "x_tick_frequency": 20,
        "x_axis_width": 8,
        "y_axis_height": 6,
        "x_labeled_nums": np.arange(0, 10.5, 1),
        "y_labeled_nums": np.arange(0, 0.00045, 0.0002),
        "x_axis_label": "Mass (ng)",
        "y_axis_label": "Basal Metabolic Rate (cal/day)",
        "axes_color": LIGHT_GRAY,
        "camera_config": {"background_color": "#2F2F2E"},
        "x_label_background_color": "#2F2F2E",
        "y_label_background_color": "#2F2F2E",
        "x_label_fill_color": LIGHT_GREY,
        "y_label_fill_color": LIGHT_GREY,
        "x_label_scale": 0.75,
        "y_label_scale": 0.75,
        "x_decimal_number_config": {"num_decimal_places": 0, "background_stroke_color": "#2F2F2E", "fill_color": LIGHT_GREY},
        "x_label_num_scale_val": 0.75,
        "y_decimal_number_config": {"num_decimal_places": 4, "background_stroke_color": "#2F2F2E", "fill_color": LIGHT_GREY},
        "y_label_num_scale_val": 0.5,
        "text_config": {"background_stroke_color": "#2F2F2E", "fill_color": BLACK},
        "num_rects": 500,
        "back": r"C:\Manim\manim-26_05_2020\science_animations\blackboard_texture.png",
    }

    def construct(self):
        back = ImageMobject(self.back).scale(4)
        self.add(back)
        cell = ImageMobject(r"C:\Manim\manim-26_05_2020\science_animations\speech_bubble_1_cell_ver1.png")

        self.graph_origin = 4 * LEFT + 3 * DOWN
        cell.scale(0.75).move_to(self.graph_origin)
        cell.save_state()
        cell.add_to_back()
        self.setup_axes(animate=True)
        self.play(FadeIn(cell))

        graph_0 = self.get_graph(lambda x: 70.38*1000 * (x/(10**12))**(3/4), color=WHITE, x_min = 0.001, x_max = 9)
        graph_0.add_to_back()
        #self.add(graph_0)

        def cell_update(mob, alpha):
            mob.restore()
            mob.scale(interpolate(1,3,alpha))
            mob.move_to(self.input_to_graph_point(interpolate(0.001, 9, alpha), graph_0))

        self.play(ShowCreation(graph_0),
            #UpdateFromAlphaFunc(graph_0, graph_update),
                  UpdateFromAlphaFunc(cell, cell_update), run_time=3)

        self.wait(2)