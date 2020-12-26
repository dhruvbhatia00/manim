from manimlib.imports import *


class SoundWaves1(GraphScene):
    CONFIG = {
        "y_max" : 2.5,
        "y_min" : -2.5,
        "x_max" : 0.005,
        "x_min" : 0,
        "y_tick_frequency" : 0.5,
        "x_tick_frequency" : 0.001,
        "x_axis_width": 5.5,
        "y_axis_height": 3,
        "x_labeled_nums": [0, 0.001, 0.002, 0.003, 0.004, 0.005],
        "y_labeled_nums": np.arange(-2, 2.5, 0.5),
        "x_axis_label":"$t$",
        "y_axis_label":"$p$",
        "axes_color" : GRAY,
        "camera_config": {"background_color": WHITE},
        "x_label_background_color":WHITE,
        "y_label_background_color":WHITE,
        "x_label_fill_color": GREY,
        "y_label_fill_color": GREY,
        "x_label_scale": 0.7,
        "y_label_scale": 0.7,
        "x_decimal_number_config": {"num_decimal_places": 3, "background_stroke_color":WHITE, "fill_color": GREY},
        "x_label_num_scale_val": 0.6,
        "y_decimal_number_config": {"num_decimal_places": 1, "background_stroke_color": WHITE, "fill_color": GREY},
        "y_label_num_scale_val": 0.54,
        "text_config": {"background_stroke_color":WHITE, "fill_color": DARK_BLUE}
    }

    def construct(self):
        self.graph_origin = 2*UP + 6.2*LEFT + 0.25 * DOWN
        self.setup_axes(animate=True)
        graph_up_left = self.get_graph(sine_wave(262, 1), color=DARK_BLUE)
        up_left_label = TextMobject(r"Pure C$_4$: $1 \cdot \sin(262 \cdot 2\pi \cdot t)$", **self.text_config).scale(0.65)
        up_left_label.move_to(self.graph_origin + 1.2 * UP + 2.75*RIGHT)

        self.graph_origin = -2*UP + 6.2*LEFT + 0.25 * DOWN
        self.setup_axes(animate=True)
        graph_down_left = self.get_graph(sine_wave(330, 1), color=DARK_BLUE)
        down_left_label = TextMobject(r"Pure E$_4$: $1 \cdot \sin(330 \cdot 2\pi \cdot t)$", **self.text_config).scale(0.65)
        down_left_label.move_to(self.graph_origin + 1.2 * UP + 2.75 * RIGHT)

        self.graph_origin = 2 * UP + RIGHT + 0.25 * DOWN
        self.setup_axes(animate=True)
        graph_up_right = self.get_graph(sine_wave(392, 1), color=DARK_BLUE)
        up_right_label = TextMobject(r"Pure G$_4$: $1 \cdot \sin(392 \cdot 2\pi \cdot t)$", **self.text_config).scale(0.65)
        up_right_label.move_to(self.graph_origin + 1.2 * UP + 2.75 * RIGHT)

        self.graph_origin = -2 * UP + RIGHT + 0.25 * DOWN
        self.setup_axes(animate=True)
        graph_down_right = self.get_graph(sine_wave(524, 1), color=DARK_BLUE)
        down_right_label = TextMobject(r"Pure C$_5$: $1 \cdot \sin(524 \cdot 2\pi \cdot t)$", **self.text_config).scale(0.65)
        down_right_label.move_to(self.graph_origin + 1.2 * UP + 2.75 * RIGHT)

        t_key = TextMobject(r"$t = $ time (s)", background_stroke_color=WHITE, fill_color=GREY).scale(0.65)
        p_key = TextMobject(r"$p = $ air pressure", background_stroke_color=WHITE, fill_color=GREY).scale(0.65)
        legend = VGroup(t_key, p_key).arrange(RIGHT, buff=LARGE_BUFF).shift(0.2* DOWN + 0.75* RIGHT)

        graphs = VGroup(graph_up_left, graph_down_left, graph_up_right, graph_down_right)
        labels = VGroup(up_left_label, down_left_label, up_right_label, down_right_label)


        self.play(FadeIn(graphs), FadeIn(labels), FadeIn(legend))
        self.wait(5)

def sine_wave(f, a, phi=0):
    return lambda x: a * math.sin(f * 2 * PI * (x - phi))

