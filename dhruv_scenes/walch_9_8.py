from manimlib.imports import *
from dhruv_scenes.walch_9_7 import *

class Sinusoid(GraphScene):
    CONFIG = {
        "y_max": 3.5,
        "y_min": -3.5,
        "x_max": 1,
        "x_min": 0,
        "y_tick_frequency": 0.5,
        "y_bottom_tick": None,
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
        im_0 = VGroup()

        self.graph_origin = 5.6 * LEFT
        self.setup_axes(animate=True)
        im_0.add(self.axes)

        phase = 1 / 16
        graph_0 = self.get_graph(sine_wave(2, 3, phase), color=BLACK)
        self.play(ShowCreation(graph_0))
        im_0.add(graph_0)

        label_0 = TextMobject(r"$f(x) = 3 \cdot \sin(2 \cdot 2\pi \cdot (x - \frac{1}{16}))$",
                              **self.text_config).scale(1.3)
        label_0.next_to(self.input_to_graph_point(5 / 8 + phase, graph_0), UP).shift(0)
        self.play(ShowCreation(label_0))
        im_0.add(label_0)

        amp = self.get_vertical_line_to_graph(1 / 8 + phase, graph_0, color=BLACK)
        amp0 = Dot(self.coords_to_point(1 / 8 + phase, 0), color=BLACK)
        amp1 = Dot(self.input_to_graph_point(1 / 8 + phase, graph_0), color=BLACK)
        self.play(ShowCreation(amp), ShowCreation(amp0), ShowCreation(amp1))
        im_0.add(amp)
        im_0.add(amp0)
        im_0.add(amp1)

        amp_brace = BraceText(amp, r"A = 3", RIGHT, **self.text_config, buff=MED_LARGE_BUFF)
        self.play(ShowCreation(amp_brace))
        im_0.add(amp_brace)

        secret_line = Line(self.coords_to_point(phase, -3), self.coords_to_point(0.5 + phase, -3))
        time_brace = BraceText(secret_line, r"Period = $\frac{1}{2}$", DOWN, **self.text_config)
        self.play(ShowCreation(time_brace))
        im_0.add(time_brace)

        secret_line = Line(self.coords_to_point(0, -3), self.coords_to_point(phase, -3))
        phase_brace = BraceText(secret_line, r"$\phi = \frac{1}{16}$", DOWN, **self.text_config)
        self.play(ShowCreation(phase_brace))
        im_0.add(phase_brace)

        self.play(im_0.move_to, ORIGIN)

        self.wait(5)


        self.wait(5)


def xMin(ph, pe):
    if ph >= 0:
        return 0
    else:
        return -pe/2

def xLabels(ph, pe, n):
    if ph >= 0:
        return np.arange(0, n*pe + ph + 0.001, n*pe/4)
    else:
        min = -(-ph - np.mod(-ph, n*pe/4)+pe/4)
        return np.arange(min, n*pe + 0.001, n*pe/4)


class SingleSinusoid(GraphScene):
    '''to edit:'''
    amplitude = 1
    amp_text = str(amplitude)
    # amp_text = r""
    omega = PI
    omega_text = r"600\pi"
    phase = 1/2
    phase_text = r"\frac{1}{600}"
    period = 2 * PI / omega
    period_text = r"\frac{1}{300}"
    labelling = False
    details = False

    if omega == 1 and phase == 0:
        label_text = r"$f(t) = " + amp_text + r"\cdot \sin(t)$"
    elif omega == 1 and phase !=0:
        label_text = r"$f(t) = " + amp_text + r" \cdot \sin(t - " + phase_text + ")$"
    elif omega != 1 and phase == 0:
        label_text = r"$f(t) = " + amp_text + r" \cdot \sin(" + omega_text + "\cdot t)$"
    else:
        label_text = r"$f(t) = " + amp_text + r" \cdot \sin(" + omega_text + "\cdot (t" + phase_text + "))$"


    CONFIG = {
        "y_max": amplitude*1.5,
        "y_min": -amplitude*1.5,
        "x_max": 2*period,
        "x_min": xMin(phase, period),
        "y_tick_frequency": 0.5 if -4 <= amplitude <= 4 else 1,
        "y_bottom_tick": - (amplitude*1.5 - np.mod(amplitude*1.5, 0.5)) if -4 <= amplitude <= 4 else - (amplitude*1.5 - np.mod(amplitude*1.5, 1)),
        "x_tick_frequency": 2*period/8,
        "x_axis_width": 12,
        "y_axis_height": 7,
        "x_labeled_nums": xLabels(phase, period, 2),
        "y_labeled_nums": np.arange(np.floor(-amplitude*1.5)+1, np.ceil(amplitude*1.5), 1),
        "x_axis_label": "$t$",
        "y_axis_label": "$p$",
        "axes_color": BLACK,
        "camera_config": {"background_color": WHITE},
        "background_rectangle_opacity": 0.85,
        "background_rectangle_color":WHITE,
        "x_label_background_color": WHITE,
        "y_label_background_color": WHITE,
        "x_label_fill_color": BLACK,
        "y_label_fill_color": BLACK,
        "x_label_scale": 1,
        "y_label_scale": 1,
        "x_decimal_number_config": {"num_decimal_places": 4, "background_stroke_color": WHITE, "fill_color": BLACK},
        "x_label_num_scale_val": 1,
        "y_decimal_number_config": {"num_decimal_places": 1, "background_stroke_color": WHITE, "fill_color": BLACK},
        "y_label_num_scale_val": 1,
        "text_config": {"background_stroke_color": WHITE, "fill_color": BLACK}
    }

    def construct(self):
        im_0 = VGroup()

        self.graph_origin = 5.6 * LEFT
        self.setup_axes(animate=True)
        self.add_foreground_mobject(self.axes)

        im_0.add(self.axes)

        graph_0 = self.get_graph(sine_wave(self.omega/(2*PI), self.amplitude, self.phase), color=BLACK)
        #graph_0 = self.get_graph(lambda x: sine_wave(262, 1)(x) +sine_wave(278.4, 1)(x), color=BLACK)
        self.play(ShowCreation(graph_0))
        im_0.add(graph_0)

        if self.labelling:
            label_0 = TextMobject(self.label_text, **self.text_config).scale(1.1)
            #label_0 = TextMobject(r"$f(t) = sin(262 \cdot 2\pi \cdot t) + sin(278.4 \cdot 2\pi \cdot t)$", **self.text_config).scale(1)
            label_0.next_to(self.graph_origin, RIGHT).shift(3*UP + 2*RIGHT)
            label_0 = VGroup(BackgroundRectangle(label_0, color=WHITE), label_0)
            self.add_foreground_mobject(label_0)
            self.play(ShowCreation(label_0))
            im_0.add(label_0)

        if self.details:
            amp = self.get_vertical_line_to_graph(self.period/4 + self.phase, graph_0, color=BLACK)
            amp0 = Dot(self.coords_to_point(self.period/4 + self.phase,0), color=BLACK)
            amp1 = Dot(self.input_to_graph_point(self.period/4 + self.phase, graph_0), color=BLACK)
            self.play(ShowCreation(amp), ShowCreation(amp0), ShowCreation(amp1))
            im_0.add(amp)
            im_0.add(amp0)
            im_0.add(amp1)
            amp_brace = BraceText(amp, r"$A = " + self.amp_text + r"$", RIGHT, **self.text_config, buff=MED_LARGE_BUFF)
            amp_brace = VGroup(BackgroundRectangle(amp_brace.brace, color=WHITE),
                               BackgroundRectangle(amp_brace.label, color=WHITE), amp_brace)
            self.add_foreground_mobject(amp_brace)
            self.play(ShowCreation(amp_brace))
            im_0.add(amp_brace)

            secret_line = Line(self.coords_to_point(self.phase,-0.5*self.amplitude), self.coords_to_point(self.period + self.phase,-0.5*self.amplitude))
            time_brace = BraceText(secret_line, r"$\frac{2\pi}{\omega} = " + self.period_text + "$", DOWN, **self.text_config)
            time_brace = VGroup(BackgroundRectangle(time_brace.brace, color=WHITE),
                                BackgroundRectangle(time_brace.label, color=WHITE), time_brace)
            self.add_foreground_mobject(time_brace)
            self.play(ShowCreation(time_brace))
            im_0.add(time_brace)

            if self.phase !=0:
                if self.phase > 0:
                    secret_line = Line(self.coords_to_point(0,0.7*self.amplitude), self.coords_to_point(self.phase,0.7*self.amplitude))
                    phase_brace = BraceText(secret_line, r"$\phi = " + self.phase_text + "$", UP, **self.text_config)
                else:
                    secret_line = Line(self.coords_to_point(0,-0.7*self.amplitude), self.coords_to_point(self.phase,-0.7*self.amplitude))
                    phase_brace = BraceText(secret_line, r"$\phi = " + self.phase_text + "$", DOWN, **self.text_config)

                #phase_brace.label.scale(0.8).shift(0.6*RIGHT+0.2*DOWN)
                phase_brace = VGroup(BackgroundRectangle(phase_brace.brace, color=WHITE),
                                     BackgroundRectangle(phase_brace.label, color=WHITE), phase_brace)
                self.add_foreground_mobject(phase_brace)
                self.play(ShowCreation(phase_brace))
                im_0.add(phase_brace)


        self.play(im_0.move_to, ORIGIN)
        #self.play(im_0.scale, 0.5)

        self.wait(5)



class SummedSinusoid(GraphScene):
    '''to edit:'''
    amplitude = [1, 1, 1]
    omega = [262*2*PI, 329*2*PI, 393*2*PI]
    phase = [0,0,0]

    period = [2 * PI / om for om in omega]
    max_period = max(period)
    n = len(amplitude)
    max_amp = sum(amplitude)
    min_omega = min(omega)
    max_phase = max(phase)

    CONFIG = {
        "y_max": max_amp*1.5,
        "y_min": -max_amp*1.5,
        "x_max": 4*max_period,
        "x_min": xMin(max_phase, max_period),
        "y_tick_frequency": 0.5 if -4 <= max_amp <= 4 else 1,
        "y_bottom_tick": - (max_amp*1.5 - np.mod(max_amp*1.5, 0.5)) if -4 <= max_amp <= 4 else - (max_amp*1.5 - np.mod(max_amp*1.5, 1)),
        "x_tick_frequency": 4*max_period/8,
        "x_axis_width": 12,
        "y_axis_height": 7,
        "x_labeled_nums": xLabels(max_phase, max_period, 4),
        "y_labeled_nums": np.arange(np.floor(-max_amp*1.5)+1, np.ceil(max_amp*1.5), 1),
        "x_axis_label": "$t$",
        "y_axis_label": "$p$",
        "axes_color": BLACK,
        "camera_config": {"background_color": WHITE},
        "background_rectangle_opacity": 0.85,
        "background_rectangle_color": WHITE,
        "x_label_background_color": WHITE,
        "y_label_background_color": WHITE,
        "x_label_fill_color": BLACK,
        "y_label_fill_color": BLACK,
        "x_label_scale": 1,
        "y_label_scale": 1,
        "x_decimal_number_config": {"num_decimal_places": 3, "background_stroke_color": WHITE, "fill_color": BLACK},
        "x_label_num_scale_val": 1,
        "y_decimal_number_config": {"num_decimal_places": 1, "background_stroke_color": WHITE, "fill_color": BLACK},
        "y_label_num_scale_val": 1,
        "text_config": {"background_stroke_color": WHITE, "fill_color": BLACK}
    }

    def construct(self):
        im_0 = VGroup()

        self.graph_origin = 5.6 * LEFT
        self.setup_axes(animate=True)
        self.add_foreground_mobject(self.axes)

        im_0.add(self.axes)

        functions = [sine_wave(self.omega[i]/(2*PI), self.amplitude[i], self.phase[i]) for i in range(self.n)]
        func = lambda x: sum([functions[i](x) for i in range(self.n)])
        graph_0 = self.get_graph(func, color=BLACK)
        self.play(ShowCreation(graph_0))
        im_0.add(graph_0)

        self.play(im_0.move_to, ORIGIN)

        self.wait(5)


class ManySinusoid(GraphScene):
    '''to edit:'''
    amplitude = [1, 1]
    omega = [1, 1]
    phase = [0, PI]

    period = [2 * PI / om for om in omega]
    max_period = max(period)
    n = len(amplitude)
    max_amp = max(amplitude)
    min_omega = min(omega)
    min_phase = min(phase)

    CONFIG = {
        "y_max": max_amp*1.5,
        "y_min": -max_amp*1.5,
        "x_max": 2*max_period,
        "x_min": xMin(min_phase, max_period),
        "y_tick_frequency": 0.5 if -4 <= max_amp <= 4 else 1,
        "y_bottom_tick": - (max_amp*1.5 - np.mod(max_amp*1.5, 0.5)) if -4 <= max_amp <= 4 else - (max_amp*1.5 - np.mod(max_amp*1.5, 1)),
        "x_tick_frequency": 2*max_period/8,
        "x_axis_width": 12,
        "y_axis_height": 7,
        "x_labeled_nums": xLabels(min_phase, max_period, 2),
        "y_labeled_nums": np.arange(np.floor(-max_amp*1.5)+1, np.ceil(max_amp*1.5), 1),
        "x_axis_label": "$t$",
        "y_axis_label": "$p$",
        "axes_color": BLACK,
        "camera_config": {"background_color": WHITE},
        "background_rectangle_opacity": 0.85,
        "background_rectangle_color": WHITE,
        "x_label_background_color": WHITE,
        "y_label_background_color": WHITE,
        "x_label_fill_color": BLACK,
        "y_label_fill_color": BLACK,
        "x_label_scale": 1,
        "y_label_scale": 1,
        "x_decimal_number_config": {"num_decimal_places": 3, "background_stroke_color": WHITE, "fill_color": BLACK},
        "x_label_num_scale_val": 1,
        "y_decimal_number_config": {"num_decimal_places": 1, "background_stroke_color": WHITE, "fill_color": BLACK},
        "y_label_num_scale_val": 1,
        "text_config": {"background_stroke_color": WHITE, "fill_color": BLACK}
    }

    def construct(self):
        im_0 = VGroup()

        self.graph_origin = 5.6 * LEFT
        self.setup_axes(animate=True)
        self.add_foreground_mobject(self.axes)

        im_0.add(self.axes)

        functions = [sine_wave(self.omega[i]/(2*PI), self.amplitude[i], self.phase[i]) for i in range(self.n)]
        graphs = [self.get_graph(functions[i], color=BLACK) for i in range(self.n)]
        if self.n == 2:
            graphs[1] = DashedVMobject(graphs[1], num_dashes=60)
        elif self.n == 3:
            graphs[1] = DashedVMobject(graphs[1], num_dashes=60)
            graphs[2] = DashedVMobject(graphs[1], num_dashes=120)

        self.play(*[ShowCreation(graph) for graph in graphs])
        im_0.add(*graphs)

        self.play(im_0.move_to, ORIGIN)


        self.wait(5)


class BeatingSinusoid(GraphScene):
    '''to edit:'''
    amplitude = [1, 1]
    omega = [262 * 2 * PI, 524 * 2 * PI]
    phase = [0, 0]

    period = [2 * PI / om for om in omega]
    frequency = [om/(2*PI) for om in omega]
    beat_freq = max(frequency) - min(frequency)
    beat_period = 1/beat_freq
    max_period = max(period)
    n = len(amplitude)
    max_amp = sum(amplitude)
    min_omega = min(omega)
    max_phase = max(phase)

    CONFIG = {
        "y_max": max_amp*1.5,
        "y_min": -max_amp*1.5,
        "x_max": 4*beat_period,
        "x_min": xMin(0, beat_period),
        "y_tick_frequency": 0.5 if -4 <= max_amp <= 4 else 1,
        "y_bottom_tick": - (max_amp * 1.5 - np.mod(max_amp * 1.5, 0.5)) if -4 <= max_amp <= 4 else - (
                    max_amp * 1.5 - np.mod(max_amp * 1.5, 1)),
        "x_tick_frequency": 4*beat_period/8,
        "x_axis_width": 12,
        "y_axis_height": 7,
        "x_labeled_nums": xLabels(0, beat_period, 4),
        "y_labeled_nums": np.arange(np.floor(-max_amp*1.5)+1, np.ceil(max_amp*1.5), 1),
        "x_axis_label": "$t$",
        "y_axis_label": "$p$",
        "axes_color": BLACK,
        "camera_config": {"background_color": WHITE},
        "background_rectangle_opacity": 0.85,
        "background_rectangle_color": WHITE,
        "x_label_background_color": WHITE,
        "y_label_background_color": WHITE,
        "x_label_fill_color": BLACK,
        "y_label_fill_color": BLACK,
        "x_label_scale": 1,
        "y_label_scale": 1,
        "x_decimal_number_config": {"num_decimal_places": 3, "background_stroke_color": WHITE, "fill_color": BLACK},
        "x_label_num_scale_val": 1,
        "y_decimal_number_config": {"num_decimal_places": 1, "background_stroke_color": WHITE, "fill_color": BLACK},
        "y_label_num_scale_val": 1,
        "text_config": {"background_stroke_color": WHITE, "fill_color": BLACK}
    }

    def construct(self):
        im_0 = VGroup()

        self.graph_origin = 5.6 * LEFT
        self.setup_axes(animate=True)
        self.add_foreground_mobject(self.axes)
        im_0.add(self.axes)

        functions = [sine_wave(self.omega[i]/(2*PI), self.amplitude[i], self.phase[i]) for i in range(self.n)]
        func = lambda x: sum([functions[i](x) for i in range(self.n)])
        graph_0 = self.get_graph(func, color=BLACK, step_size=0.001)
        self.play(ShowCreation(graph_0))
        im_0.add(graph_0)

        self.play(im_0.move_to, ORIGIN)

        self.wait(5)