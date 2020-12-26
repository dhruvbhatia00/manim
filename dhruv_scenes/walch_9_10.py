from manimlib.imports import *


class GraphFunc(GraphScene):

    CONFIG = {
        "func": lambda x: x,
        "func_kwargs": {"color": BLACK, "x_min": 0, "x_max": 5},

        "y_max": 20,
        "y_min": 0,
        "x_max": 5,
        "x_min": 0,
        "y_tick_frequency": 1,
        "y_bottom_tick": None,
        "x_tick_frequency": 1/8,
        "x_axis_width": 11,
        "y_axis_height": 6.5,
        "x_labeled_nums": np.arange(0,5.5, 1),
        "y_labeled_nums": np.arange(0, 21, 5),
        "x_axis_label": "$x$",
        "y_axis_label": "length",
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
        im = VGroup()

        self.graph_origin = 5 * LEFT + 4 * DOWN
        self.setup_axes(animate= True)
        im.add(self.axes)

        graph = self.get_graph(self.func, **self.func_kwargs)
        self.play(ShowCreation(graph))
        im.add(graph)


        self.play(im.move_to, ORIGIN)
        self.wait(5)


def hyp_func(x): return 1.5 * x
def real_func(x): return 1.5 * x**(2/3)

class Graph2Func(GraphScene):

    minimum = 0
    maximum = 300
    n = 10
    data = list(map(lambda x: [x, real_func(x) + np.random.normal(0,9,1)], np.linspace(minimum, maximum, n+1)))


    CONFIG = {
        "hyp_func": hyp_func,
        "hyp_func_kwargs": {"color": BLACK, "x_min": 0, "x_max": 200/1.5},
        "real_func": real_func,
        "real_func_kwargs": {"color": BLACK, "x_min": minimum, "x_max": maximum},
        "data": data,

        "y_max": 200,
        "y_min": 0,
        "x_max": maximum,
        "x_min": minimum,
        "y_tick_frequency": 25,
        "y_bottom_tick": None,
        "x_tick_frequency": (maximum - minimum)/n,
        "x_axis_width": 11,
        "y_axis_height": 6.5,
        "x_labeled_nums": np.linspace(minimum, maximum, n+1),
        "y_labeled_nums": np.arange(0, 201, 50),
        "x_axis_label": "$m$",
        "y_axis_label": "$r$",
        "axes_color": GRAY,
        "camera_config": {"background_color": WHITE},
        "x_label_background_color": WHITE,
        "y_label_background_color": WHITE,
        "x_label_fill_color": GREY,
        "y_label_fill_color": GREY,
        "x_label_scale": 1,
        "y_label_scale": 1,
        "x_decimal_number_config": {"num_decimal_places": 0, "background_stroke_color": WHITE, "fill_color": GREY},
        "x_label_num_scale_val": 1,
        "y_decimal_number_config": {"num_decimal_places": 0, "background_stroke_color": WHITE, "fill_color": GREY},
        "y_label_num_scale_val": 1,
        "text_config": {"background_stroke_color": WHITE, "fill_color": BLACK}
    }

    def construct(self):
        im = VGroup()

        self.graph_origin = 5 * LEFT + 4 * DOWN
        self.setup_axes(animate=True)
        im.add(self.axes)

        hyp_graph = DashedVMobject(self.get_graph(self.hyp_func, **self.hyp_func_kwargs))
        real_graph = self.get_graph(self.real_func, **self.real_func_kwargs)
        self.play(ShowCreation(hyp_graph), ShowCreation(real_graph))
        im.add(hyp_graph, real_graph)

        dots = []
        for dot in self.data:
            d = Dot(self.coords_to_point(dot[0], dot[1]), color=BLACK)
            dots.append(d)

        self.play(*[ShowCreation(p) for p in dots])
        im.add(*dots)

        im.move_to(ORIGIN)

        self.wait(5)


class ScaledShapes(ThreeDScene):
    CONFIG = {
        "camera_config": {"background_color": WHITE},
    }
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        c = Cube(fill_color= GREY, stroke_width=1, stroke_color= BLACK)
        self.play(ShowCreation(c))

        self.wait(5)


class SimilarTriangleProblem(Scene):
    CONFIG = {

        "shape_config": {"stroke_color": BLACK, "fill_opacity":0.5, "fill_color": GREY},
        "shape_verts": [4*RIGHT + 3*UP, 3*LEFT + 2*UP, 2*LEFT + 3* DOWN],
        "proportion":0.5,

        "big_left": True,
        "big_up": True,
        "big_hyp": True,
        "small_left": True,
        "small_up": True,
        "small_hyp": True,

        "camera_config": {"background_color": WHITE},
        "text_config": {"stroke_color": WHITE, "fill_color": BLACK}
    }

    def construct(self):
        prop = self.proportion

        # useful constants for directions and lengths
        vertices = self.shape_verts
        up_dir = vertices[1] - vertices[0]
        up_angle = math.atan2(-up_dir[1], -up_dir[0])
        up_perp_dir = np.array([up_dir[1], -up_dir[0], 0])
        up_len = np.linalg.norm(up_dir)

        left_dir = vertices[2] - vertices[1]
        left_angle = math.atan2(-left_dir[1], -left_dir[0])
        left_perp_dir = np.array([left_dir[1], -left_dir[0], 0])
        left_len = np.linalg.norm(left_dir)

        hyp_dir = vertices[2] - vertices[0]
        hyp_angle = math.atan2(-hyp_dir[1], -hyp_dir[0])
        hyp_perp_dir = np.array([-hyp_dir[1], hyp_dir[0], 0])
        hyp_len = np.linalg.norm(hyp_dir)



        # big
        big_tri = Polygon(*vertices, **self.shape_config)
        #elements.append(big_tri)

        big_left_text = "$a = " + str(round(left_len, 1)) + "$" if self.big_left else "$a$"
        big_left = TextMobject(big_left_text, **self.text_config).rotate(left_angle)
        big_left.move_to(vertices[1] + 0.5 * left_dir + 0.4 * left_perp_dir/left_len)
        #elements.append(big_left)

        big_up_text = "$b = " + str(round((1-prop)*up_len, 1)) + "$" if self.big_up else "$b$"
        big_up = TextMobject(big_up_text, **self.text_config).rotate(up_angle)
        big_up.move_to(((1+prop)/2) * up_dir + vertices[0] + 0.4 * up_perp_dir/up_len)
        #elements.append(big_up)

        big_hyp_text = "$c =" + str(round((1-prop)*hyp_len, 1)) + "$" if self.big_hyp else "$c$"
        big_hyp = TextMobject(big_hyp_text, **self.text_config).rotate(hyp_angle)
        big_hyp.move_to(((1+prop)/2) * hyp_dir + vertices[0] + 0.4 * hyp_perp_dir/hyp_len)
        #elements.append(big_hyp)

        big = VGroup(big_tri, big_left, big_up, big_hyp)


        # small
        small_vertices = lambda al: [vertices[0], al * up_dir + vertices[0],
                                     al * hyp_dir + vertices[0]]
        small_tri =  Polygon(*small_vertices(self.proportion), **self.shape_config).set_color(DARKER_GREY)
        #elements.append(small_tri)

        small_left_text = "$d = " + str(round(prop * left_len, 1)) + "$" if self.small_left else "$d$"
        small_left = TextMobject(small_left_text, **self.text_config).rotate(left_angle)
        small_left.move_to(vertices[0] + prop * up_dir + 0.5 * prop * left_dir + 0.4 * left_perp_dir / left_len)
        #elements.append(small_left)

        small_up_text = "$e = " + str(round((prop) * up_len, 1)) + "$" if self.small_up else "$e$"
        small_up = TextMobject(small_up_text, **self.text_config).rotate(up_angle)
        small_up.move_to(0.5 * prop * up_dir + vertices[0] + 0.4 * up_perp_dir / up_len)
        #elements.append(small_up)

        small_hyp_text = "$f =" + str(round((prop) * hyp_len, 1)) + "$" if self.small_hyp else "$f$"
        small_hyp = TextMobject(small_hyp_text, **self.text_config).rotate(hyp_angle)
        small_hyp.move_to(0.5 * prop * hyp_dir + vertices[0] + 0.4 * hyp_perp_dir / hyp_len)
        #elements.append(small_hyp)

        small = VGroup(small_tri, small_up, small_left, small_hyp)


        # display
        elements = VGroup(big, small).move_to(ORIGIN)
        self.play(Write(elements))

        self.wait(5)