class SoundWaves2(GraphScene):
    CONFIG = {
        "y_max": 2.5,
        "y_min": -2.5,
        "x_max": 0.01,
        "x_min": 0,
        "y_tick_frequency": 0.5,
        "x_tick_frequency": 0.001,
        "x_axis_width": 10,
        "y_axis_height": 2,
        "x_labeled_nums": np.arange(0, 0.01, 0.002),
        "y_labeled_nums": np.arange(-2, 2.5, 1),
        "x_axis_label": "$t$",
        "y_axis_label": "$p$",
        "axes_color": GRAY,
        "camera_config": {"background_color": WHITE},
        "x_label_background_color": WHITE,
        "y_label_background_color": WHITE,
        "x_label_fill_color": GREY,
        "y_label_fill_color": GREY,
        "x_label_scale": 0.7,
        "y_label_scale": 0.7,
        "x_decimal_number_config": {"num_decimal_places": 3, "background_stroke_color": WHITE, "fill_color": GREY},
        "x_label_num_scale_val": 0.6,
        "y_decimal_number_config": {"num_decimal_places": 1, "background_stroke_color": WHITE, "fill_color": GREY},
        "y_label_num_scale_val": 0.5,
        "text_config": {"background_stroke_color": WHITE, "fill_color": BLACK}
    }

    def piano_c(self, x):
        out = 0
        for i in range(1, 10):
            out += sine_wave(262 * i, math.exp(-0.5 * (i - 1)))(x)
        return out

    def construct(self):
        self.graph_origin = 2.6 * UP + 5.6 * LEFT + 0.25 * DOWN
        self.setup_axes(animate=True)
        graph_0 = self.get_graph(self.piano_c, color=BLACK)
        label_0 = TextMobject(r"Piano C$_4$", **self.text_config).scale(
            0.65)
        label_0.move_to(self.graph_origin + 1 * UP + 5 * RIGHT)
        im_0 = VGroup(self.axes, graph_0, label_0)
        eq = TextMobject(r"$=$", **self.text_config).scale(1.7)
        eq.next_to(im_0, RIGHT, buff=MED_SMALL_BUFF)
        fig_0 = VGroup(im_0, eq)
        self.play(FadeIn(fig_0))

        harmonics = ["C$_4$", "C$_5$", "G$_5$", "C$_6$", "E$_6$", "G$_6$", "B$\\flat_6$", "C$_7$", "D$_7$"]
        freqs = list(map(lambda i: str(i) + "\\cdot 262", range(1, 10)))
        amps = list(map(lambda i: str(round(math.exp(-0.5 * (i-1)), 2)), range(1, 10)))

        figs = VGroup()
        num_graphs = 4

        for i in range(1, num_graphs + 1):
            j = 10 - i
            if i == num_graphs:
                fig = TextMobject(r"$ + \cdots$", **self.text_config).scale(1.7 * j/10).move_to(self.graph_origin + j/10 * 1.5 * DOWN + j/10 * RIGHT + j/10 * 5 * RIGHT)
            else:
                self.graph_origin = self.graph_origin + j/10 * 2.1 * DOWN + j/10 * RIGHT
                self.setup_axes(animate=True)
                plus = TextMobject(r"$+$", **self.text_config).scale(2)
                if i == 1:
                    plus.set_color(WHITE)
                graph = self.get_graph(sine_wave(i*262, math.exp(-0.5 * (i - 1))), color=BLACK)
                label_tex = "Pure " + harmonics[i-1] + ": $" + amps[i-1] + " \\cdot \\sin(" + freqs[i-1] + " \\cdot 2\\pi \\cdot t)$"
                label = TextMobject(label_tex, **self.text_config).scale(0.65)
                label.move_to(self.graph_origin + 1 * UP + 5 * RIGHT)
                im = VGroup(self.axes, graph, label)
                plus.next_to(im, LEFT, buff=MED_SMALL_BUFF)
                fig = VGroup(plus, im)
                fig.scale(j/10)
                figs.add(fig)

            self.play(FadeIn(fig))



        self.wait(5)

def manageable(limit, val):
    if val <= limit:
        return val
    else:
        return manageable(limit, val/2)

class HarmonicSeries(Scene):
    CONFIG = {
        "text_config": {"background_stroke_color": WHITE, "fill_color": DARK_BLUE},
        "camera_config": {"background_color": WHITE},
    }
    def construct(self):
        table_dict ={
            TextMobject("Position", **self.text_config): list(map(str, range(1, 21))),
            TextMobject("Frequency", **self.text_config): list(map(lambda i: str(i*262), range(1, 21))),
            TextMobject("Note", **self.text_config):
                ["C$_4$", "C$_5$", "G$_5$", "C$_6$", "E$_6$", "G$_6$", "B$\\flat_6$", "C$_7$", "D$_7$",
                 "E$_7$", "F$\\sharp_7$", "G$_7$", "A$\\flat_7$", "B$\\flat_7$", "B$_7$", "C$_8$",
                 "C$\\sharp_8$", "D$_8$", "D$\\sharp_8$", "E$_8$"],
            TextMobject("Manageable Frequency", **self.text_config): list(map(lambda val: str(round(manageable(2*262, val))),
                                                                              list(map(lambda i: i*262, range(1, 21)))))
        }

        table = Table(tabledict=table_dict, buff_length=0.3, line_color=GRAY, raw_string_color=DARK_BLUE).scale(0.35)

        self.play(ShowCreation(table))
        self.wait(5)

class SoundWaves4(GraphScene):
    CONFIG = {
        "y_max": 4,
        "y_min": -4,
        "x_max": 0.01,
        "x_min": 0,
        "y_tick_frequency": 1,
        "x_tick_frequency": 0.001,
        "x_axis_width": 10,
        "y_axis_height": 4,
        "x_labeled_nums": np.arange(0, 0.01, 0.002),
        "y_labeled_nums": np.arange(-4, 4.5, 1),
        "x_axis_label": "$t$",
        "y_axis_label": "$p$",
        "axes_color": GRAY,
        "camera_config": {"background_color": WHITE},
        "x_label_background_color": WHITE,
        "y_label_background_color": WHITE,
        "x_label_fill_color": GREY,
        "y_label_fill_color": GREY,
        "x_label_scale": 0.7,
        "y_label_scale": 0.7,
        "x_decimal_number_config": {"num_decimal_places": 3, "background_stroke_color": WHITE, "fill_color": GREY},
        "x_label_num_scale_val": 0.6,
        "y_decimal_number_config": {"num_decimal_places": 1, "background_stroke_color": WHITE, "fill_color": GREY},
        "y_label_num_scale_val": 0.5,
        "text_config": {"background_stroke_color": WHITE, "fill_color": DARK_BLUE}
    }

    def combine_harmonics(self, amp_func, x):
        out = 0
        for i in range(1, 10):
            out += sine_wave(262 * i, amp_func(i), 0)(x)
        return out

    def construct(self):
        self.graph_origin = 5.6 * LEFT
        self.setup_axes(animate=True)
        graph_0 = self.get_graph(lambda x: self.combine_harmonics(lambda i: 1 - i/10, x), color=DARK_BLUE)
        label_0 = TextMobject(r"$\sum_{i=0}^{10} (1 - \frac{i}{10}) \cdot \sin(i \cdot 262 \cdot 2\pi \cdot t))$", **self.text_config).scale(1)
        label_0.move_to(self.graph_origin + 2 * UP + 5 * RIGHT)
        im_0 = VGroup(self.axes, graph_0, label_0)
        self.play(FadeIn(im_0.move_to(ORIGIN)))


        self.wait(5)


class SoundWaves5(GraphScene):
    CONFIG = {
        "y_max" : 3,
        "y_min" : -3,
        "x_max" : 0.1,
        "x_min" : 0,
        "y_tick_frequency" : 0.5,
        "x_tick_frequency" : 0.01,
        "x_axis_width": 9,
        "y_axis_height": 4,
        "x_labeled_nums": np.arange(0, 0.105, 0.02),
        "y_labeled_nums": np.arange(-3, 3.5, 1),
        "x_axis_label":"$t$",
        "y_axis_label":"$p$",
        "axes_color" : GRAY,
        "camera_config": {"background_color": WHITE},
        "x_label_background_color":WHITE,
        "y_label_background_color":WHITE,
        "x_label_fill_color": GREY,
        "y_label_fill_color": GREY,
        "x_label_scale": 1,
        "y_label_scale": 0.8,
        "x_decimal_number_config": {"num_decimal_places": 2, "background_stroke_color":WHITE, "fill_color": GREY},
        "x_label_num_scale_val": 1,
        "y_decimal_number_config": {"num_decimal_places": 1, "background_stroke_color": WHITE, "fill_color": GREY},
        "y_label_num_scale_val": 1,
        "text_config": {"background_stroke_color":WHITE, "fill_color": DARK_BLUE}
    }

    def construct(self):
        self.graph_origin = 5.6 * LEFT
        self.setup_axes(animate=True)
        graph_0 = self.get_graph(lambda x: sine_wave(262, 1)(x) + sine_wave(278, 1)(x), color=DARK_BLUE, step_size=0.01)
        label_0 = TextMobject(r"$\sin(262 \cdot 2\pi \cdot t) + \sin(278 \cdot 2\pi \cdot t)$", **self.text_config).scale(0.9)
        label_0.move_to(self.graph_origin + 1.75 * UP + 4.5 * RIGHT)
        im_0 = VGroup(self.axes, graph_0, label_0)
        self.play(FadeIn(im_0.move_to(ORIGIN)))


        self.wait(5)

class SoundWaves6(GraphScene):
    CONFIG = {
        "y_max" : 4,
        "y_min" : -4,
        "x_max" : 0.025,
        "x_min" : 0,
        "y_tick_frequency" : 0.5,
        "x_tick_frequency" : 0.25,
        "x_axis_width": 9,
        "y_axis_height": 4,
        "x_labeled_nums": np.arange(0, 0.026, 0.005),
        "y_labeled_nums": np.arange(-3, 3.5, 1),
        "x_axis_label":"$t$",
        "y_axis_label":"$p$",
        "axes_color" : GRAY,
        "camera_config": {"background_color": WHITE},
        "x_label_background_color":WHITE,
        "y_label_background_color":WHITE,
        "x_label_fill_color": GREY,
        "y_label_fill_color": GREY,
        "x_label_scale": 1,
        "y_label_scale": 0.8,
        "x_decimal_number_config": {"num_decimal_places": 3, "background_stroke_color":WHITE, "fill_color": GREY},
        "x_label_num_scale_val": 1,
        "y_decimal_number_config": {"num_decimal_places": 1, "background_stroke_color": WHITE, "fill_color": GREY},
        "y_label_num_scale_val": 1,
        "text_config": {"background_stroke_color":WHITE, "fill_color": DARK_BLUE}
    }

    def construct(self):
        self.graph_origin = 5.6 * LEFT
        self.setup_axes(animate=True)
        graph_0 = self.get_graph(lambda x: sine_wave(262, 1)(x) + sine_wave(330, 1)(x) + sine_wave(392, 1)(x), color=DARK_BLUE)
        label_0 = TextMobject(r"$\sin(262 \cdot 2\pi \cdot t) + \sin(330 \cdot 2\pi \cdot t) + \sin(392 \cdot 2\pi \cdot t)$", **self.text_config).scale(0.85)
        label_0.move_to(self.graph_origin + 2 * UP + 5.5 * RIGHT)
        im_0 = VGroup(self.axes, graph_0, label_0)
        self.play(FadeIn(im_0.move_to(ORIGIN)))


        self.wait(5)


class Blah(Scene):
    CONFIG = {
        "camera_config": {"background_color": WHITE},
        "number_plane_style": {
            "center_point": ORIGIN,
            "axis_config": {
                "stroke_color": BLACK,
                "stroke_opacity":0.5,
                "stroke_width": 4,
                "include_ticks": False,
                "include_numbers": True,
                "include_tip": True,
                "line_to_number_buff": SMALL_BUFF,
                "label_direction": DR,
                "number_scale_val": 0.5,
                "decimal_number_config": {
                    "num_decimal_places": 0,
                    "stroke_color": WHITE,
                    "fill_color": BLACK
                }
            },
            "y_axis_config": {
                "label_direction": DR,
            },
            "background_line_style": {
                "stroke_color": BLACK,
                "stroke_width": 2,
                "stroke_opacity": 0.8,
            },
            # Defaults to a faded version of line_config
            "faded_line_style": {
                "stroke_color": BLACK,
                "stroke_width": 2,
                "stroke_opacity": 0.2,
            },
            "x_line_frequency": 1,
            "y_line_frequency": 1,
            "faded_line_ratio": 1,
            "make_smooth_after_applying_functions": True,
        }
    }

    def construct(self):

        plane = NumberPlane(**self.number_plane_style)
        self.play(ShowCreation(plane))

        A = Polygon(ORIGIN, 3*RIGHT, 2*RIGHT + 2*UP, color=BLACK, stroke_width=6, fill_color=LIGHT_GREY, fill_opacity=0.4)
        B = A.copy().scale_about_point(-1.5, ORIGIN)
        A_label = TextMobject(r"A", stroke_color=WHITE, fill_color=BLACK).move_to(A.get_center()).shift(0.3*DOWN)
        B_label = TextMobject(r"B", stroke_color=WHITE, fill_color=BLACK).move_to(B.get_center()).shift(0.3*UP + 0.3*LEFT)

        self.play(ShowCreation(A),ShowCreation(A_label), ShowCreation(B), ShowCreation(B_label))



        self.wait(5)


class Sinusoid(GraphScene):
    CONFIG = {
        "y_max": 3.5,
        "y_min": -3.5,
        "x_max": 1,
        "x_min": 0,
        "y_tick_frequency": 0.5,
        "x_tick_frequency": 1/8,
        "x_axis_width": 9,
        "y_axis_height": 6,
        "x_labeled_nums": np.arange(0, 1.25, 0.25),
        "y_labeled_nums": np.arange(-3, 4, 1),
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        "axes_color": GRAY,
        "camera_config": {"background_color": WHITE},
        "x_label_background_color": WHITE,
        "y_label_background_color": WHITE,
        "x_label_fill_color": GREY,
        "y_label_fill_color": GREY,
        "x_label_scale": 1,
        "y_label_scale": 1,
        "x_decimal_number_config": {"num_decimal_places": 2, "background_stroke_color": WHITE, "fill_color": GREY},
        "x_label_num_scale_val": 1,
        "y_decimal_number_config": {"num_decimal_places": 1, "background_stroke_color": WHITE, "fill_color": GREY},
        "y_label_num_scale_val": 1,
        "text_config": {"background_stroke_color": WHITE, "fill_color": BLACK}
    }

    def construct(self):
        self.graph_origin = 5.6 * LEFT
        self.setup_axes(animate=True)
        phase = 1/16
        graph_0 = self.get_graph(sine_wave(2, 3, phase), color=BLACK)
        self.play(ShowCreation(graph_0))

        label_0 = TextMobject(r"$f(x) = 3 \cdot \sin(2 \cdot 2\pi \cdot (x - \frac{1}{16}))$", **self.text_config).scale(1.3)
        label_0.next_to(self.input_to_graph_point(5/8 + phase, graph_0), UP).shift(0)
        self.play(ShowCreation(label_0))

        amp = self.get_vertical_line_to_graph(1/8 + phase, graph_0, color=BLACK)
        amp0 = Dot(self.coords_to_point(1/8 + phase,0), color=BLACK)
        amp1 = Dot(self.input_to_graph_point(1/8 + phase, graph_0), color=BLACK)
        self.play(ShowCreation(amp), ShowCreation(amp0), ShowCreation(amp1))

        amp_brace = BraceText(amp, r"A = 3", RIGHT, **self.text_config, buff=MED_LARGE_BUFF)
        self.play(ShowCreation(amp_brace))

        secret_line = Line(self.coords_to_point(phase,-3), self.coords_to_point(0.5 + phase,-3))
        time_brace = BraceText(secret_line, r"Period = $\frac{1}{2}$", DOWN, **self.text_config)
        self.play(ShowCreation(time_brace))

        secret_line = Line(self.coords_to_point(0,-3), self.coords_to_point(phase,-3))
        phase_brace = BraceText(secret_line, r"$\phi = \frac{1}{16}$", DOWN, **self.text_config)
        self.play(ShowCreation(phase_brace))



        im_0 = VGroup(self.axes, graph_0, label_0, amp, amp0, amp1, amp_brace, time_brace, phase_brace)
        self.play(im_0.move_to, ORIGIN)


        self.wait(5)

